from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from model import RecognitionModel

router = APIRouter(prefix="")
model = RecognitionModel()

vie2en_dict = {'can ho': 'apartment',
               'canh sat': 'police',
               'com': 'rice',
               'hoc sinh': 'student',
               'nguoi': 'human'}

vie2vie_dict = {'can ho': 'căn hộ',
               'canh sat': 'cảnh sát',
               'com': 'cơm',
               'hoc sinh': 'học sinh',
               'nguoi': 'người'}


def get_class_from_audio(file):
    file_location = f"{'tmp.wav'}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    class_name_vie = model.predict([file_location])[0]
    class_name_en = vie2en_dict[class_name_vie]
    class_name_en = vie2vie_dict[class_name_vie]
    print(class_name_vie)
    return class_name_en, class_name_vie

@router.post("/recognize")
def perform_recognition(file: UploadFile = File(...)):
    class_name_en, class_name_vie = get_class_from_audio(file)
    return {"filename": file.filename, "class_name_en": class_name_en, "class_name_vie": class_name_vie}

