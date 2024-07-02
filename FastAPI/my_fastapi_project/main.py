from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


# Define a Pydantic model for the blog post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


# Sample data (for demonstration purposes)
my_list = [
    {"title": "Title of Post 1", "content": "Content of Post 1", "id": 1},
    {"title": "Title of Post 2", "content": "Content of Post 2", "id": 2}
]


# Get all posts
@app.get("/posts")
def get_all_posts():
    return {"data": my_list}


# Create a new post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    # Generate a random ID (for demonstration)
    post_id = randrange(1000)
    post_dict = post.dict()
    post_dict["id"] = post_id
    my_list.append(post_dict)
    return {"message": "Post created successfully", "post_id": post_id}


# Update an existing post
@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    # Update the post with the given ID
    for p in my_list:
        if p["id"] == post_id:
            p.update(post.dict())
            return {"message": f"Post with ID {post_id} updated successfully"}
    raise HTTPException(status_code=404, detail=f"Post with ID {post_id} not found")


# Delete a post
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    # Remove the post with the given ID
    for p in my_list:
        if p["id"] == post_id:
            my_list.remove(p)
            return {"message": f"Post with ID {post_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Post with ID {post_id} not found")
