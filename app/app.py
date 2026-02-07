from fastapi import FastAPI, HTTPException

app = FastAPI()


text_post = {
    1: {"title": "New Post", "content": "Cool test post"},
    2: {"title": "Learning FastAPI", "content": "FastAPI is fast and easy to use"},
    3: {"title": "Python Tips", "content": "Use list comprehensions to write cleaner code"},
    4: {"title": "Backend Development", "content": "Building APIs is essential for modern apps"},
    5: {"title": "Testing APIs", "content": "Postman helps test endpoints easily"},
    6: {"title": "Async Programming", "content": "Async improves performance in web servers"},
    7: {"title": "Database Integration", "content": "SQLAlchemy works great with FastAPI"},
    8: {"title": "Authentication", "content": "JWT is commonly used for API security"},
    9: {"title": "Deployment", "content": "Docker helps deploy applications consistently"},
    10: {"title": "Code Organization", "content": "Keep your project structure clean and modular"}
}


@app.get("/post")
def get_all_posts(): 
    return text_post


@app.get("/post/{id}")
def get_post(id: int): 
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_post.get(id)