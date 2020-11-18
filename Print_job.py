#Print_job.py Class declaration of print jobs and of queue class
class Print_job:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.pages = 0

    def set_start(self, start):
        self.start_time = int(start)

    def set_end(self, end):
        self.end_time = int(end)

    def get_time_print(self):
        if self.end_time == None:
            return 'False'
        else:
            return self.end_time - self.start_time

    def get_pages(self):
        return int(self.pages)

    def get_end_time(self):
        return self.end_time

    def get_start_time(self):
        return self.start_time

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)