# VectorAPI

/vectorapi/.env.example を .envに直してOPEN_API＿KEYを設定
### New database

```sh
docker compose up --build
```

### Adding a vector to a collection

1. Create a collection

```sh
curl -X POST "http://localhost:8889/v1/collections/create" \
    -H "Content-Type: application/json" \
    -d '{"collection_name":"my_collection", "dimension":384}'
```

2. Add a vector to the collection

```sh
curl -X POST "http://localhost:8889/v1/collections/my_collection/upsert" \
    -H "Content-Type: application/json" \
    -d '{"id":"abc2", "metadata":{"key":"value"}, "input":"ビーチを散歩するのが好きなんだ。"}'
```

### Vector search

```sh
curl -X POST "http://localhost:8889/v1/collections/my_collection/search" \
    -H "Content-Type: application/json" \
    -d '{"input":"ビーチで歩く"}'
```
