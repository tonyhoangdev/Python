#!/usr/bin/python3
#
"""
    @author: MinhHT3
    @brief : Threading
"""

import threading
import time

exit_flag = 0

class MyThead(threading.Thread):
    def __init__(self, thread_id, name, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.delay, 5)
        print("Exiting " + self.name)
    
    
# Define a function for the thread
def print_time(thread_name, delay, counter):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1

# Create two threads as follows
thread1 = MyThead(1, "Thread-1", 1)
thread2 = MyThead(2, "Thread-2", 2)

# Start new threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
    