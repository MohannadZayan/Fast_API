from fastapi import Body, FastAPI #?This will allow us to use the dependencies that we have installed in our environment
app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# * ============== PATH PARAMETERS ==============   (Part of the URL)

# * GET REQUESTS:

@app.get ("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")     #? {book_title} is a dynamic path parameter            #? This is the endpoint that we will be using to access our API
async def read_book(book_title: str):           #? We do not necessarily need to use async here as python adds it automatically, this is just for illustration.
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold(): #?casefold is essentially tolower like in c++
            return book

#? Dynamic parameters are defined in the path of the endpoint by the user himself, for example he might want to access the books of a specific author
# ! Static API's must be in front because fastapi looks from top to bottom to see what matches the url 

# *===============================================



# * ============== QUERY PARAMETERS ==============     (Sort and filter through data that is NOT marked by a path parameter)

@app.get("/books/") #! Notice the slash at the end of the endpoint, indicating that it is a query parameter
async def read_category_by_query(category: str): #? This is the endpoint that we will be using to access our API:
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold(): #? Checking if the category of the book matches the query parameter
            books_to_return.append(book)
    return books_to_return

# ! We can also use query and path parameters together!

# ! Let's say we want a function that searches by author AND category

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold(): #? Notice the backslash here, it is used to continue the same line of code on the next line
            books_to_return.append(book)

    return books_to_return

# * ===============================================




# * ============== BODY PARAMETERS ==============

# * POST REQUESTS:

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# * PUT REQUESTS:

@app.put("/books/update_book")
async def update_book (update_book = Body()):
    for i in range (len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book
            break


# * DELETE REQUESTS:

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break



# * ASSIGNMENT: Create a new API endpoint that can fetch all books from a specific author using path OR query parameters

@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return