from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import route_file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

app.include_router(route_file.router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

