import time 
import concurrent.futures

def sleep_func():
    print('Sleeping for a 1 second')
    time.sleep(1)
    return 'Done.'


if __name__ == '__main__':
    time_start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as ppe:
        out = []
        for _ in range(5):
            out.append(ppe.submit(sleep_func))

        for curr in concurrent.futures.as_completed(out):
            print(curr.result())

    time_stop = time.time()
    print(f'Took {round(time_stop - time_start, 2)} seconds to execute!')
