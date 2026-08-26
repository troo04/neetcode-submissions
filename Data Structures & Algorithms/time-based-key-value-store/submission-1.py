class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [(timestamp, value)]
        else:
            self.mapping[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.mapping:
            return ""
        
        arr = self.mapping[key]
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        
        if high == -1:
            return ""
        
        return arr[high][1]