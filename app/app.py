from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()


text_posts = {
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
def get_all_posts(limit: int = None):
    if limit: 
        return list(text_posts.values())[:limit] 
    return text_posts



@app.get("/post/{id}")
def get_post(id: int): 
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/post")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post