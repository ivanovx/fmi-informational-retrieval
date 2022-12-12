from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = 'RRfdxagvI1HKL9l+5Pd1'
ELASTIC_FINGERPRINT = '34752822c2815921bc7f159894d82546ad4e076b0da60561a2269d018061f703'

es = Elasticsearch(
    "https://localhost:9200",
    ssl_assert_fingerprint = ELASTIC_FINGERPRINT,
    basic_auth = (
        "elastic", 
        ELASTIC_PASSWORD
    )
)

print(es.info())