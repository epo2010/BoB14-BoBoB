# merge.py
# 사용: python merge.py datat.txt (인자 없으면 data.txt를 읽음)
import sys
import re
import time
from pathlib import Path

MAX_ITEMS = 10_000

def read_numbers(path: Path) -> list[int]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    nums = [int(tok) for tok in re.findall(r"[-+]?\d+", text)]
    if not nums:
        raise ValueError("입력 파일에서 정수를 찾지 못했습니다.")
    return nums[:MAX_ITEMS]

def merge(left: list[int], right: list[int]) -> list[int]:
    i = j = 0
    out: list[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    if i < len(left):  out.extend(left[i:])
    if j < len(right): out.extend(right[j:])
    return out

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def main():
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data.txt")
    if not in_path.exists():
        raise FileNotFoundError(f"입력 파일이 없습니다: {in_path}")

    nums = read_numbers(in_path)

    # 정렬에 소요된 시간만 측정 (입력 파싱 시간 제외)
    t0 = time.perf_counter()
    sorted_nums = merge_sort(nums)
    t1 = time.perf_counter()

    # 정렬 결과 출력
    print(", ".join(map(str, sorted_nums)))

    # 시간 출력
    elapsed = t1 - t0
    print(f"\n정렬 시간: {elapsed*1000:.3f} ms ({elapsed:.6f} s), 항목 수: {len(nums)}")

if __name__ == "__main__":
    main()
