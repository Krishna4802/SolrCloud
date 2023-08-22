# Request-Handler (qt) - 
    /select - default request handler and is used for executing search queries
    /update - sed for updating the index with new or deleting existing ones
    /admin - access to various administrative actions and operations for Solr, such as getting server status, reloading configurations, etc.


<img width="1161" alt="Screenshot 2023-08-03 at 2 25 39 PM" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/eb109709-6fcc-4643-911b-b0c3593edbb0">


  
* The "q" (query) field in the Schema section allows you to perform a test query to check how a specific field is analyzed and processed during the indexing and querying process.

  <img width="1134" alt="Screenshot 2023-08-03 at 2 38 43 PM" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/f023fc59-412a-4f03-8790-0285f8122695">


* brand:"Apple"

<img width="1118" alt="Screenshot 2023-08-03 at 2 41 46 PM" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/dae949c0-18a1-412a-8fc5-4e3388dadc0a">


* storage:"128GB"
  
  <img width="1124" alt="Pasted Graphic 2" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/64aa5a27-97be-4ff5-a2c4-67fb098b72a3">


* _version_: 1773196033807876096

<img width="1166" alt="Pasted Graphic 3" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/db3a9159-4fbf-4e82-949c-a27a4f05fa0b">



* The fq parameter defines a query that can be used to restrict the superset of documents that can be returned

        * views:[315 TO *]

<img width="1103" alt="Pasted Graphic 4" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/7c68bda3-0c9e-41da-a6d8-5db7d27aedf1">



#### SORT :-  The sort parameter arranges search results in either ascending (asc) or descending (desc) order. The parameter can be used with either numerical or alphabetical content. The directions can be entered in either all lowercase or all uppercase letters (i.e., both asc and ASC are accepted).


* Id desc - ordered by the descending order of id field

<img width="1296" alt="Pasted Graphic 6" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/9eb7cd76-18f6-4254-a23f-e00ca08ed743">



* id asc, views desc - Sorts by the contents of the id field in ascending order, then when multiple documents have the same value for the id field, those results are sorted in descending order by the contents of the views field.
  
<img width="1168" alt="Pasted Graphic 7" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/9baa79ac-8d98-4b9c-a936-f4f289930cf1">


* Fq : id:[4000 TO *]   &   sort : id asc - combination of field query and sort
  
<img width="1018" alt="Pasted Graphic 5" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/4ba54113-13ae-46d9-8cb2-4cb0268c869d">





* The start parameter specifies an offset into a query’s result set and instructs Solr to begin displaying results from this offset
0 is the default value of start

* The parameter specifies the maximum number of documents from the complete result set that Solr should return to the client at one time
10 is the default value


Here starting is 5 and Ending is 10 (we can give these numbers according to our needs)

<img width="1093" alt="Pasted Graphic 8" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/0a6e2f23-0bd8-47ad-ba53-017ea231bc28">



The fl parameter limits the information included in a query response to a specified list of fields

     * - Return all the stored fields in each document, as well as any docValues fields that have useDocValuesAsStored="true". This is the default value of the fl parameter

	   Id brand model - Only the id, brand and model field will be displayed

<img width="836" alt="Pasted Graphic 9" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/6035820a-23a9-40ae-810c-8ff0b398290e">



Brand - Fetches all the brand names only

<img width="894" alt="Pasted Graphic 10" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/0103fa51-0c2a-49bb-95d2-6c8f940d9033">



 the "df" (default field) parameter is used to specify the default field to be used for query parsing when no field is explicitly specified in the query itself

* Query: apple
* With "df" set to "brand": Solr will search for "apple" in the “brand” field by default.
  

<img width="1146" alt="Pasted Graphic 11" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/ea449679-5263-45ce-9cad-6cbdb4b67e37">



The wt(writer type) parameter selects the Response Writer that Solr should use to format the query’s response

* Json format

<img width="1082" alt="Pasted Graphic 12" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/64cdaf45-c429-4ff6-ab8f-f98b9148eda8">


* Xml format

<img width="1095" alt="Pasted Graphic 13" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/9b2bc659-5da0-4078-a7dc-7997618c85bc">


* Csv format

<img width="1138" alt="Pasted Graphic 14" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/afeeb518-2788-4215-b11a-85fc9103fbed">


* Indent is used for getting the output with space properties

The "debugQuery" parameter is included in a query, Solr will provide an extensive "explanation" section in the search results that helps you understand how the query was processed and how the scoring was calculated.

Here brand’s query debug details is fetched


<img width="1408" alt="Pasted Graphic 15" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/d6171943-a0dc-46ce-8f24-06024c4ed3ac">



"defType" (short for "default type") refers to the parameter used to specify the query parser that should be used to process the search query. The defType parameter tells Solr which query parser to use to interpret the query and generate the corresponding search results

There are 3 types : Lucene, dismax, edismax

* The Lucene query parser is the default query parser used in Solr. It is simple and straightforward
* The DisMax (Distributed Maximum) query parser is designed to handle user-entered search queries more effectively
* The EDisMax (Extended DisMax) query parser is an extension of the DisMax parser with additional capabilities

In Dismax
* q.alt: Specifies an alternate query to be used when the main query (q) returns no results.
* qf: Specifies the fields to be searched and their respective boosts when performing the main query (q).
* mm: Specifies the minimum number of "should" clauses that must be satisfied in a disjunctive query (e.g., "OR" query) for a document to be considered a match.
* pf: Specifies the fields and their boosts used to generate phrase queries for highlighting.
* ps: Specifies the size of the position window for phrase slop queries during parsing.
* qs: Specifies the size of the position window for proximity slop queries during parsing.
* tie: Sets the tiebreaker in DisMax queries, controlling the relative importance of query terms.
* bq: Specifies additional boosting queries that are used to influence the final score of documents in the search results.
* bf: Specifies function queries that are used to influence the final score of documents in the search results.



##### Facet - If you give the filed name to it , it will give you count of distinct data with the specified column


<img width="1150" alt="Pasted Graphic 18" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/eb01e5f5-daa2-4011-8d6a-587d5d049024">


<img width="906" alt="Pasted Graphic 16" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/f9c34ac7-9150-4ceb-a128-a7b71c84bbb7">



The parameters hl.fl, hl.simple.pre, and hl.simple.post are used in conjunction with the Highlighting component to enable and customise the highlighting of search results.

*  Brand is highlighted here 

<img width="1203" alt="Pasted Graphic" src="https://github.com/Krishna4802/SolrCloud/assets/139359113/67a0c26c-db71-4011-8cf5-12c8bbeb5fa8">


### Summary :-

##### Parameter	Description
    q     - This is the main query parameter of Apache Solr, documents are scored by their similarity to terms in this parameter.
    fq    - This parameter represents the filter query of Apache Solr the restricts the result set to documents matching this filter.
    start - The start parameter represents the starting offsets for a page results the default value of this parameter is 0.
    rows  - This parameter represents the number of the documents that are to be retrieved per page. The default value of this parameter is 10.
    sort  - This parameter specifies the list of fields, separated by commas, based on which the results of the query is to be sorted.
    fl    - This parameter specifies the list of the fields to return for each document in the result set.
    wt    - This parameter represents the type of the response writer we wanted to view the result.


