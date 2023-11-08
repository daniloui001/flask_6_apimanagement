import requests 
import json 

# GET Request

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())

# GET Request with parameters

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts", 
    params={"userId": 1}
)
print(response.status_code)
print(response.json())

# Or can include the parameters in the URL

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts?userId=1"
)
print(response.status_code)
print(response.json())


# POST Request

response = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "foo", "body": "bar", "userId": 1})
print(response.status_code)
print(response.json())

# PUT Request

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json={"id": 1, "title": "foo", "body": "bar", "userId": 1})
print(response.status_code)
print(response.json())

# DELETE Request

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())


