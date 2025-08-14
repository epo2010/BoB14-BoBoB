import re, sys, time

maxCount = 10000

def loadNumbers(path):
    numbers = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.split(':', 1)[1] if ':' in line else line
            for token in re.findall(r'-?\d+', s):
                numbers.append(int(token))
                if len(numbers) >= maxCount:
                    return numbers
    return numbers

def selectionSort(a):
    n = len(a)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if a[j] < a[minIndex]:
                minIndex = j
        if minIndex != i:
            a[i], a[minIndex] = a[minIndex], a[i]

def main():
    filePath = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    try:
        numbers = loadNumbers(filePath)
    except FileNotFoundError:
        sys.stderr.write(f"파일을 찾을 수 없습니다: {filePath}\n")
        sys.exit(1)
    if not numbers:
        sys.stderr.write("숫자를 읽지 못했습니다.\n")
        sys.exit(1)

    tStart = time.perf_counter()
    selectionSort(numbers)
    tEnd = time.perf_counter()

    print(", ".join(map(str, numbers)))
    print(f"소요 시간: {(tEnd - tStart) * 1000:.3f} ms")

if __name__ == "__main__":
    main()
