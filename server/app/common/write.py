
import json
from multiprocessing import Lock

class fileWrite:
    def __init__(self):
        with open("./api_outlet/content.json", "r",encoding="utf-8") as jsonData:
            self.data = json.load(jsonData)

        self.processLock = Lock()
      
    def write(self, dataFile):
        for i in dataFile.keys():
            if i in self.data.keys():
                print("WARNING: this index already exists in the data, ignore if updating the present data")
            self.data[i] = dataFile[i]
        jsonData = json.dumps(self.data, indent=4)
        self.processLock.acquire()
        with open("./api_outlet/content.json", "w", encoding="utf-8") as jsonDataFile:
            jsonDataFile.write(jsonData)
        self.processLock.release()