import time 

def sleep_func():
    print('Sleeping for a 1 second')
    time.sleep(1)
    print('Done.')


if __name__ == '__main__':
    time_start = time.time()

    # Run the function 5 times in loop
    for _ in range(5):
        sleep_func()

    time_stop = time.time()
    print(f'Took {round(time_stop - time_start, 2)} seconds to execute!')




