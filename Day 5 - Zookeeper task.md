Day 5 - Zookeeper task

ChatGpt Link : https://chat.openai.com/share/1c0d0229-c255-4644-a85f-8a744932aad7

2888 - for leader election communication
3888 - for leader and follower communication

        - docker run -d            # Run the Docker container in detached mode (in the background).
        - --net zknet                # Connect the container to the Docker network named "zknet".
        - --name zk1                # Assign the name "zk1" to the running container.
        - -e ZOO_MY_ID=1      # Set the environment variable "ZOO_MY_ID" to 1. This identifies the node as having the ID of 1 within the ensemble.
        - -e ZOO_SERVERS="server.1=0.0.0.0:2888:3888 server.2=zk2:2888:3888 server.3=zk3:2888:3888”   # Set the environment variable "ZOO_SERVERS" to define the ZooKeeper servers in the ensemble.
        - zookeeper:3.6           # The Docker image to use, in this case, "zookeeper" version 3.6.


Commands used

        * docker network create zknet
        * docker run -d --net zknet --name zk1 -e ZOO_MY_ID=1 -e ZOO_SERVERS="server.1=0.0.0.0:2888:3888 server.2=zk2:2888:3888 server.3=zk3:2888:3888" zookeeper:3.6
        * docker run -d --net zknet --name zk2 -e ZOO_MY_ID=2 -e ZOO_SERVERS="server.1=zk1:2888:3888 server.2=0.0.0.0:2888:3888 server.3=zk3:2888:3888" zookeeper:3.6
        * docker run -d --net zknet --name zk3 -e ZOO_MY_ID=3 -e ZOO_SERVERS="server.1=zk1:2888:3888 server.2=zk2:2888:3888 server.3=0.0.0.0:2888:3888" zookeeper:3.6
        * docker logs zk1
        * docker logs zk2
        * docker logs zk3

# Based on the my_id In logs, we can find the leader and followers

    * 2023-08-04 11:02:29,556 [myid:1] - INFO  [QuorumPeer[myid=1](plain=disabled)(secure=disabled):Follower@75] - FOLLOWING - LEADER ELECTION TOOK - 9825 MS
    * 2023-08-04 11:02:19,306 [myid:2] - INFO  [QuorumPeer[myid=2](plain=disabled)(secure=disabled):Leader@581] - LEADING - LEADER ELECTION TOOK - 232 MS
    * 2023-08-04 11:02:35,125 [myid:3] - INFO  [QuorumPeer[myid=3](plain=disabled)(secure=disabled):Follower@75] - FOLLOWING - LEADER ELECTION TOOK - 15 MS

        * Therefore leader is zk2


# Killing Leader

        * docker stop zk2(leader)
        * Checking logs again 
                * docker logs zk1
                * docker logs zk3

# Logs:
    * 2023-08-04 11:02:35,125 [myid:3] - INFO  [QuorumPeer[myid=3](plain=disabled)(secure=disabled):Follower@75] - FOLLOWING - LEADER ELECTION TOOK - 15 MS
    * 2023-08-04 11:45:34,941 [myid:3] - INFO  [QuorumPeer[myid=3](plain=disabled)(secure=disabled):Leader@581] - LEADING - LEADER ELECTION TOOK - 211 MS

* Therefore leader is zk3

Note :- If you run only one ZooKeeper node, there is no leader or follower because a ZooKeeper ensemble requires a minimum of three nodes to establish a quorum and elect a leader. Without a quorum, ZooKeeper cannot perform leader election, and therefore, there won't be a leader.
