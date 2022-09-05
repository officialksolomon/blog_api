
# Simple Blog Webapp API

## This API can be used to create a fully functional Blog Webapp.  

The API is available at `http://127.0.0.1:8000/api/`.   

_Note_: To get this API to work on your local machine do the following:
- **Clone the Repository**
- **Install Requirements**
- **Execute CMD command python manage.py runserver.**  

I assume you have knowlegde of ***Python Django***.  

_Note_: This API requires authentication for its core features, register with the user registration endpoint.
## **Endpoints** 
Work in progress... Adding enpoints....
## ***Authentication***
### User Registration

**POST `/register`**   
Register, and returns a new user with authentication token.  
The request body needs to be in JSON format and include the following properties:

 - `username` - String - Required
 - `email` - String - Required
 - `password` - String - Required

Example
```
POST /register
{
  "username": "solo",
  "email": "solo@gmail.com"
  "password": "YOUR_PASSWORD"
}
```
### Get Authorization Token

**POST `/auth_token`**   
Returns user auth token.   
The request body needs to be in JSON format and include the following properties:

 - `username` - String - Required
 - `password` - String - Required

Example
```
POST /auth_token
{
  "username": "solo",
  "password": "YOUR_PASSWORD"
}
```
### List of books

**GET `/posts`**   
Returns a list of posts.

Optional query parameters:
- tag: (example tag: web, flutter, food, coding.....)  
_sample endpoint:_  `/posts/?tag=web`
### Get a Single Post

**GET `/posts/:postId`**   
Returns detailed information about a post.

### Submit a Post ###

POST `/post`

Allows you to submit a new post. Requires authentication.

The request body needs to be in JSON format and include the following properties:

 - `title` - String - Required
 - `content` - String - Required
 - `tags` - Optional: [] of JSON objects or single JSON object.

Example
```
POST /posts/
Authorization: Bearer <YOUR TOKEN>

{
        "title": "Is web3 really taking over?",
        "content": "Web3 in 2022 adn beyond.",
        "tags": [
            {
               
                "name": "crypto"
               
            },
            {
                
                "name": "web3"
               
            }
        ]
    }
```