from fastapi import FastAPI

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# Định nghĩa một route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Định nghĩa một route với tham số
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
