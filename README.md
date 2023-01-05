# Informational retrieval project

Project for FMI Information retrieval course

## TODO

* Finish web crawlers
* Store data from datasets in Elastic
* Search algo with Elastic
* Web client
    * React - using rest api
    * flask + js

## How run crawers

```
PS C:\Users\csynt\Desktop\fmi-informational-retrieval> cd .\imdb_spider\
PS C:\Users\csynt\Desktop\fmi-informational-retrieval\imdb_spider> scrapy list
imdb_spider
wiki_spider
PS C:\Users\csynt\Desktop\fmi-informational-retrieval\imdb_spider> scrapy crawl wiki_spider
....
....
....
PS C:\Users\csynt\Desktop\fmi-informational-retrieval\imdb_spider> scrapy crawl imdb_spider
```


* Save to json
```
scrapy crawl wiki_spider -o test.json
```

* Elastic as service
```
.\elasticsearch-service.bat install
```

## Docs

* [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
* [Elasticsearch Guide](https://www.elastic.co/guide/index.html)
* [Elasticsearch Install](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
* [Elasticsearch Python](https://elasticsearch-py.readthedocs.io/en/v8.5.3)

### Advanced docs

* [Search Rank](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-rank-eval.html)
* [Phrase searching](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query-phrase.html)
