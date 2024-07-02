from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database simulation
posts_db = []


# Pydantic model for a blog post
class BlogPost(BaseModel):
    id: int
    title: str
    content: str


# Root endpoint to serve the HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts_db})


# Create a new post
@app.post("/create_post")
async def create_post(title: str = Form(...), content: str = Form(...)):
    post_id = len(posts_db) + 1
    new_post = BlogPost(id=post_id, title=title, content=content)
    posts_db.append(new_post)
    return RedirectResponse(url="/", status_code=303)


# Update a post by ID
@app.post("/update_post/{post_id}")
async def update_post(post_id: int, title: str = Form(...), content: str = Form(...)):
    post_index = next((index for index, post in enumerate(posts_db) if post.id == post_id), None)
    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")
    posts_db[post_index] = BlogPost(id=post_id, title=title, content=content)
    return RedirectResponse(url="/", status_code=303)


# Delete a post by ID
@app.post("/delete_post/{post_id}")
async def delete_post(post_id: int):
    post_index = next((index for index, post in enumerate(posts_db) if post.id == post_id), None)
    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")
    posts_db.pop(post_index)
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
