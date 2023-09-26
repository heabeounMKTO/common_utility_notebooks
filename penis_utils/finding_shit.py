import os
import json
from pathlib import Path


class FilesFinder:
    def __init__(self, path):
        self.path = Path(path)

    def by_extension(self, extension, recursive: bool = False, fullpath: bool = True):
        """
        if recursive is true , searches folders and subfolders
        """
        file_list = []
        """
        recursive is a WIP
        """
        if recursive == True:
            for roots, dirs, files in os.walk(self.path):
                # print (roots, dirs, files)
                for file in files:
                    if file.endswith(extension):
                        if not fullpath:
                            file_list.append(files)
            return file_list
        else:
            for file in os.listdir(self.path):
                if file.endswith(extension):
                    if not fullpath:
                        file_list.append(file)
                    else:
                        file_list.append(os.path.join(self.path, file))
            return file_list


class LabelsLoader:
    def __init__(self, json_array):
        self.json_array = json_array
<<<<<<< HEAD

=======
    def get_img_with_label(self, label):
        '''
        will add **kwargs later.
        '''
        img_w_label = []
        for file in self.json_array:
            for shit in json.load(open(file))['shapes']:
                if shit['label'] == label:
                    img_w_label.append(file)
        return img_w_label, label
        
>>>>>>> 86c7e059b7de6526506be49e0836963af3e4410b
    def load_all_classes_from_array(self, to_dict=False):
        """
        loads all classes from json array
        """
        self.classes = []
        for file in self.json_array:
            for shit in json.load(open(file))["shapes"]:
                self.classes.append(shit["label"])
        self.classes = sorted(set(self.classes))
        if to_dict:
            c_dict = self.to_class_count_dict()
            return self.classes, c_dict
        else:
            return self.classes

    def to_class_count_dict(self):
        _cc = {}
        for i in self.classes:
            _cc[i] = 0
        return _cc
