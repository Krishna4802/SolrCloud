# Solr with Zookeeper Ensemble Docker Compose file

    version: '3'
    services:
      zoo1:
        image: zookeeper:3.6.3
        container_name: zoo1
        ports:
          - "2181:2181"
        environment:
          ZOO_MY_ID: 1
          ZOO_SERVERS: server.1=zoo1:2888:3888;2181 server.2=zoo2:2888:3888;2181 server.3=zoo3:2888:3888;2181
          ZOO_4LW_COMMANDS_WHITELIST: "mntr,conf,ruok"
        restart: always
  
    zoo2:
      image: zookeeper:3.6.3
      container_name: zoo2
      ports:
        - "2182:2181"
      environment:
        ZOO_MY_ID: 2
        ZOO_SERVERS: server.1=zoo1:2888:3888;2181 server.2=zoo2:2888:3888;2181 server.3=zoo3:2888:3888;2181
        ZOO_4LW_COMMANDS_WHITELIST: "mntr,conf,ruok"
      depends_on:
        - zoo1
      restart: always
  
    zoo3:
      image: zookeeper:3.6.3
      container_name: zoo3
      ports:
        - "2183:2181"
      environment:
        ZOO_MY_ID: 3
        ZOO_SERVERS: server.1=zoo1:2888:3888;2181 server.2=zoo2:2888:3888;2181 server.3=zoo3:2888:3888;2181
        ZOO_4LW_COMMANDS_WHITELIST: "mntr,conf,ruok"
      depends_on:
        - zoo1
        - zoo2
      restart: always
  
    solr1:
      image: solr:8.11.0
      container_name: solr1
      ports:
        - "8983:8983"
      environment:
        ZK_HOST: "zoo1:2181,zoo2:2181,zoo3:2181"
        SOLR_CORE: "mycore1"
      depends_on:
        - zoo1
        - zoo2
        - zoo3
      restart: always
  
    solr2:
      image: solr:8.11.0
      container_name: solr2
      ports:
        - "8984:8983"
      environment:
        ZK_HOST: "zoo1:2181,zoo2:2181,zoo3:2181"
        SOLR_CORE: "mycore2"
      depends_on:
        - zoo1
        - zoo2
        - zoo3
      restart: always


