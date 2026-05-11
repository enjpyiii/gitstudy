# writer:enjoyiii
# 2025年05月26日16时40分23秒
# 1663472473@qq.com
def bresearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    arr = [12, 22, 32, 42, 52, 62, 72, 80, 85, 95]
    pos = bresearch(arr, 22)
    print(pos)
