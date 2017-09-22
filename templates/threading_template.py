import threading
import os
import sys

# Threading events allow for a signal to be sent across several threads
thread_wrangler = threading.Event()

def thread_func():
    while not thread_wrangler.is_set():
        print "hello!"


def main():
    #Create a list of 10 threads, allows us to join on all threads
    threads = []
    for i in xrange(10):
        threads.append(threading.Thread(target=thread_func, args=(), name="thread%s" % i))
    # Start 10 threads
    for thread in threads:
        thread.start()
    # Join threads with error checking and to allow for non-blocking
    # interrupts across multiple threads in python.
    try:
        for thread in threads:
            while thread.is_alive():
                # Sends keyboard interrupt if threading event is set.
                # This ensures that anything proceeding in the function
                # is safe to execute.
                #if thread_wrangler.is_set():
                #    os.kill(os.getpid(), signal.SIGINT)
                thread.join(timeout=1)
    # FIXME: Add more interrupts/exceptions if needed
    except KeyboardInterrupt:
        thread_wrangler.set()
        try:
            # Wait for graceful shutdown of threads.
            for thread in threads:
                while thread.is_alive():
                    thread.join(timeout=1.0)
                #Cleanup has finished
        #Case that we want to exit immediately and not cleanup
        except (KeyboardInterrupt, Exception) as e:
            #Uses protected class to force exit of all threads
            os._exit(-1)
        sys.exit(-1)
    print "Everything has finished!"

if __name__ == "__main__":
    main()
