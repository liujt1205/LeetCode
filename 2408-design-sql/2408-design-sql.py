class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        self.columns = {}
        self.rows = {}
        for i in range(len(names)):
            self.tables[names[i]] = {}
            self.columns[names[i]] = columns[i]
            self.rows[names[i]] = 1
        

    def insertRow(self, name: str, row: List[str]) -> None:
        self.tables[name][self.rows[name]] = row
        self.rows[name] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.tables[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId - 1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)