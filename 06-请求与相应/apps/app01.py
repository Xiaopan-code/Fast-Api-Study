from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/user/{id}")
def get_user(id):
    print(id)
    return {
        "user_id": "id"
    }