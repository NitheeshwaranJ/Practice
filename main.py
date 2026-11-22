from fastapi import FastAPI, HTTPException
 
app = FastAPI()
 
# In-memory book data
books = [
    {
        "id": 101,
        "title": "Python Basics",
        "author": "John Smith",
        "category": "Programming",
        "price": 499.00
    },
    {
        "id": 102,
        "title": "Data Structures and Algorithms",
        "author": "Robert Martin",
        "category": "Computer Science",
        "price": 599.00
    }
]

@app.post("/books")
def create_book(book: dict):
  for boo in books:
    if boo["id"]==book["id"]:
      return {"message": "Book Id exist"}
    
  books.append(book)
  return {"message": "Book created"}

@app.get("/books")
def get_books():
  return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
  for book in books:
    if book["id"]==book_id:
      return book
  raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int,updated_data :dict):
  for book in books:
    if book["id"]==book_id:
      book["title"]=updated_data["title"]
      book["author"]=updated_data["author"]
      book["category"]=updated_data["category"]
      book["price"]=updated_data["price"]
      return {"message": "Book updated", "data": book}
  raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
  for book in books:
    if book["id"]==book_id:
      books.remove(book)
      return {"message": "Book deleted"}
  raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books_search_bycategory")
def searchby_category(category: str):
  result=[]
  for book in books:
    if book["category"].lower()==category.lower():
      result.append(book)
  
  return result
  

@app.get("/books_greater500")
def book_greaterthan500():
  result=[]
  for book in books:
    if book["price"]>500:
      result.append(book)
  return result

@app.get("/total_books")
def total_no_books():
  return len(books)

@app.get("/books_search_byauthor")
def searchby_author(author: str):
  result=[]
  for book in books:
    if book["author"].lower()==author.lower():
      result.append(book)
  return result
  
