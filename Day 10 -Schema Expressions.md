* Searching, sampling and aggregating results from Solr.
        * search(test, q="*:*", fl="id,brand,model,storage,color,views,publish_date", sort="views asc", rows=100)

* Transforming result sets after they are retrieved from Solr.
        * select(
        *   search(test, q="*:*", fl="id,brand,model,storage,color,views,publish_date", rows=10),
        *   id as document_id,
        *   brand as manufacturer,
        *   color as product_color,
        *   views as view_count,
        * )

* Analyzing and modeling result sets using probability and statistics and machine learning libraries.
        * search(test, q="*:*", fl="views"),
        * stats(field="views", mean(views) as avg_views)

* Visualizing result sets, aggregations and statistical models of the data.


