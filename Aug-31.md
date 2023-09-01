### Proximity

    title:"The"~2

<img width="1440" alt="image" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/1bddb357-b20d-4899-a5b0-194af63c7304">


### Highlight

    title:”The Catcher in the Rye” &hl=true&hl.fl=title

<img width="1440" alt="image" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/23dc9f8d-5f25-4332-8a92-6a4b4dba127c">


### Facet

    facet.field=category & facet.query=price:[5 TO 10]

<img width="957" alt="image" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/4f8f0734-db1e-434a-9358-18f8582da9c5">

#### Output:
<img width="1347" alt="image" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/5d177803-191b-45e1-94f9-7698d4970771">

***
    facet.field=author&facet.limit=5

<img width="951" alt="image" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/6ed4eac3-02f7-4531-af6b-42400bcee246">

#### output:
<img width="1171" alt="image" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/abd585c4-9098-430a-af2b-3deef69d9b99">

*** 

    facet.limit":"5",
        "q":"*:*",
        "facet.field":"author",
        "indent":"true",
        "q.op":"OR",
        "facet.mincount":"1",
        "facet":"true",
        "facet.sort":"count"
        
#### Output:

<img width="916" alt="image" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/cfab06db-df60-4845-9c00-673038230aa9">


### Json Facets

    curl http://localhost:8985/solr/test1/query -d '
    {
      "query": "*:*",
      "facet": {
        "categories" : {
          "type": "terms",
          "field": "cat",
          "limit": 3
        }
      }
    }'



Output :

      "response":{"numFound":49,"start":0,"maxScore":1.0,"numFoundExact":true,"docs":[
          {
            "id":"0553573403",
            "cat":["book"],
            "name":"A Game of Thrones",
            "price":7.99,
            "price_c":"7.99,USD",
            "inStock":true,
            "author":"George R.R. Martin",
            "author_s":"George R.R. Martin",
            "series_t":"A Song of Ice and Fire",
            "sequence_i":1,
            "genre_s":"fantasy",
            "_version_":1775815358787092480,
            "price_c____l_ns":799},
      "facets":{
        "count":49,
        "categories":{
          "buckets":[{
              "val":"electronics",
              "count":12},
            {
              "val":"book",
              "count":10},
            {
              "val":"currency",
              "count":4}]}}}


*** 


    curl http://localhost:8985/solr/test1/query -d '
    {
      "query": "*:*",
      "facet": {
        "high_popularity": {
          "type": "query",
          "q": "popularity:[8 TO 10]"
        }
      }
    }'


Output

    "response":{"numFound":49,"start":0,"maxScore":1.0,"numFoundExact":true,"docs":[
          {
            "id":"0553573403",
            "cat":["book"],
            "name":"A Game of Thrones",
            "price":7.99,
            "price_c":"7.99,USD",
            "inStock":true,
            "author":"George R.R. Martin",
            "author_s":"George R.R. Martin",
            "series_t":"A Song of Ice and Fire",
            "sequence_i":1,
            "genre_s":"fantasy",
            "_version_":1775815358787092480,
            "price_c____l_ns":799},
      "facets":{
        "count":49,
        "high_popularity":{
          "count":2}}}
