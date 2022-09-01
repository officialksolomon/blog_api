
# Simple Blog Webapp API

## This API can be used to create a fully functional Blog Webapp.  

The API is available at `http://127.0.0.1:8000/api/`.   

_Note_: To get this API to work on your local machine do the following:
- **Clone the Repository**
- **Install Requirements**
- **Execute CMD command python manage.py runserver.**  

I assume you have knowlegde of ***Python Django***.  


## **Endpoints** 
Work in progress... Adding enpoints....

### **List of books**

**GET `/posts`**   
Returns a list of books.

Optional query parameters:
- tag: (example tag: web, flutter, food, coding.....)  
_sample endpoint:_  `/posts/?tag=web`
### **Get a Single Post**

**GET `/posts/:postId`**   
Returns detailed information about a post.
