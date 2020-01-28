# RESTapi made with Flask, SQLalchemy, deployed on Heroku

## This on <a href = 'https://flask-rest-api-st.herokuapp.com/'>Heroku</a> ##
---
* ### Endpoints:
* #### /register(POST) example body: {"username": "admin", "password": "admin"}
* #### /auth(POST)     example body: {"username": "admin", "password": "admin"}, <span style="background-color: #FFFF00">returns you a JWT token</span>
* #### /items(GET)     empty body, requires JWT 
