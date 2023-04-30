from typing import MutableSequence

def selection_sort(a: MutableSequence)->None:
    n=len(a)
    for i in range(n-1):
        min=1
        for k in range(i+1,n):
            if a[k] < a[min]:
                min=k

        a[i],a[min]=a[min],a[i]
