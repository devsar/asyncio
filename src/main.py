from fastapi import FastAPI
import httpx

app = FastAPI()
anime_url = "https://ghibliapi.herokuapp.com/films"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fast/{anime_id}")
def get_info_fast(anime_id: str):
    url = f"{anime_url}/{anime_id}"
    response = httpx.get(url)
    return response.json()

