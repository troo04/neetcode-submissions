class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        # print(self.calendar, startTime)
        if not self.calendar:
            self.calendar.append((startTime, endTime))
            return True
        else:
            low, high = 0, len(self.calendar) - 1

            while low <= high:
                mid = (low + high) // 2

                if not (endTime <= self.calendar[mid][0] or self.calendar[mid][1] <= startTime):
                    return False
                elif startTime >= self.calendar[mid][1]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            self.calendar.insert(low, (startTime, endTime))
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)