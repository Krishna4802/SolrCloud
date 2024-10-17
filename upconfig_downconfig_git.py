Manoj task - Down,Up,create,alias


Python code to downconfig

import os
import requests
import subprocess

def get_solr_collections(solr_url):
    collections_endpoint = f"{solr_url}/solr/admin/collections?action=LIST"

    response = requests.get(collections_endpoint)

    if response.status_code == 200:
        collections_data = response.json()
        return collections_data.get('collections', [])
    else:
        print(f"Failed to get collection list. Status code: {response.status_code}, Response: {response.text}")
        return None

def get_solr_cluster_status(solr_url, collection_name):
    cluster_status_endpoint = f"{solr_url}/solr/admin/collections?action=CLUSTERSTATUS"

    response = requests.get(cluster_status_endpoint)

    if response.status_code == 200:
        cluster_status = response.json()

        if collection_name in cluster_status['cluster']['collections']:
            config_name = cluster_status['cluster']['collections'][collection_name]['configName']
            return config_name
        else:
            print(f"Collection '{collection_name}' not found in the cluster.")
            return None
    else:
        print(f"Failed to get cluster status. Status code: {response.status_code}, Response: {response.text}")
        return None

def download_solr_config_with_zkcli(zkcli_path, zkhost, config_name, local_dir, collection_name):
    collection_dir = os.path.join(local_dir, collection_name)
    os.makedirs(collection_dir, exist_ok=True)

    zkcli_command = [
        zkcli_path,
        "-zkhost", zkhost,
        "-cmd", "downconfig",
        "-confname", config_name,
        "-confdir", collection_dir
    ]

    subprocess.run(zkcli_command)

# Example usage
solr_url = "http://localhost:8983"
zkcli_path = "/solr-8.11.2/server/scripts/cloud-scripts/zkcli.sh"
zkhost = "localhost:9983"
local_dir = "/media"

collections = get_solr_collections(solr_url)

if collections:
    if len(collections) == 1:
        collection_name = collections[0]
    else:
        print("Multiple collections found:", collections)
        collection_name = input("Enter the name of the collection you want to download configuration for: ")

    config_name = get_solr_cluster_status(solr_url, collection_name)

    if config_name:
        print(f"Config name for the collection '{collection_name}': {config_name}")

        download_solr_config_with_zkcli(zkcli_path, zkhost, config_name, local_dir, collection_name)
        print(f"Configuration downloaded to '{os.path.join(local_dir, collection_name)}'")
    else:
        print(f"Failed to get config name for the collection '{collection_name}'.")
else:
    print("No collections found in the cluster.")


—————————————————————————————————————————————————————————————————————————————


Python code to Upconfig


#Working Code

import subprocess
import os

def upload_solr_config_with_zkcli(zkcli_path, zkhost, config_name, config_dir):
    # Construct the zkcli.sh command to upload the configuration
    zkcli_command = [
        zkcli_path,
        "-zkhost", zkhost,
        "-cmd", "upconfig",
        "-confname", config_name,
        "-confdir", config_dir
    ]

    # Execute the command
    subprocess.run(zkcli_command)

# Example usage
zkcli_path = "/solr-8.11.2/server/scripts/cloud-scripts/zkcli.sh"
zkhost = "localhost:9983"

# Get user input for config_name and config_dir
config_name = input("Solr configuration Name: ")
config_dir = input("Configuration files Location: ")

# Upload configuration
upload_solr_config_with_zkcli(zkcli_path, zkhost, config_name, config_dir)



—————————————————————————————————————————————————————————————————————————————


Python code to create collection

import requests

def get_solr_cluster_status(solr_url):
    cluster_status_endpoint = f"{solr_url}/solr/admin/collections?action=CLUSTERSTATUS"
    
    response = requests.get(cluster_status_endpoint)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get cluster status. Status code: {response.status_code}, Response: {response.text}")
        return None

