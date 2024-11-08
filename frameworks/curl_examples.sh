curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{
           "id": 1,
           "name": "Test 2",
           "description": "This is a test item",
           "price": 2.88
         }'


curl -X PUT "http://localhost:8000/items/1" \
     -H "Content-Type: application/json" \
     -d '{
           "id": 1,
           "name": "Test 2",
           "description": "simple test item",
           "price": 2.88
         }'
