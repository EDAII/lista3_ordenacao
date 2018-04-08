<<<<<<< HEAD
"""Add main method.May use Python 3.6.5."""

from vector import Vector
from sort import Sort
import sys
import timeit
import matplotlib.pyplot as plt
import os
if __name__ == "__main__":
    while(1):
        os.system("clear")
        print("Choose an option:\n1: Quick_sort\n2: Heap_sort\n0: exit")
        try:
            ans = int(input())
        except:
            continue
        if ans == 1:
            ''' Graph of quick sort in time '''

            ''' Unsorted Vector '''
            list_result = []
            list_index = []
            Sort = Sort()
            for count in range(1, 1000, 10):
                vector = Vector.vector_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.quick_sort(vector, 0, len(vector)-1)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            f, axarr = plt.subplots(5, sharex=True)
            axarr[0].plot(list_index, list_result)
            axarr[0].set_title('Quick sort unsorted vector')
            ''' Sorted Vector '''
            list_result = []
            list_index = []
            for count in range(1, 1000, 10):
                vector = Vector.vector_sorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.quick_sort(vector, 0, len(vector)-1)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[1].plot(list_index, list_result)
            axarr[1].set_title("Quick sort in sorted vector")
            ''' Semi unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1, 1000, 10):
                vector = Vector.vector_semi_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.quick_sort(vector, 0, len(vector)-1)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[2].plot(list_index, list_result)
            axarr[2].set_title("Quick sort in semi unsorted vector")

            ''' Decreasing Vector '''
            list_result = []
            list_index = []
            for count in range(1, 1000, 10):
                vector = Vector.vector_decreasing(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.quick_sort(vector, 0, len(vector)-1)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[3].plot(list_index, list_result)
            axarr[3].set_title("Quick sort in decreasing vector")
            ''' Repeater Vector '''
            list_result = []
            list_index = []
            for count in range(1, 1000, 10):
                vector = Vector.vector_repeater(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.quick_sort(vector, 0, len(vector)-1)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[4].plot(list_index, list_result)
            axarr[4].set_title("Quick sort in repeater vector")

            f.subplots_adjust(hspace=0.6, right=0.5, left=0.2, top=1.2)
            plt.show()
        if ans == 2:
            ''' Graph of Heap sort in time '''

            ''' Unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1, 5000, 50):
                vector = Vector.vector_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.heapsort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            f, axarr = plt.subplots(5, sharex=True)
            axarr[0].plot(list_index, list_result)
            axarr[0].set_title('Heap sort unsorted vector')
            ''' Sorted Vector '''
            list_result = []
            list_index = []
            for count in range(1, 5000, 100):
                vector = Vector.vector_sorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.heapsort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[1].plot(list_index, list_result)
            axarr[1].set_title("Heap sort in sorted vector")
            ''' Semi unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1, 5000, 100):
                vector = Vector.vector_semi_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.heapsort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[2].plot(list_index, list_result)
            axarr[2].set_title("Heap sort in semi unsorted vector")

            ''' Decreasing Vector '''
            list_result = []
            list_index = []
            for count in range(1, 5000, 100):
                vector = Vector.vector_decreasing(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.heapsort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[3].plot(list_index, list_result)
            axarr[3].set_title("Heap sort in decreasing vector")
            ''' Repeater Vector '''
            list_result = []
            list_index = []
            for count in range(1, 5000, 100):
                vector = Vector.vector_repeater(count)
                list_index.append(count)
                tic = timeit.default_timer()
                Sort.heapsort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            axarr[4].plot(list_index, list_result)
            axarr[4].set_title("Heap sort in repeater vector")
            f.subplots_adjust(hspace=0.6, right=0.5, left=0.2, top=1.2)
            plt.show()

        if ans == 0:
            sys.exit()

        else:
            continue
