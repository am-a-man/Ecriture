
import json
import time


class CustomError(Exception):
    pass


class fileWrite:
    def __init__(self, lock):
        print("fileWrite instance declared")
        with open("../server/api_outlet/content.json", "r", encoding="utf-8") as jsonData:
            try:
                self.data = json.load(jsonData)
            except:
                self.data = {}
            # jsonData.close()
        self.processLock = lock

    def write(self, dataFile):

        for i in dataFile.keys():
            self.data[i] = dataFile[i]

        jsonData = json.dumps(self.data, indent=4)

        self.processLock.acquire()
        with open("../server/api_outlet/content.json", "w", encoding="utf-8") as jsonDataFile:

            jsonDataFile.write(jsonData)
            jsonDataFile.close()
        print("data writing complete")
        self.processLock.release()


def colored(text, r=255, g=0, b=0):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
