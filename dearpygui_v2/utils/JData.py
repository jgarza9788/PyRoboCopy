
import os
import json5 as json

class JData():
    """
    loads and saves the data
    """
    def __init__(self,file=None,default=[]):
        self.default = default
        if file == None:
            directory = os.path.dirname(os.path.realpath(__file__))
            self.file = os.path.join(directory,'data.json')
        else:
            self.file = file
        self.data = self.load()

    def load(self):
        try:
            with open(self.file,'r') as file:
                return json.load(file)
        except:
            self.data = self.default
            self.save()
            return self.data

    def save(self):
        with open(self.file,'w') as file:
            file.write(json.dumps(self.data,indent=4))