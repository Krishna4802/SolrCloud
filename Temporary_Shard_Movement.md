* Copy the initial Shard folder to the other directory

* Index data to solr cloud collection

* Stop solr

* move the new Shard folder to the other directory

* create the simp link for the initial folder in the /solr-8.11.2/example/cloud/node2/solr/ with the same name.

        ln -s /solr_node_bkp/Shard_test_shard1_replica_n1/ Shard_test_shard1_replica_n1

* restart solr 

* check for the shards

* now stop solr 

* create the simp link for the new shard folder in the /solr-8.11.2/example/cloud/node2/solr/ with the same name.

* start solr again and check for the shards

* when i try to create the replica of the directory and start solr
 
* This may be because whenever we make changes in the data in the shard. its updated in segment_% file inside the Shard_test_shard1_replica_n1/data/index directory. It have data like
 
      ?�lsegments
      �'[�w�K�*��k2_0�'[�w�K�*��gLucene87�����������������'[�w�K�*��jcommitTimeMSec
      1722428280559commitCommandVer1806096956715433984�(��>Q�
* i think its the problem because of commitTimeMSec and commitCommandVer in this file.
 
* also whenever we update or insert data the segment_% file becoming like segment_2 -> segment_3 -> segment_4 .....
 
* for example : the above code is segment_2, Now i added data to collection then then segment_3 came like 
   
      ?�l^W^Hsegments^@^@^@
      ~]��^C~L��^G M^]@A�~P^A3^H^K^B^H^@^@^@^@^@^@^@^K^B^@^@^@^B^H^K^B^B_0^[�'[�w^T�K�*�^B�^]g^HLucene87^@^@^@^@^@^@^@^B^@^@^@A����������������^@^@^@^@^A~]��^C~L��^G M^]@A�~O^@^@^@^@^@^B_1~]��^C~L��^G M^]@@
      A�~L^HLucene87��������^@^@^@^@����������������^@^@^@^@^A~]��^C~L��^G M^]@A�~N^@^@^@^@^@^B^NcommitTimeMSec^M1722432509529^PcommitCommandVer^S1806101391111880704�(~S�^@^@^@^@^@^@^@^@I~A��
  
  
   