def create_solr_collection_command(solr_url, cluster_status, collection_name):
    if cluster_status:
        collections = cluster_status['cluster']['collections']
        
        # Choose a live node as the target for the collection creation command
        live_nodes = cluster_status['cluster']['live_nodes']
        if live_nodes:
            target_node = live_nodes[0]
        else:
            print("No live nodes found in the cluster.")
            return None
        
        # Check if the provided collection name exists in the cluster status
        if collection_name in collections:
            collection_details = collections[collection_name]

            # Fetch existing configuration name
            config_name = collection_details['configName']

            # Check if shards and replicas are available
            if 'shards' in collection_details and collection_details['shards']:
                # Take the first shard and its first replica if available
                first_shard = next(iter(collection_details['shards'].values()))
                if 'replicas' in first_shard and first_shard['replicas']:
                    first_replica = next(iter(first_shard['replicas'].values()))

                    # Fetch required parameters
                    num_shards = len(collection_details['shards'])
                    max_shards_per_node = collection_details['maxShardsPerNode']
                    tlog_replicas = collection_details.get('tlogReplicas', 0)
                    pull_replicas = collection_details.get('pullReplicas', 0)

                    # Construct the Solr collection creation command
                    command = (
                        f"{solr_url}/solr/admin/collections?action=CREATE"
                        f"&name={collection_name}"
                        f"&numShards={num_shards}"
                        f"&createNodeSet={target_node}"
                        f"&configName={config_name}"
                        f"&maxShardsPerNode={max_shards_per_node}"
                        f"&tlogReplicas={tlog_replicas}"
                        f"&pullReplicas={pull_replicas}"
                    )

                    return command
                else:
                    print(f"No replicas found for the first shard of collection '{collection_name}'.")
            else:
                print(f"No shards found for collection '{collection_name}'.")
        else:
            print(f"Collection '{collection_name}' not found in the Solr cluster.")
            return None
    else:
        return None

def main():
    solr_url = "http://localhost:8983"

    cluster_status = get_solr_cluster_status(solr_url)

    if cluster_status:
        collections = cluster_status['cluster']['collections']

        if not collections:
            print("No collections found in the Solr cluster.")
            return

        print("Available collections in the Solr cluster:")
        for collection_name in collections:
            print(collection_name)

        user_collection_name = input("Enter the collection name: ").strip().replace(" ", "_")

        if user_collection_name:
            collection_command = create_solr_collection_command(
                solr_url, cluster_status, user_collection_name
            )

            if collection_command:
                print(f"Solr collection creation command:\n{collection_command}")
            else:
                print("Failed to generate collection creation command.")
        else:
            print("Exiting without creating a collection.")
    else:
        print("Failed to get Solr cluster status.")

if __name__ == "__main__":
    main()



—————————————————————————————————————————————————————————————————————————————


Python code to create Alias

import requests

def get_solr_cluster_status(solr_url):
    cluster_status_endpoint = f"{solr_url}/solr/admin/collections?action=CLUSTERSTATUS"
    
    response = requests.get(cluster_status_endpoint)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get cluster status. Status code: {response.status_code}, Response: {response.text}")
        return None

def create_solr_alias_command(solr_url, cluster_status, alias_name):
    if cluster_status:
        aliases = cluster_status['cluster']['aliases']

        # Check if the provided alias name exists in the cluster status
        if alias_name not in aliases:
            print(f"Alias '{alias_name}' not found in the Solr cluster.")
            return None

        alias_collections = aliases[alias_name].split(',')

        alias_command = (
            f"{solr_url}/solr/admin/collections?action=CREATEALIAS"
            f"&name={alias_name}"
            f"&collections={','.join(alias_collections)}"
        )

        return alias_command
    else:
        return None

def main():
    solr_url = "http://localhost:8983"

    cluster_status = get_solr_cluster_status(solr_url)

    if cluster_status:
        aliases = cluster_status['cluster']['aliases']

        if not aliases:
            print("No aliases found in the Solr cluster.")
            return

        print("Available aliases in the Solr cluster:")
        for alias_name in aliases:
            print(alias_name)

        user_alias_name = input("Enter the alias name to create: ").strip().replace(" ", "_")

        alias_command = create_solr_alias_command(solr_url, cluster_status, user_alias_name)

        if alias_command:
            print(f"Solr alias creation command:\n{alias_command}")
        else:
            print("Failed to generate alias creation command.")
    else:
        print("Failed to get Solr cluster status.")

if __name__ == "__main__":
    main()


—————————————————————————————————————————————————————————————————————————————


All in One code


import requests
import subprocess
import os

def get_solr_collections(solr_url, username, password):
    collections_endpoint = f"{solr_url}/solr/admin/collections?action=LIST"
    response = requests.get(collections_endpoint, auth=(username, password))

    if response.status_code == 200:
        collections_data = response.json()
        return collections_data.get('collections', [])
    else:
        print(f"Failed to get collection list. Status code: {response.status_code}, Response: {response.text}")
        return None

