from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


class Post(BaseModel):
    userId: int
    title: str
    body: str


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
    if response.status_code == 200:
        posts = response.json()
        return templates.TemplateResponse("create_post.html", {"request": request, "posts": posts, "message": None})
    raise HTTPException(status_code=response.status_code, detail="Error fetching posts")


@app.post("/create-post", response_class=HTMLResponse)
async def create_post(request: Request, userId: int = Form(...), title: str = Form(...), body: str = Form(...)):
    post = Post(userId=userId, title=title, body=body)
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=post.dict())
    if response.status_code == 201:
        return RedirectResponse("/", status_code=303)
    else:
        message = "Error creating post: " + response.text
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_URL)
        if response.status_code == 200:
            posts = response.json()
            return templates.TemplateResponse("create_post.html",
                                              {"request": request, "posts": posts, "message": message})
        raise HTTPException(status_code=response.status_code, detail="Error fetching posts")


@app.get("/posts", response_class=HTMLResponse)
async def get_posts(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
    if response.status_code == 200:
        posts = response.json()
        return templates.TemplateResponse("posts.html", {"request": request, "posts": posts})
    raise HTTPException(status_code=response.status_code, detail="Error fetching posts")
