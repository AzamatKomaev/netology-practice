import time
import threading


result_1, result_2 = None, None


def f1(x):
    global result_1
    result_1 =  x**2 - x **2 + 4*x - 5*x + x + x


def f2(x) -> int:
    global result_2
    result_2 = x + x



def main():
    global result_1, result_2

    time_before = time.time()
    for i in range(10_000):
        t1 = threading.Thread(target=f1, args=[i])
        t2 = threading.Thread(target=f2, args=[i])
        t1.start()
        t2.start()
        # t1.join()
        # t2.join()
        res = result_1 + result_2  # formula 3
    print(f"10_000 iterations. Time: {time.time() - time_before}")

    time_before, result_1, result_2 = time.time(), None, None

    for i in range(100_000):
        t1 = threading.Thread(target=f1, args=[i])
        t2 = threading.Thread(target=f2, args=[i])
        t1.start()
        t2.start()
        # t1.join()
        # t2.join()
        res = result_1 + result_2  # formula 3

    print(f"100_000 iterations. Time: {time.time() - time_before}")


if __name__ == '__main__':
    main()
