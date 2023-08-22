# For Normal Data


## add-distinct
Adds the specified values to a multiValued field, only if not already present. May be specified as a single value, or as a list.
 
    {
        "id": "8862",
      "color": {"add-distinct": "Black"},  
      }

## add
Adds the specified values to a multiValued field. May be specified as a single value, or as a list.

      {
        "id": "8862",
        "color": {"add": "Red"},
      }


## remove
Removes (all occurrences of) the specified values from a multiValued field. May be specified as a single value, or as a list.
  
     {
        "id": "8862",
        "color": {"remove": "Blue"},
      }


## removeregex
Removes all occurrences of the specified regex from a multiValued field. May be specified as a single value, or as a list.

    {
        "id": "8862",
        "color": {"removeregex": "^B.*"},
      }


## inc
Increments a numeric value by a specific amount. Must be specified as a single numeric value.

      {
        "id": "8862",
        "views”:{“inc”:  “20”}
    }


## set
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



# For nested Datas - Updating Child Documents

    {
        "id": "1",
        "comments": [
        {
            "id": "5758",
            "comments.comment": { "set": "Updated comment for id 5758." }
          }
        ]
      }




# Using Curl Command

     curl -X POST 'http://localhost:8983/solr/part/update?commit=true' -H 'Content-Type: application/json' --data-binary '[
      {
        "id": "8862",
        "views":{"set":  "0"}
      }
    
    ]'



## Setting model and date as false and updating the data

* fq = model:*
* facet.field = model

<img width="1136" alt="Pasted Graphic 1" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/153a69f5-a056-4d8f-9945-4b12a6a1ed65">


