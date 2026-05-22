import time
from time import sleep
from threading import Thread



def job(job_num):
    print('Starting job %d now' % job_num)
    sleep(3)
    print('Job %d done' % job_num)

time_start = int(time.time())

# we are creating 10 threads in these loop and initializing them, appending
# them to the llist and starting them
threads = []
for num in range(1, 11):
    thread = Thread(target=job, args=(num,))
    threads.append(thread)
    # we start our threads, start() method
    thread.start()
    
 # for every thread we appended into our threads array, joing them to the main thread
for thread in threads:
    thread.join() 

time_end = int(time.time())

print("Running jobs took %d secs" % (time_end - time_start))

