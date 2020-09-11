# Queue trigger in Python to create new nodes in the graph database

This is a Queue trigger function written in Python in Visual Studio Code as the editor. When it recieves a item in the queue, creates a node in the Cosmos DB using Gremlin API. The beauty of a graph database is, it facililates to store the data or nodes along with its relationships 

## Technology stack  
* Python version 3.7.9 64 bit version https://www.python.org/downloads/release/python-379/
* Azure functions for python version 1.2 *(azure-functions 1.2.0)* https://pypi.org/project/azure-functions/
* gremlinpython version 3.4.6, to connect to the Cosmos DB with Gremlin API *(pip install gremlinpython)* https://pypi.org/project/gremlinpython/

## How to run the solution
 * Create a storage account and create a queue inside it, Go to the Access keys section and get the connection string and provide it to the AzureWebJobsStorage setting in local.settings.json file
 * You have to create a Cosmos DB account with Gremlin (Graph) API then go to the Keys section, get the Gremlin endpoint and key to connect to the database
 * Create a database and graph inside the Cosmos DB account, use the same values for the settings database and collection entries
 * Open the solution file in Visual Studio and run the project
 * Insert a new item in the queue and check it is inserted to the graph database
