import time
from time import sleep
from threading import Thread



def job(job_num):
    print('Starting job %d now' % job_num)
    sleep(3)
    print('Job %d done' % job_num)

time_start = int(time.time())

# here we start two threads using the Thread class
# we initialize it and provide it wit the target function
# and the args arguments(a tuple)
thread1 = Thread(target=job, args=(1,))
thread2 = Thread(target=job, args=(2,))

# we start our threads, start() method
thread1.start()
thread2.start()

# we use the join() method to join the new threads to the main thread
# meaning this main thread has to wait for those two threads to complete
thread1.join()
thread2.join()


time_end = int(time.time())

print("Running jobs took %d secs" % (time_end - time_start))

