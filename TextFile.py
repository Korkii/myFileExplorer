import FileClass


class textFile(FileClass.File):
    def __init__(self, name: str, data: bytes):
        super().__init__(name, data)

    def readData(self):
        return self.data.decode("utf-8")


test = textFile("yes", "yes")
