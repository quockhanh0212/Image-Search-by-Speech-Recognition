from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from model import RecognitionModel

router = APIRouter(prefix="")
model = RecognitionModel()


def get_class_from_audio(file):
    file_location = f"{'tmp.wav'}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    class_name = model.predict([file_location])[0]
    return class_name

@router.post("/recognize")
def perform_recognition(file: UploadFile = File(...)):
    class_name = get_class_from_audio(file)
    return {"filename": file.filename, "class_name": class_name}
    