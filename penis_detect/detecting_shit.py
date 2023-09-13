import sys
sys.path.append('/.../penis_utils')
import cv2
import os 
import json
from pathlib import Path
from models.common import DetectMultiBackend
from utils.torch_utils import select_device
from penis_detect.detect import imageDetect

class ClassifyShit:
    def __init__(self, imagepath):
       # a path string
       self.image = cv2.imread(imagepath) 
   
    def variance_of_laplacian(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        return cv2.Laplacian(gray, cv2.CV_64F).var()
    
    def tell_if_blurry(self, threshold):
        fm = self.variance_of_laplacian()
        print(fm)
        if fm < threshold:
            return True 
        else: 
            return False
        
    def detect_from_model(self, model, device, conf):
        model = DetectMultiBackend(
            weights=model, device=device, dnn=False, data=None, fp16=True
        )
        detect_image = imageDetect(source=self.image, device=device, model=model, conf=conf)
        results = detect_image.detect()
        return results 
        