def get_solr_cluster_status(solr_url, username, password, collection_name=None):
    cluster_status_endpoint = f"{solr_url}/solr/admin/collections?action=CLUSTERSTATUS"
    response = requests.get(cluster_status_endpoint, auth=(username, password))

    if response.status_code == 200:
        cluster_status = response.json()

        if collection_name and collection_name not in cluster_status['cluster']['collections']:
            print(f"Collection '{collection_name}' not found in the cluster.")
            return None
        else:
            return cluster_status
    else:
        print(f"Failed to get cluster status. Status code: {response.status_code}, Response: {response.text}")
        return None

def download_solr_config_with_zkcli(zkcli_path, zkhost, config_name, local_dir, collection_name, username, password):
    collection_dir = os.path.join(local_dir, collection_name)
    os.makedirs(collection_dir, exist_ok=True)

    zkcli_command = [
        zkcli_path,
        "-zkhost", zkhost,
        "-cmd", "downconfig",
        "-confname", config_name,
        "-confdir", collection_dir
    ]

    subprocess.run(zkcli_command)

def upload_solr_config_with_zkcli(zkcli_path, zkhost, config_name, config_dir, username, password):
    zkcli_command = [
        zkcli_path,
        "-zkhost", zkhost,
        "-cmd", "upconfig",
        "-confname", config_name,
        "-confdir", config_dir
    ]

    subprocess.run(zkcli_command, check=True)

def create_solr_collection_command(solr_url, cluster_status, collection_name, username, password):
    if cluster_status:
        collections = cluster_status['cluster']['collections']
        
        # Choose a live node as the target for the collection creation command
        live_nodes = cluster_status['cluster']['live_nodes']
        if live_nodes:
            target_node = live_nodes[0]
        else:
            print("No live nodes found in the cluster.")
            return None
        
        # Check if the provided collection name exists in the cluster status
        if collection_name in collections:
            collection_details = collections[collection_name]

            # Fetch existing configuration name
            config_name = collection_details['configName']

            # Check if shards and replicas are available
            if 'shards' in collection_details and collection_details['shards']:
                # Take the first shard and its first replica if available
                first_shard = next(iter(collection_details['shards'].values()))
                if 'replicas' in first_shard and first_shard['replicas']:
                    first_replica = next(iter(first_shard['replicas'].values()))

                    # Fetch required parameters
                    num_shards = len(collection_details['shards'])
                    max_shards_per_node = collection_details['maxShardsPerNode']
                    tlog_replicas = collection_details.get('tlogReplicas', 0)
                    pull_replicas = collection_details.get('pullReplicas', 0)

                    # Construct the Solr collection creation command
                    command = (
                        f"{solr_url}/solr/admin/collections?action=CREATE"
                        f"&name={collection_name}"
                        f"&numShards={num_shards}"
                        f"&createNodeSet={target_node}"
                        f"&configName={config_name}"
                        f"&maxShardsPerNode={max_shards_per_node}"
                        f"&tlogReplicas={tlog_replicas}"
                        f"&pullReplicas={pull_replicas}"
                    )

                    return command
                else:
                    print(f"No replicas found for the first shard of collection '{collection_name}'.")
            else:
                print(f"No shards found for collection '{collection_name}'.")
        else:
            print(f"Collection '{collection_name}' not found in the Solr cluster.")
            return None
    else:
        return None

def create_solr_alias_command(solr_url, cluster_status, alias_name, username, password):
    if cluster_status:
        aliases = cluster_status['cluster']['aliases']

        # Check if the provided alias name exists in the cluster status
        if alias_name not in aliases:
            print(f"Alias '{alias_name}' not found in the Solr cluster.")
            return None

        alias_collections = aliases[alias_name].split(',')

        alias_command = (
            f"{solr_url}/solr/admin/collections?action=CREATEALIAS"
            f"&name={alias_name}"
            f"&collections={','.join(alias_collections)}"
        )

        return alias_command
    else:
        return None

