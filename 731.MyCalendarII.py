class MyCalendarTwo:

    def __init__(self):
        self.overlaps = list()
        self.calendar = list()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and s < end:
                return False
        for s, e in self.calendar:
            if start < e and s < end:  # overlap
                self.overlaps.append((max(s, start), min(e, end)))
        self.calendar.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
