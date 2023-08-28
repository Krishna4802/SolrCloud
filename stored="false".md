      * docker run -dit -p 7574:7574 -p 8983:8983 -p 8984:8984 --name solr ubuntu
      * docker exec -ti solr bash 
          1  apt update
          2  apt install default-jre
          3  apt-get install wget
          4  wget https://archive.apache.org/dist/lucene/solr/8.11.0/solr-8.11.0.tgz
          5  tar -xzf solr-8.11.0.tgz
          6  cd solr-8.11.0
          7  bin/solr -e cloud -force
      * bin/solr zk downconfig -n _default -d server/solr/configsets/nest -z 172.17.0.2:9983
      * Create the cluster as usual
      * Go the the file location - server/solr/configsets/test1/conf/
      * mv managed-schema schema.xml
      * Change the content of schema.xml and solrconfig.xml
      * bin/solr zk upconfig -n nest -d server/solr/configsets/nest/conf -z 172.17.0.2:9983
      * Create the collection and index the data to the collection
      
![image](https://github.com/Krishna4802/SolrCloud/assets/139359113/0a3e1788-6a3f-4407-a50c-db5b7bc34642)


### Query
        Fq : title:*
        Fl : *,[child]

# Nested Schema File with false columns


    <?xml version="1.0" encoding="UTF-8" ?>
    <schema name="default-config" version="1.6">
      <types>
        <fieldType name="string" class="solr.StrField" />
        <fieldType name="pint" class="solr.IntPointField" docValues="true" />
        <fieldType name="date" class="solr.TrieDateField" />
        <fieldType name="text_custom" class="solr.TextField" positionIncrementGap="100">
          <analyzer>
            <tokenizer class="solr.StandardTokenizerFactory"/>
            <filter class="solr.LowerCaseFilterFactory"/>
          </analyzer>
        </fieldType>
        <fieldType name="_version_" class="solr.LongPointField" docValues="true" />
        <fieldType name="_nest_path_" class="solr.NestPathField" />
        <fieldType name="nested" class="solr.NestPathField">
          <autoGenerateBlockJoinId>true</autoGenerateBlockJoinId>
          <childField>_childDocuments_</childField>
        </fieldType>
      </types>
      <fields>
        <field name="id" type="string" indexed="true" stored="true" required="true" />
        <field name="user" type="string" indexed="true" stored="true" />
        <field name="post" type="text_custom" indexed="true" stored="true" />
        <field name="likes_count" type="pint" indexed="true" stored="true" />
        <field name="_nest_path_" type="_nest_path_" />
        <field name="_nest_parent_" type="string" indexed="true" stored="true" />
        <field name="comments" type="_nest_path_" indexed="true" stored="true" multiValued="true" />
        <field name="comments.id" type="string" indexed="true" stored="true" />
        <field name="comments.user" type="string" indexed="true" stored="true" />
        <field name="comments.comment" type="text_custom" indexed="true" stored="true" />
        <field name="comments.timestamp" type="date" indexed="true" stored="true" />
        <field name="title" type="text_custom" indexed="true" stored="false" />
        <field name="content" type="text_custom" indexed="true" stored="false" />
        <field name="_version_" type="_version_" indexed="true" stored="true" />
        <field name="_root_" type="string" indexed="true" stored="false" />
        <dynamicField name="*_str" type="string" indexed="true" stored="true" />
        <dynamicField name="*_comments" type="nested" multiValued="true" indexed="true" stored="true" />
      </fields>
      <uniqueKey>id</uniqueKey>
      <!-- ... (other configurations) ... -->
    </schema>


## Updating Parts of Documents

For Normal Data

### add-distinct
Adds the specified values to a multiValued field, only if not already present. May be specified as a single value, or as a list.
 
    {
        "id": "8862",
      "color": {"add-distinct": "Black"},  
      }


### add
Adds the specified values to a multiValued field. May be specified as a single value, or as a list.

      {
        "id": "8862",
        "color": {"add": "Red"},
      }


### remove
Removes (all occurrences of) the specified values from a multiValued field. May be specified as a single value, or as a list.

     {
        "id": "8862",
        "color": {"remove": "Blue"},
      }


### removeregex
Removes all occurrences of the specified regex from a multiValued field. May be specified as a single value, or as a list.

    {
        "id": "8862",
        "color": {"removeregex": "^B.*"},
      }


### inc
Increments a numeric value by a specific amount. Must be specified as a single numeric value.
    
      {
        "id": "8862",
        "views”:{“inc”:  “20”}
    }


### set
Set or replace the field value(s) with the specified value(s), or remove the values if 'null' or empty list is specified as the new value.
May be specified as a single value, or as a list for multiValued fields.

      {
        "id": "8862",
        "storage": {"set": "128GB"},
        "color": {"set": "Blue"},
      }

  
    {
      "id": "8862",
      "views":{"set":  "0"}
    }
  


## For nested Datas - Updating Child Documents

        {
            "id": "1",
            "comments": [
              {
                "id": "5758",
                "comments.comment": { "set": "Updated comment for id 5758." }
              }
            ]
          }
    
    

## Using Curl Command
     curl -X POST 'http://localhost:8983/solr/part/update?commit=true' -H 'Content-Type: application/json' --data-binary '[
      {
        "id": "8862",
        "views":{"set":  "0"}
      }
    
    ]'





### Setting model and date as false and updating the data

    fq = model:*
    facet.field = model


<img width="1136" alt="Pasted Graphic 1" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/adc0e308-e15f-423b-9e64-4152fd8d5bfd">



