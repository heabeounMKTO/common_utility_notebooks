import os 
import json
from pathlib import Path


class FilesFinder:
    def __init__(self, path, extension):
        self.extension = extension
        self.path = Path(path)
    
    def by_extension(self, recursive: bool):
        '''
        if recursive is true , searches folders and subfolders
        '''
        self.file_list = []
        if recursive == True:
            for roots, dirs, files in os.walk(self.path):
                for files in os.walk: 
                    if files.endswith(tuple(self.extension)):
                        self.file_list.append(files)