class SnapshotArray:

    def __init__(self, length: int):
        self.records = {i: [] for i in range(length)}
        self.temp_arr = [0] * length
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.temp_arr[index] = val

        if self.records[index] and self.records[index][-1][0] == self.snap_id:
            self.records[index][-1] = (self.snap_id, val)
        else:
            self.records[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1

        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        res = 0

        for snaps in self.records[index]:
            if snaps[0] <= snap_id:
                res = snaps[1]
            else:
                break
        return res


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)