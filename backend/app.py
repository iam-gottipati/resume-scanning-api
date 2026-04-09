from fastapi import FastAPI, UploadFile, File
import shutil
from parser import extract_text, score_resume

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_location)
    score = score_resume(text)

    return {"score": score}
