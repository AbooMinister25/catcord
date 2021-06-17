---
id: token
title: /token
sidebar_position: 1
---

# /token

## Description

- Method: POST
- Auth: None
- Args:
  + Username: string
  + Password: string

Registers a new user based off of the given username and password, and returns a token. This token is 
used to authenticate with the API.

## Code examples

### cURL

```sh
curl -X 'POST' \
  'http://localhost:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "this is a username",
  "password": "dis be a password"
}'
```

### Requests

```py
r = requests.post(
    "https://catcord.codes/token",
    json={
        "username": "a username",
        "password": "a password"
    }
)
```

