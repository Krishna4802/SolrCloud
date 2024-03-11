## Log in to zookeeper client from zookeepers bin location
	./zkCli.sh

## To download the security.json file to local
    /solr-8.11.2/server/scripts/cloud-scripts/zkcli.sh -zkhost localhost:2181 -cmd get /security.json > /tmp/security.json

## Modification of security.json
	vi /tmp/security.json

## add in the end of security.json file in zookeeper 
      "auditlogging": {
        "class": "solr.SolrLogAuditLoggerPlugin",
        "async": true,
        "blockAsync": false,
        "numThreads": 2,
        "queueSize": 4096,
        "eventTypes": ["AUTHENTICATED", "REJECTED", "ANONYMOUS", "ANONYMOUS_REJECTED", "AUTHORIZED", "UNAUTHORIZED", "COMPLETED", "ERROR"]
      }
    }

## to upload the security.json file to machine
    /solr-8.11.2/server/scripts/cloud-scripts/zkcli.sh -zkhost localhost:2181 -cmd putfile /security.json /tmp/security.json
