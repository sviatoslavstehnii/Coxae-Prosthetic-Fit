from io import BytesIO
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    img_bytes = await file.read(file.size)
    base_image = Image.open(BytesIO(img_bytes))
    overlay_image = Image.open("overlay.jpg")

    base_image = base_image.convert("RGBA")
    overlay_image = overlay_image.convert("RGBA")

    overlay_image = overlay_image.resize((100, 100))
    position = (100, 100)
    base_image.paste(overlay_image, position, overlay_image) 

    img_byte_arr = BytesIO()
    base_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    headers = {"size": "50"}
    return StreamingResponse(img_byte_arr, media_type="image/png", headers=headers)
