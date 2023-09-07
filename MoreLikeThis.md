# MLT - More Like This


### Add the following in solrconfig.xml
    <requestHandler name="/mlt" class="solr.MoreLikeThisHandler">
       <lst name="defaults">
          <str name="mlt.fl">field_name</str> 
          <int name="mlt.mindf">1</int>       
          <int name="mlt.mintf">1</int>       
       </lst>
    </requestHandler>



## CURL Commands

    curl "http://localhost:8983/solr/mlt/mlt?mlt.fl=genre&mlt.interestingTerms=details&mlt.match.include=true&mlt.mindf=0&mlt.mintf=0&q=genre:"Fiction""
* mlt.fl=genre: Specifies that you want to perform the MLT query based on the "genre" field.
* mlt.interestingTerms=details: Indicates that you want to include interesting terms in the MoreLikeThis results.
* mlt.match.include=true: Specifies that the matching document (the document that triggered the MLT query) should be included in the results.
* mlt.mindf=0 and mlt.mintf=0: Set the minimum document frequency and minimum term frequency to 0, which means there are no strict frequency filters.
* q=genre:"Fiction": Specifies the query to find similar documents based on the genre "Fiction."

#### Output Explanation:

The output indicates that you have found documents similar to the input document(s) with the genre "Fiction." In this case, the input genre is "Fiction," and there are three documents with a similar genre:

* Document with id: 2, title "To Kill a Mockingbird," and author "Harper Lee."
* Document with id: 5, title "The Great Gatsby," and author "F. Scott Fitzgerald."
* Document with id: 3, title "1984," and author "George Orwell."

*** 

##### Command matches the Genre of **author:"Aldous Huxley"** to the entire Document in the collection

    curl "http://localhost:8983/solr/mlt/mlt?mlt.fl=genre&mlt.interestingTerms=details&mlt.match.include=true&mlt.mindf=0&mlt.mintf=0&q=author:"Aldous Huxley""

##### Command matches the author of **id:8** to the entire Document in the collection
   
    curl "http://localhost:8983/solr/mlt/mlt?mlt.fl=author&mlt.interestingTerms=details&mlt.match.include=true&q=id:8"

##### Command matches the genre of **book_title:"The Catcher in the Rye"** to the entire Document in the collection
 
    curl "http://localhost:8983/solr/mlt/mlt?mlt.fl=genre&mlt.interestingTerms=details&mlt.match.include=true&mlt.mindf=0&mlt.mintf=0&q=book_title:"The Catcher in the Rye""\n

##### Command matches the genre of **book_title:"The"** to the entire Document in the collection

    curl "http://localhost:8983/solr/mlt/mlt?mlt.fl=genre&mlt.interestingTerms=details&mlt.match.include=true&q=book_title:"The""\n



## Data I used 

    [
      {
        "id": "1",
        "book_title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "publication_year": 1951
      },
      {
        "id": "2",
        "book_title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "publication_year": 1960
      },
      {
        "id": "3",
        "book_title": "1984",
        "author": "George Orwell",
        "genre": "Fiction, Dystopian",
        "publication_year": 1949
      },
      {
        "id": "4",
        "book_title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Fiction, Romance",
        "publication_year": 1813
      },
      {
        "id": "5",
        "book_title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "publication_year": 1925
      },
      {
        "id": "6",
        "book_title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "publication_year": 1937
      },
      {
        "id": "7",
        "book_title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "publication_year": 1997
      },
      {
        "id": "8",
        "book_title": "Brave New World",
        "author": "Aldous Huxley",
        "genre": "Fiction, Dystopian",
        "publication_year": 1932
      },
      {
        "id": "9",
        "book_title": "The Lord of the Rings: The Fellowship of the Ring",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "publication_year": 1954
      },
      {
        "id": "10",
        "book_title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Fiction, Dystopian",
        "publication_year": 2008
      }
    ]
