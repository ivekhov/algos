from typing import List, Tuple


with open('input.txt',  'r' ) as f:
    time_ = int(f.readline().strip())
    n = f.readline().strip().split(' ')
    k = f.readline().strip()

    n = [int(item) for item in n]
    k = int(k)


def ma(n, k):
    res = []
    summary = sum(n[0:k])
    res.append(summary / k)

    for idx in range(k, len(n)):

        summary -= n[idx-k]

        summary += n[idx]
        res.append(summary / k)

    return res


res = ma(n, k)
res = [str(i) for i in res]


with open('output.txt', 'w') as f:
    f.write(' '.join(res))



def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

# arr, window_size = read_input()
# print(" ".join(map(str, moving_average(arr, window_size))))