def main():
    solr_url = "http://localhost:8983"
    username = "krish"
    password = "123"
    zkcli_path = "/solr-8.11.2/server/scripts/cloud-scripts/zkcli.sh"
    local_dir = "/media"

    print("1. Download Solr Configuration")
    print("2. Upload Solr Configuration")
    print("3. Create Solr Collection")
    print("4. Create Solr Alias")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        collections = get_solr_collections(solr_url, username, password)

        if collections:
            if len(collections) == 1:
                collection_name = collections[0]
            else:
                print("Multiple collections found:", collections)
                collection_name = input("Enter the name of the collection you want to download configuration for: ")

            config_name = get_solr_cluster_status(solr_url, username, password, collection_name)

            if config_name:
                print(f"Config name for the collection '{collection_name}': {config_name}")

                download_solr_config_with_zkcli(zkcli_path, solr_url, config_name, local_dir, collection_name, username, password)
                print(f"Configuration downloaded to '{os.path.join(local_dir, collection_name)}'")
            else:
                print(f"Failed to get config name for the collection '{collection_name}'.")
        else:
            print("No collections found in the cluster.")
    elif choice == "2":
        config_name = input("Solr configuration Name: ")
        config_dir = input("Configuration files Location: ")

        upload_solr_config_with_zkcli(zkcli_path, solr_url, config_name, config_dir, username, password)
    elif choice == "3":
        cluster_status = get_solr_cluster_status(solr_url, username, password)

        if cluster_status:
            collections = cluster_status['cluster']['collections']

            if not collections:
                print("No collections found in the Solr cluster.")
                return

            print("Available collections in the Solr cluster:")
            for collection_name in collections:
                print(collection_name)

            user_collection_name = input("Enter the collection name: ").strip().replace(" ", "_")

            if user_collection_name:
                collection_command = create_solr_collection_command(
                    solr_url, cluster_status, user_collection_name, username, password
                )

                if collection_command:
                    print(f"Solr collection creation command:\n{collection_command}")
                else:
                    print("Failed to generate collection creation command.")
            else:
                print("Exiting without creating a collection.")
        else:
            print("Failed to get Solr cluster status.")
    elif choice == "4":
        cluster_status = get_solr_cluster_status(solr_url, username, password)

        if cluster_status:
            aliases = cluster_status['cluster']['aliases']

            if not aliases:
                print("No aliases found in the Solr cluster.")
                return

            print("Available aliases in the Solr cluster:")
            for alias_name in aliases:
                print(alias_name)

            user_alias_name = input("Enter the alias name to create: ").strip().replace(" ", "_")

            alias_command = create_solr_alias_command(solr_url, cluster_status, user_alias_name, username, password)

            if alias_command:
                print(f"Solr alias creation command:\n{alias_command}")
            else:
                print("Failed to generate alias creation command.")
        else:
            print("Failed to get Solr cluster status.")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()



—————————————————————————————————————————————————————————————————————————————


GitHub to solr 


import subprocess
import os
from git import Repo

def clone_repo(github_repo_url, local_repo_path):
    if os.path.exists(local_repo_path):
        subprocess.run(["rm", "-rf", local_repo_path], check=True)

    Repo.clone_from(github_repo_url, local_repo_path)

def upload_solr_config(github_repo_url, local_repo_path, solr_version, zk_host):
    clone_repo(github_repo_url, local_repo_path)

    repo_files = [f for f in os.listdir(local_repo_path) if not f.startswith('.')]
    
    if not repo_files:
        print(f"No files found in the cloned repository. Exiting.")
        return

    print("Available Solr Configs:")
    for idx, file_name in enumerate(repo_files, start=1):
        print(f"{idx}. {file_name}")

    while True:
        try:
            selected_index = int(input("Enter the index of the Solr config to upload: "))
            selected_file = repo_files[selected_index - 1]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid index.")

    conf_name = input(f"Enter a name for the Solr config '{selected_file}': ")

    zkcli_command = f"/{solr_version}/server/scripts/cloud-scripts/zkcli.sh"
    conf_dir = os.path.join(local_repo_path, selected_file)

    upload_command = [
        zkcli_command,
        "-zkhost", zk_host,
        "-cmd", "upconfig",
        "-confname", conf_name,
        "-confdir", conf_dir
    ]

    subprocess.run(upload_command, check=True)

github_repo_url = "https://github.com/Krishna4802/config"
local_repo_path = "/media/clone"
solr_version = "solr-8.11.2"
zk_host = "localhost:9983"

try:
    upload_solr_config(github_repo_url, local_repo_path, solr_version, zk_host)
except FileNotFoundError as e:
    print(f"Error: {e}")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")




