#!/usr/bin/python3
#
"""
    @author: MinhHT3
    @brief : Synchronizing Threads 
"""

import threading
import time

threadLock = threading.Lock()
threads = []

class MyThead(threading.Thread):
    def __init__(self, thread_id, name, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay
    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        # Free lock to release next thread
        threadLock.release()
        # print("Exiting " + self.name)
    
    
# Define a function for the thread
def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1

# Create two threads as follows
thread1 = MyThead(1, "Thread-1", 1)
thread2 = MyThead(2, "Thread-2", 2)

# Start new threads
thread1.start()
thread2.start()

# Add threads in thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
    
print("Exiting Main Thread")
    