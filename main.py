import argparse
import os
from femur_head_segmentator import FemurHeadSegmentator
from femur_head_segmentator_types import FemurHeadResponse
from joints_detector import JointsDetector

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def main(parser: argparse.ArgumentParser):

    args = parser.parse_args()
    image_path = args.image_path
    model_path = args.model_path


    jd = JointsDetector(model_path)
    joints_res = jd.get_detection(image_path)

    seg = FemurHeadSegmentator("https://outline.roboflow.com", API_KEY)
    resp:FemurHeadResponse = seg.get_femur_head(image_path)

    print(f"Bounding box (xyxy) of joint: {jd.get_joint_coords(joints_res)}")
    print(f"Highest y coordinate of femur head: {seg.get_highest_y(resp, True)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Coxae Prosthetic Fit',
                    description='Find size of prothesis in coxae')
    parser.add_argument('image_path', type=str)
    parser.add_argument('model_path', type=str)

    
    main(parser)