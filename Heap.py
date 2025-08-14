import re, sys, time

maxCount = 10000  # set to None for no limit

def loadNumbers(path):
    numbers = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.split(':', 1)[1] if ':' in line else line
            for token in re.findall(r'-?\d+', s):
                numbers.append(int(token))
                if maxCount is not None and len(numbers) >= maxCount:
                    return numbers
    return numbers

def siftDown(a, root, end):
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and a[child] < a[child + 1]:
            child += 1
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
        else:
            break

def heapSort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        siftDown(a, i, n - 1)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        siftDown(a, 0, end - 1)

def main():
    filePath = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    try:
        numbers = loadNumbers(filePath)
    except FileNotFoundError:
        sys.stderr.write(f"Cannot open file: {filePath}\n")
        sys.exit(1)
    if not numbers:
        sys.stderr.write("No numbers were read.\n")
        sys.exit(1)

    tStart = time.perf_counter()
    heapSort(numbers)
    tEnd = time.perf_counter()

    print(", ".join(map(str, numbers)))
    print(f"소요 시간 : {(tEnd - tStart) * 1000:.3f} ms")

if __name__ == "__main__":
    main()
