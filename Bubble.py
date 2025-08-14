import time
import sys

def bubble_sort_from_file(filename):
    def bubble_sort(arr):
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    with open(filename, "r") as f:
        data = list(map(int, f.read().strip().split(',')))

    print("정렬 전:", data)

    start_time = time.time()
    bubble_sort(data)
    end_time = time.time()

    print("정렬 후:", data)
    print("정렬 소요 시간: {:.6f}초".format(end_time - start_time))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "data.txt"
    bubble_sort_from_file(filename)