from FileClass import File


class Dir(File):
    def __init__(self, parentDir=None):
        self._fileList = []
        self._parentDir = parentDir

    def addFileToDir(self, file: File):
        self._fileList.append(file)

    @property
    def parentDir(self) -> str:
        return self._parentDir
