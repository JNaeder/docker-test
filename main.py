from fastapi import FastAPI
from database import Database

app = FastAPI()
db = Database()


@app.get("/")
def default():
    return {"message", "This is the default page."}


@app.get("/db/one/{table_name}")
async def get_db_data(table_name):
    output = db.select_all(table_name)
    return output


@app.post("/db/{table_name}")
async def write_to_db(table_name, name, age):
    return db.insert(["name", "age"], [name, age], table_name)


@app.get("/db/all")
async def get_all_data():
    query = "SELECT * FROM test_db.people JOIN test_db.pets ON owner_id = people.id"
    return db.execute(query)
