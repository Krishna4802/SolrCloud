# Shard Moving in SolrCloud

* Create the collection
* Index the data to it


In my case : create a replica in the shard2 as same as in Shard1 and delete the previous replica from shard2 (now it will be like the rpx machine)

# Command to create replica :

    curl -X POST -H 'Content-Type: application/json' \
      'http://localhost:8983/solr/admin/collections?action=ADDREPLICA&collection=<collection_name>&shard=<shard_name>&replica.type=<replica_type>&node=<target_node>'


# For my case :

    curl -X POST -H 'Content-Type: application/json' \
      'http://localhost:8983/solr/admin/collections?action=ADDREPLICA&collection=replica&shard=shard1&replica.type=NRT&node=192.168.32.6:8983_solr'


After indexing the data delete the replica that you have moved to new node 
