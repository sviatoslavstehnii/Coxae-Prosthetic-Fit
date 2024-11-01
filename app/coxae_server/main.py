from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()




@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    img_bytes = await file.read(file.size)
    return {"filename": file.filename}
