import threading

# Threading events allow for a signal to be sent across several threads
thread_wrangler = threading.Event()

def thread_func():
    while not thread_wrangler.is_set():
        print "hello!"


def main():
    # Start 10 threads
    for i in xrange(10):
        thread = threading.Thread(target=thread_func, args=(), name="thread%s" % i)
        thread.start()
    # Join threads with error checking and to allow for non-blocking
    # interrupts across multiple threads in python.
    try:
        while thread.is_alive():
            thread.join(timeout=1)
    # FIXME: Add more interrupts/exceptions if needed
    except KeyboardInterrupt:
        thread_wrangler.set()
if __name__ == "__main__":
    main()
