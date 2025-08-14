import sys
import time

def parse_numbers(text: str):
    nums = []
    for token in text.replace("\n", " ").split(","):
        s = token.strip()
        if not s:
            continue
        try:
            nums.append(int(s))
        except ValueError:
            nums.append(float(s))
    return nums

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def main():
    if len(sys.argv) != 2:
        print("사용법: python Insertion.py data.txt")
        sys.exit(1)

    in_path = sys.argv[1]
    with open(in_path, "r", encoding="utf-8") as f:
        arr = parse_numbers(f.read())

    start = time.perf_counter()
    insertion_sort(arr) 
    elapsed_ms = (time.perf_counter() - start) * 1000.0

    print(", ".join(str(x) for x in arr))
    print(f"개수: {len(arr)}")
    print(f"정렬 시간: {elapsed_ms:.3f} ms")

if __name__ == "__main__":
    main()
