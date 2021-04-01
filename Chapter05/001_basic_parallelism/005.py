import time 
import concurrent.futures

def sleep_func(how_long: int):
    print(f'Sleeping for {how_long} seconds')
    time.sleep(how_long)
    return f'Finished sleeping for {how_long} seconds.'


if __name__ == '__main__':
    time_start = time.time()
    sleep_seconds = [1, 2, 3, 1, 2, 3]

    with concurrent.futures.ProcessPoolExecutor() as ppe:
        out = []
        for sleep_second in sleep_seconds:
            out.append(ppe.submit(sleep_func, sleep_second))

        for curr in concurrent.futures.as_completed(out):
            print(curr.result())

    time_stop = time.time()
    print(f'Took {round(time_stop - time_start, 2)} seconds to execute!')
