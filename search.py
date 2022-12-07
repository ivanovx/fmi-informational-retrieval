from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = 'UAabsRHsqcNsD9bOhfUf'
ELASTIC_FINGERPRINT = '1c48be5c1b0c444dcf55a337492ce18f7adced5c678c91f020da8461658c6217'

es = Elasticsearch(
    "https://localhost:9200",
    ssl_assert_fingerprint = ELASTIC_FINGERPRINT,
    basic_auth = (
        "elastic", 
        ELASTIC_PASSWORD
    )
)

print(es.info())