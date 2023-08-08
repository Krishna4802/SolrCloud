Day 6 - Securing Solo

docker run -dit -p 7574:7574 -p 8983:8983 -p 8984:8984 --name solr ubuntu

 docker exec -ti solr bash 
    1  apt update
    2  apt install default-jre
    3  apt-get install wget
    4  wget https://archive.apache.org/dist/lucene/solr/8.11.0/solr-8.11.0.tgz
    5  tar -xzf solr-8.11.0.tgz
    6  cd solr-8.11.0
    7  bin/solr -e cloud -force
    8  bin/solr auth enable -type basicAuth -prompt true -z localhost:9983 -blockUnknown true


Security.Json File

{
  "authentication":{
    "blockUnknown":true,
    "class":"solr.BasicAuthPlugin",
    "credentials":{
      "krishna":"pzn8wgIn9qRo+MVGKRGwapOzDeEGdVk5Oih9Rk2149Q= 4HOecBquEyV3zKc75OhT2xmjEUzIpdISF/8EHG6CcQ0=",
      "shanthini":"zmO7FNGeJkuXNthVoWhBcqXCx/LBlReamvQf0RuTL3U= Juy/NsXNECXcfxFUadT8Hbv06le5T/N13kN0KCQaOuM="},
    "":{"v":9},
    "forwardCredentials":true},
  "authorization":{
    "class":"solr.RuleBasedAuthorizationPlugin",
    "permissions":[
      {
        "name":"security-edit",
        "role":"admin",
        "index":1},
      {
        "name":"security-read",
        "role":"admin",
        "index":2},
      {
        "name":"config-edit",
        "role":"admin",
        "index":3},
      {
        "name":"collection-admin-edit",
        "role":"admin",
        "index":4},
      {
        "name":"core-admin-edit",
        "role":"admin",
        "index":5},
      {
        "name":"schema-read",
        "role":["user"],
        "index":6}],
    "user-role":{
      "krishna":"admin",
      "shanthini":["user"]},
    "":{"v":15}}}



Python code to index data

import requests
import json

def index_data_to_solr(json_file_path, solr_collection_url, username, password):
    # Read data from JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Define headers for the Solr API request
    headers = {'Content-Type': 'application/json'}

    # Construct the Solr update URL
    update_url = f'{solr_collection_url}/update'

    # Convert data to Solr's required format (add or update)
    solr_data = [{'add': doc} for doc in data]

    # Send the data to Solr using the POST request
    response = requests.post(update_url, json=solr_data, headers=headers, auth=(username, password))

    # Check the response status
    if response.status_code == 200:
        print('Data indexed successfully in Solr.')
    else:
        print(f'Error indexing data: {response.text}')

# Example usage
if __name__ == "__main__":
    json_file_path = '/Users/krishnaprasath/Documents/Solr/mobile_data.json'
    solr_collection_url = 'http://localhost:8983/solr/test5'
    solr_username = 'krishna'
    solr_password = '1234'
    
    index_data_to_solr(json_file_path, solr_collection_url, solr_username, solr_password)




To enable TLS  # Enables HTTPS. It is implicitly true if you set SOLR_SSL_KEY_STORE. Use this config
# to enable https module with custom jetty configuration.
SOLR_SSL_ENABLED=true
# Uncomment to set SSL-related system properties
# Be sure to update the paths to the correct keystore for your environment
SOLR_SSL_KEY_STORE=etc/solr-ssl.keystore.p12
SOLR_SSL_KEY_STORE_PASSWORD=secret
SOLR_SSL_TRUST_STORE=etc/solr-ssl.keystore.p12
SOLR_SSL_TRUST_STORE_PASSWORD=secret
# Require clients to authenticate
SOLR_SSL_NEED_CLIENT_AUTH=false
# Enable clients to authenticate (but not require)
SOLR_SSL_WANT_CLIENT_AUTH=false
# SSL Certificates contain host/ip "peer name" information that is validated by default. Setting
# this to false can be useful to disable these checks when re-using a certificate on many hosts
SOLR_SSL_CHECK_PEER_NAME=true


Apply this in /solr-8.11.0/bin/solr.in.sh
