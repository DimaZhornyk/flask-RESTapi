# RESTapi made with Flask, SQLalchemy, deployed on Heroku

## This on <a href = 'https://flask-rest-api-st.herokuapp.com/'>Heroku</a> ##
---
### Endpoints:
* #### /register(POST)      example body: {"username": "admin", "password": "admin"}
* #### /auth(POST)          example body: {"username": "admin", "password": "admin"}, returns you a JWT token
* #### /items(GET)          empty body, :exclamation: requires JWT
* #### /item/<name>(GET)    empty body, :exclamation: requires JWT
* #### /item/<name>(POST)   example body: {"price":44.99, "store_id":1}, :exclamation: requires JWT
* #### /item/<name>(PUT)    example body: {"price":4.99, "store_id":2}, :exclamation: requires JWT
* #### /item/<name>(DELETE) empty body, :exclamation: requires JWT  
* #### /stores(GET)         empty body, :exclamation: requires JWT
* #### /store/<name>(GET)   empty body, :exclamation: requires JWT 
* #### /store/<name>(POST)  empty body, :exclamation: requires JWT  
