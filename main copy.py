from enum import Enum
from turtle import title
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None

@app.get("/")
async def root():
    return f"Hello World"

food_items = {
    'indian' : ['samosa', 'chat'],
    'american' : ['pizza', 'pasta']
}

valid_cusine = food_items.keys()

@app.get("/item/{cusine}")
async def root(cusine):
    if cusine not in valid_cusine:
        return "Cusine not found"
    else:
        return food_items.get(cusine)


class available_cus(str, Enum):
    indian = 'indian'
    american = 'american'

@app.get("/get_item/{cusine}")
async def root(cusine: available_cus):
    return food_items.get(cusine)

cupons = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_cup/{code}")
async def root(code: int):
    return cupons.get(code)


@app.get("/posts")
def get_posts():
    return {"data":"This is first post"}

# @app.post("/createposts")
# #payload is variable, take all field from body as dict
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new post":f"title {payload['title']} content: {payload['content']}"}
# #title str, content str, category,

##validation check
@app.post("/createposts")
def create_posts(new_post: Post):
    #print(new_post)
    print(new_post.rating)
    print(new_post.dict())
    return {"data":"new_post"}


