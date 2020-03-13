from fastapi import FastAPI
import httpx

app = FastAPI()
anime_url = "https://ghibliapi.herokuapp.com/films"
anime_ids = [
    "2baf70d1-42bb-4437-b551-e5fed5a87abe",
    "12cfb892-aac0-4c5b-94af-521852e46d6a",
    "58611129-2dbc-4a81-a72f-77ddfc1b1b49",
    "ea660b10-85c4-4ae3-8a5f-41cea3648e3e",
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/slow/")
def get_info():
    data = []
    for url in [f"{anime_url}/{anime_id}" for anime_id in anime_ids]:
        response = httpx.get(url)
        data.append(response.json())
    return data


@app.get("/fast/")
async def get_info_fast():
    data = []
    async with httpx.AsyncClient() as client:
        for url in [f"{anime_url}/{anime_id}" for anime_id in anime_ids]:
            response = await client.get(url)
            data.append(response.json())
    return data

