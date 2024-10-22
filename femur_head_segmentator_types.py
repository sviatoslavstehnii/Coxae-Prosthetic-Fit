from pydantic import BaseModel
from typing import List

class Point(BaseModel):
    x: float
    y: float

class Prediction(BaseModel):
    x: float
    y: float
    width: float
    height: float
    confidence: float
    class_name: str
    points: List[Point]
    class_id: int
    detection_id: str

class ImageInfo(BaseModel):
    width: int
    height: int

class FemurHeadResponse(BaseModel):
    inference_id: str
    time: float
    image: ImageInfo
    predictions: List[Prediction]
