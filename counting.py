import cv2
import json
import os
from penis_utils import finding_shit as FS 
import pprint as pp
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class CountClasses:
    def __init__(self, path):
        self.path = path
    def count_classes(self):
        all_json = FS.FilesFinder(path=self.path).by_extension(".json")
        classes, dict_classes = FS.LabelsLoader(all_json).load_all_classes_from_array(to_dict=True)
        for _json in all_json:
            load_json = json.load(open(_json))
            for idx ,contents in enumerate(load_json['shapes']):
                _label = contents['label'] 
                dict_classes[_label] = dict_classes.get(_label, 0) + 1
        self.count_class = dict_classes
        return self.count_class 
    def draw_plot(self):
        x = list(self.count_class.keys())
        y = list(self.count_class.values()) 
        fig = plt.figure(figsize = (10,5))
        plt.bar(x , y,width= 0.2)   
        plt.xlabel("class_name")
        plt.ylabel("instance count")
        plt.title("class labels balance")        
        plt.show()