import random
import time
import matplotlib.pyplot as plt
from bubble import bubble_sort
from heap import heap_sort
from insertion import insertion_sort
from merge import merge_sort
from quick import quick_sort
from selection import selection_sort

N = [100, 1000, 3000, 5000, 7000, 10000]
sort_functions = [bubble_sort,
                  heap_sort,
                  insertion_sort,
                  merge_sort,
                  quick_sort,
                  selection_sort]


def sort_test(sort_function, N):
    arr = list(random.randint(0, N) for _ in range(N))
    time_value = []
    for _ in range(10):
        start = time.time()
        sort_function(arr)
        end = time.time()
        time_value.append(end-start)
    return sum(time_value) / len(time_value)

time_data = [[sort_test(f, n) for n in N] for f in sort_functions]

for i in range(6):
    plt.axis([0,1,0,10000])
    plt.title(f'{sort_functions[i].__name__}_3.11')
    plt.plot(time_data[i], N)
    plt.savefig(f'{i+1}_3.11.png')
    plt.clf()
