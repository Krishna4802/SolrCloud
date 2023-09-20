* Hard Commit : updates are immediately saved to the index and visible for searching
* Soft Commit : updates are quickly visible for searching but not immediately saved to disk


### 1. Soft Commit:
* Use soft commits to quickly make data visible for searching.
* Set up an auto-soft commit strategy based on time intervals or document counts. For example, you can configure Solr to perform a soft commit every 15 second or after indexing a certain number of documents (e.g., every 1,000 documents).
* This will ensure that most of your data is visible for searching within seconds.

### 2. Hard Commit:
* Perform hard commits at regular intervals (e.g., every 5 minutes).
* Hard commits make sure that the data is securely saved to disk and is durable. It's a safety net to protect your data.
* Even if you perform hard commits less frequently, the soft commits will ensure that most of the data is available for searching in near-real-time


## Task:
Set soft Commit to 30 seconds
Set hard commit to 60 seconds

Shell

1. Date in between all steps
2. Index one record
3. Verify that record
4. Verify tlog size
5. Wait for 30 seconds
6. Verify record
7. Verify tlog size
8. Wait for 30 seconds
9. Verify t log size



## Shell Commands

    echo “$(date): Indexing Sample Record”
    
    curl —s -X POST -H "Content-Type: application/json" --data '[
      {
        "id": "1",
        "title": "Sample Document",
        "content": "This is a sample document for indexing in Solr."
      }
    ]' "http://localhost:8983/solr/commit/update"
    
    echo “$(date): Verifying the record in solr”
    curl -s “http://localhost:8983/solr/commit/select?q=*:*"
    
    ls -lhtr /solr-8.11.2/example/cloud/node1/solr/commit_shard2_replica_n2/data/tlog
    
    echo “$(date): Sleeping for 30 seconds to finish soft commit”
    sleep 30
    
    echo “$(date): Verifying the record in solr again”
    curl -s “http://localhost:8983/solr/commit/select?q=*:*"
    ls -lhtr /solr-8.11.2/example/cloud/node1/solr/commit_shard2_replica_n2/data/tlog
    
    	echo “$(date): Sleeping for 30 seconds to finish hard commit”
    sleep 30
    
    echo “$(date): Verifying the record in solr again”
    curl -s “http://localhost:8983/solr/commit/select?q=*:*"
    ls -lhtr /solr-8.11.2/example/cloud/node1/solr/commit_shard2_replica_n2/data/tlog
