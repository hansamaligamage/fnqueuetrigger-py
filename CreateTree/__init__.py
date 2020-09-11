import logging
import json
from gremlin_python.driver import client, serializer

import azure.functions as func

def main(msg: func.QueueMessage) -> None:
    logging.info('Python queue trigger function processed a queue item: %s', msg.get_body().decode('utf-8'))

    personstring = msg.get_body().decode('utf-8')
    person = json.loads(personstring)

    graphclient = createclient()

    query = "g.addV('profile').property('id', '" + person['id'] + "').property('name', '" + person['name'] +"').property('city', '" + person['city'] + "')"
    insert_vertices(graphclient, query)

    try:
        connections = person['connections']
    except KeyError :
        connections = None

    if connections != None : 
        for connection in connections :
            query = "g.V('" + person['id'] + "').addE('" +  connection['relationship'] + "').to(g.V('" + connection['relatedperson'] + "'))"
            insert_edges(client, query)

def createclient ():
    graphclient = client.Client('wss://persongraph.gremlin.cosmosdb.azure.com:443/', 'g', username="/dbs/persondb/colls/profile",
         password="ojkqBjav8vMWmFJOIeg3vaZWQ3b1CDKkyWKt4A4CN8bnwyDbvep9vrrxXOfwxvEGX15mnrbDDCmp2IMbaktzVA==", message_serializer=serializer.GraphSONSerializersV2d0())
    return graphclient

def cleanup_graph(client):
    callback = client.submitAsync(_gremlin_cleanup_graph)
    if callback.result() is not None:
        logging.info("\tCleaned up the graph!")

def insert_vertices(client, query):
    callback = client.submitAsync(query)
    if callback.result() is not None:
        logging.info("\tInserted this vertex:\n\t{0}\n".format(callback.result().one()))
    else:
        logging.info("Something went wrong with this query: {0}".format(query))

def insert_edges(client, query):
    callback = client.submitAsync(query)
    if callback.result() is not None:
        print("\tInserted this edge:\n\t{0}\n".format(callback.result().one()))
    else:
        print("Something went wrong with this query:\n\t{0}".format(query))
