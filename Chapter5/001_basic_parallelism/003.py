import time 
from multiprocessing import Process

def sleep_func():
    print('Sleeping for a 1 second')
    time.sleep(1)
    print('Done.')


if __name__ == '__main__':
    time_start = time.time()

    process_1 = Process(target=sleep_func)
    process_2 = Process(target=sleep_func)
    process_3 = Process(target=sleep_func)

    process_1.start()
    process_2.start()
    process_3.start()

    process_1.join()
    process_2.join()
    process_3.join()

    time_stop = time.time()
    print(f'Took {round(time_stop - time_start, 2)} seconds to execute!')
