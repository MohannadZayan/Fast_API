from fastapi import FastAPI #?? Allows us to use the dependencies of FASTAPI in our code

app = FastAPI() #?? Creates an instance of the FastAPI class, which is used to define the API endpoints and handle requests.

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
# ?? async is used for asynchronous programming, allowing the function to run without blocking other operations.
@app.get ("/books") #?? Specifies the API endpoint that will call this function when accessed via a GET request.
async def read_all_books():
    return BOOKS #?? Returns a JSON response with the list of books when the endpoint is accessed.






## * ================== PATH PARAMETERS ================== * ##
# *Path parameters are used to capture values from the URL path and pass them as arguments to the function, think of them like a computer file system.

# * Let's take a look at @app.get("/books") for example, "/books" is a static path. Meaning it can't be changed. Which takes us to dynamic path parameters.

