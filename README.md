# RESTapi made with Flask, SQLalchemy, deployed on Heroku

## This on <a href = 'https://flask-rest-api-st.herokuapp.com/'>Heroku</a> ##
---
* ### Endpoints:
* #### /register(POST) example body: {"username": "admin", "password": "admin"}
* #### /auth(POST)     example body: {"username": "admin", "password": "admin"}, <mark>returns you a JWT token</mark>
* #### /items(GET)     empty body, requires JWT 
