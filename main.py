from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import route_file

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(route_file.router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

