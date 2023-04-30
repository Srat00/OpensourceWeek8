#셰이커 정렬 알고리즘 구현하기
from typing import MutableSequence

def shaker_sort(a: MutableSequence)->None:
    left=0
    right=len(a)-1
    last=right
    while left<right:
        for i in range(right,left,-1):
            if a[k-1] > a[k]:
                a[k-1],a[k]=a[k],a[k-1]
                last=k
        left=last

        for k in range(left,right):
            if a[k]>a[k+1]:
                a[k],a[k+1] = a[k+1],a[k]
                last=k
        right=last
        

