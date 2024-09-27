from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.booking_count = SortedDict()
        self.max_overlapped_booking = 2

    def book(self, start: int, end: int) -> bool:
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1
        overlapped_booking = 0
        for count in self.booking_count.values():
            overlapped_booking += count
            if overlapped_booking > self.max_overlapped_booking:
                self.booking_count[start] -= 1
                self.booking_count[end] += 1

                if self.booking_count[start] == 0:
                    del self.booking_count[start]
                if self.booking_count[end] == 0:
                    del self.booking_count[end]
                    
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)