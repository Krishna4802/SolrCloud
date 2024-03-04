# SolrCloud Commands

    docker run -dit -p 7574:7574 -p 8983:8983 -p 8984:8984 --name solr ubuntu
    
    docker exec -ti solr bash 
        1  apt update
        2  apt install default-jre
        3  apt-get install wget
        4  wget https://archive.apache.org/dist/lucene/solr/8.11.0/solr-8.11.0.tgz
        5  tar -xzf solr-8.11.0.tgz
        6  cd solr-8.11.0
        7  bin/solr -e cloud -force
        8  bin/solr zk downconfig -n _default -d server/solr/configsets/test -z 172.17.0.2:9983
        9  cd server
       10  cd solr
       11  cd configsets/
       12  cd test
       13  cd conf/
       14  mv managed-schema schema.xml
       15  cd ../
       16  bin/solr zk upconfig -n test -d server/solr/configsets/test/conf -z 172.17.0.2:9983     

# Child filter
    *,[child parentFilter=id:* limit=-1]


# to check logs  
    cd /solr-8.11.0/example/cloud/node1/solr/../logs
    tail -200f solr.log

# To reload collection
    curl 'http://localhost:8983/solr/admin/collections?action=RELOAD&name=patent_1'  Stop command : bin/solr stop -all start again command : bin/solr start -c -p 8983 -z localhost:2181/solr -force

    Stop command : bin/solr stop -all 
    start again command : bin/solr start -c -p 8983 -z localhost:2181/solr -force

# Command for deleting config
    curl -X DELETE "http://localhost:8088/solr/admin/configs?action=DELETE&name=test"

# To delete the data 
    curl -X POST -H "Content-Type: application/json" "http://localhost:8983/solr/nest2/update" -d '{
      "delete": {
        "query": "*:*"
      },
      "commit": {}
    }'

    <delete><query>*:*</query></delete> in UI 

**For searching :**  find / -name "start.jar" 2>/dev/null

# Python code index the data  import requests

        import json
        from IPython import embed
        
        def index_data_to_solr_cloud(solr_url, collection_name, data_file_path):
            # Read data from the JSON file
            with open(data_file_path, 'r') as file:
                data = json.load(file)
            # Prepare the Solr URL for the new collection
            solr_update_url = f"{solr_url}/solr/{collection_name}/update"
            # Prepare headers for the POST request
            headers = {'Content-Type': 'application/json'}
            # Send the data to Solr for indexing
            response = requests.post(solr_update_url, json=data, headers=headers)
            # Commit the changes to make them visible in the index
            commit_url = f"{solr_url}/solr/{collection_name}/update?commit=true"
            requests.post(commit_url)
            # Check if the indexing was successful
            if response.status_code == 200:
                print("Data indexed successfully!")
            else:
                print(f"Error indexing data: {response.status_code} - {response.text}")
        if __name__ == "__main__":
            solr_cloud_url = "http://localhost:8983"
            collection_name = "patent_1"
            data_file_path = "/Users/krishnaprasath/Documents/postgress/data.json"
            index_data_to_solr_cloud(solr_cloud_url, collection_name, data_file_path)


## Upconfig and Downconfig

        solr-8.7.0/server/scripts/cloud-scripts/zkcli.sh -zkhost "localhost:2181" -cmd downconfig -confname analyst_default_conf -confdir "/tmp/analyst_conf_8_11"
        
        solr-8.11.2/server/scripts/cloud-scripts/zkcli.sh -zkhost "localhost:2181" -cmd upconfig -confname  -confdir "/tmp/acl_test
