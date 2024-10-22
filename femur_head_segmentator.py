from typing import List
from inference_sdk import InferenceHTTPClient
from femur_head_segmentator_types import FemurHeadResponse, Point


class FemurHeadSegmentator(InferenceHTTPClient):

    def __init__(self, url: str, key: str) -> None:
        super().__init__(url, key)

    def get_femur_head(self, path: str) -> FemurHeadResponse:
        return self.infer(path, model_id="femur-head-segmentation/2")
    
    @staticmethod
    def get_highest_y(data: FemurHeadResponse, is_right: bool = True) -> float:
        pred_idx = 0 if is_right else 1
        points: List[Point] = data['predictions'][pred_idx]['points']

        highest_y = float('inf')

        for point in points:
            if point['y'] < highest_y:
                highest_y = point['y']

        return highest_y