from typing import List
from ultralytics import YOLO
from ultralytics.engine.results import Results


class JointsDetector:

    def __init__(self, path_to_model):
        self.model = YOLO(path_to_model)

    def get_detection(self, image) -> Results:
        return self.model(image)

    def get_joint_coords(self, detection: Results, is_right: bool = True) -> List[float]:
        box_idx = 1 if is_right else 0
        bbox = detection[0].boxes[box_idx].xyxy.tolist()[0]
        return bbox
