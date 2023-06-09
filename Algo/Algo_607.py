from typing import MutableSequence

def insertion_sort(a: MutableSequence)->None:
    n=len(a)
    for i in range(1,n):
        k=i
        tmp=a[i]
        while k>0 and a[k-1]>tmp:
            a[k]=a[k-1]
            k-=1
        a[k]=tmp

if __name__== '__main__':
    print("단순 삽입 정렬을 수행합니다.")
    num=int(input('원소 수를 입력하세요.: '))
    x=[None]*num

    for i in range(num):
        x[i]=int(input(f'x[{i}] : '))


    insertion_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
        
