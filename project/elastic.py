from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = 'RRfdxagvI1HKL9l+5Pd1'
ELASTIC_FINGERPRINT = '34752822c2815921bc7f159894d82546ad4e076b0da60561a2269d018061f703'

elastic = Elasticsearch(
    hosts='https://localhost:9200',
    ssl_assert_fingerprint = ELASTIC_FINGERPRINT,
    basic_auth = ( 'elastic', ELASTIC_PASSWORD )
)

#print(es.info())
#print(elastic.indices.create(index='movies'))
#print(es.count(index='movies'))

#print(elastic.search(index="movies", query={"match_all": {}}))

#print(es.index(index='movies', document=movie_doc))

def search_by_title(title: str):
    return elastic.search(index='movies', query= {
        'match': {
            'title': title
        }
    })