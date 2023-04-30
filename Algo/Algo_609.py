from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            k = i - h
            tmp = a[i]
            while k >= 0 and a[k] > tmp:
                a[k + h] = a[k]
                k -= h
            a[k + h] = tmp
        h //= 3

if __name__ == '__main__':
    print('셸 정렬을 수행합니다(h * 3 + 1의 수열 사용).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)  # 배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')