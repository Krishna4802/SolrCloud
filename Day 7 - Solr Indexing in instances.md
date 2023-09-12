* docker run -dit -p 7574:7574 -p 8983:8983 -p 8984:8984 --name solr ubuntu
* docker exec -ti solr bash

        1  apt update
        2  apt install default-jre
        3  apt-get install wget
        4  wget https://archive.apache.org/dist/lucene/solr/8.11.0/solr-8.11.0.tgz
        5  tar -xzf solr-8.11.0.tgz
        6  cd solr-8.11.0

## Now create the instance of solrcloud

    * bin/solr -e cloud -force
    * Create the cluster as usual
        * Go the the file location - /solr-8.11.0/server/solr/configsets/test1/conf/
    * bin/solr zk downconfig -n _default -d server/solr/configsets/test -z 172.17.0.2:9983
    * mv managed-schema schema.xml
        * Change the content of schema.xml and solrconfig.xml
    * bin/solr zk upconfig -n test -d server/solr/configsets/test/conf -z 172.17.0.2:9983
    * Create the collection and index the data to the collection 


## Now create the another instance of solrcloud

    * bin/solr start -c -p 8984 -force
    * bin/solr zk downconfig -n test -d server/solr/configsets/test1 -z 172.17.0.2:9983
    * bin/solr zk upconfig -n test1 -d server/solr/configsets/test1/conf -z 172.17.0.2:9984   -> upconfig in the 9984 (newly created instance)
    * Now create a collection there 
    * Execture the python code to move the data from one instance to another


## Python code to move the data from instance to instance in solr cloud

    import pysolr
    # Connect to the source SolrCloud instance
    source_url = 'http://localhost:8983/solr/test'
    source_solr = pysolr.Solr(source_url)
    
    # Connect to the target SolrCloud instance
    target_url = 'http://localhost:8984/solr/test'
    target_solr = pysolr.Solr(target_url)
    
    # Query and iterate over the documents in the source collection
    query = '*:*'
    results = source_solr.search(query, rows=1000)
    for doc in results:
        # Remove "_version_" field if present (not needed for indexing)
        if "_version_" in doc:
            del doc["_version_"]
        
        # Index each document to the target collection
        target_solr.add([doc])
    
    # Commit the changes to the target collection
    target_solr.commit()
    
    print("Data transfer completed.")


