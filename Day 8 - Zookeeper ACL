https://solr.apache.org/guide/8_11/zookeeper-access-control.html 
 
IMPLEMENT THE ZOOKEEPER ENABLED ACLS 

     docker pull zookeeper:latest 
 

First we need to create a Zookeeper Network 
 
      docker network create zookeeper-net 
 
Second we need to create a two containers 
           create a one container with Authentication to enable a acls 
 
docker run -d --name acl-zookeeper --network zookeeper-net -p 2181:2181 -p 2888:2888 -p 3888:3888 -e ZOO_MY_ID=1 -e 
 ZOO_SERVERS="server.1=0.0.0.0:2888:3888;2181" -e ZOO_AUTH_ENABLED=true -e ZOO_REQUIRE_CLIENT_AUTH_SCHEME=digest -e                                                                         
      ZOO_SUPERACL="super:shalu123:cdrwa" zookeeper 

        
execute a docker container 
 
docker exec -it acl-zookeeper bash 
                apt update 
                apt install nano 
 
 
enable a acls 
                  cd conf 
                  nano zoo.cfg 

 edit that zoo.cfg file with following lines 
          
 dataDir=/data 
dataLogDir=/datalog 
tickTime=2000 
initLimit=5 
syncLimit=2 
autopurge.snapRetainCount=3 
autopurge.purgeInterval=0 
maxClientCnxns=60 
standaloneEnabled=true 
admin.enableServer=true 
server.1=0.0.0.0:2888:3888;2181 
clientPort=2181 
authProvider.1=org.apache.zookeeper.server.auth.DigestAuthenticationProvider 
authProvider.2=org.apache.zookeeper.server.auth.IPAuthenticationProvider 
requireClientAuthScheme=sasl                                        
           

save the zoo.cfg file 
        
                        cd .. 
                        cd apache-zookeeper-3.8.2-bin/ 
                        cd bin 
 
we need to execute a zkClient shell 
                        
zkCli.sh -server acl-zookeeper:2181 
 

if we successfully executed zkclient  shell we need to  execute a  below codes 
 
                  addauth digest shalu:shalu123 
                  create /mydata "acl-protected-data" digest:shalu:shalu123:rwcda 
                  ls / 
 

create a onother container  without  Authentication to enable a acls 

docker run -d --name non-acl-zookeeper --network zookeeper-net -p 2182:2181 -p 2889:2888 -p 3889:3888 -e ZOO_MY_ID=2 -e ZOO_SERVERS="server.1=acl-zookeeper:2888:3888;2181" zookeeper\n 

 
 
    docker exec -it non-acl-zookeeper  bash 
    cd  conf/ 
    nano zoo.cfg 
    copy the zoo.cfg file system 
    server.1=non-acl-zookeeper:2888:3888 change this line …….. 
    zkCli.sh -server non-acl-zookeeper:2181\n 
 
 
echo "srvr" | nc localhost 2181 | grep "Mode" 
 
echo "srvr" | nc localhost 2182 | grep "Mode" 
