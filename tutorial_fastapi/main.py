from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"data":item_id} #fetch item by id=id

@app.get("/items/{item_id}/name")
async def read_item_name(item_id:int):
    return {"data":{item_id:{"item_name"*3:"item_name"}}} #fetch item by id=id and return item_name