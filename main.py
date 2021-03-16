from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import uvicorn


app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # onli get 10 published blogs ?limit=10&published=true
    # return published
    if published:
        return {'data': f'{limit} publishedblogs from de database'}
    else:
        return {'data': f'{limit} blogs from de database'}


@app.get('/blog/unpublished')
def unpublished():
    # fetch blog with id = id
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/coments')
def comments(id, limit=10):
    # fetch comments of blopg with id = id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    # return request
    return {'data': f"Blog is created as {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
