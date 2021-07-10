
import json

class CustomError(Exception):
    pass

class fileWrite:
    def __init__(self, lock):
        print("fileWrite instance declared")
        with open("./api_outlet/content.json", "r",encoding="utf-8") as jsonData:
            self.data = json.load(jsonData)
            # jsonData.close()
        self.processLock = lock
      
    def write(self, dataFile):
        print("written data")
        for i in dataFile.keys():
            if i in self.data.keys():
                print("WARNING: this index already exists in the data, ignore if updating the present data")
            self.data[i] = dataFile[i]

        jsonData = json.dumps(self.data, indent=4)
        print("---------------------------------------------------------------------------------------> reached here")
        self.processLock.acquire()
        with open("./api_outlet/content.json", "w", encoding="utf-8") as jsonDataFile:
         
            jsonDataFile.write(jsonData)
            jsonDataFile.close()
        self.processLock.release()




def colored(text, r=255, g=0, b=0):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

