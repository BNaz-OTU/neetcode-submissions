import bisect

class FileSystem:

    def __init__(self):
        self.files = collections.defaultdict(str)
        self.direct = collections.defaultdict(list)

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            dirs = path.split("/")
            return [dirs[-1]]
        
        else:
            return self.direct[path]
        

    def mkdir(self, path: str) -> None:
        split_path = path.split("/")
        cummulation = ""

        for idx in range(1, len(split_path)):
            cur = "/".join(split_path[:idx]) or "/"

            if (cur not in self.direct or split_path[idx] not in self.direct[cur]):
                bisect.insort(self.direct[cur], split_path[idx])

        # for p in split_path:
        #     self.direct[cummulation].add(p)

        #     cummilation += ("/" + p)

        #     if cummulation not in self.direct:
        #         self.direct[cummulation] = set()
            



    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
        
        self.files[filePath] += content
        

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
