from vector import Vector

class Sort:
    def heapsort(list_item):
        def swap(list_item, min, max ):
            tmp = list_item[min]
            list_item[min] = list_item[max]
            list_item[max] = tmp

        def moveDown(list_item, first, last ):
            largest = 2 * first + 1
            while largest <= last:
                # right child exists and is larger than left child
                if ( largest < last ) and ( list_item[largest] < list_item[largest + 1] ):
                  largest += 1
                # right child is larger than parent
                if list_item[largest] > list_item[first]:
                  swap( list_item, largest, first )
                  # move down to largest child
                  first = largest;
                  largest = 2 * first + 1
                else:
                  return # force exit
        # convert list_item to heap
        length = len( list_item ) - 1
        leastParent = int(length / 2)
        for i in range ( leastParent, -1, -1 ):
            moveDown( list_item, i, length )
        # flatten heap into sorted array
        for i in range ( length, 0, -1 ):
            if list_item[0] > list_item[i]:
                swap( list_item, 0, i )
                moveDown( list_item, 0, i - 1 )

    def quick_sort(self,vector, start, end):
        def partition(vector, start, end):
            pivot = vector[end]
            bottom = start -1
            top = end
            done = 0
            while not done:
                while not done:
                    bottom += 1

                    if bottom == top:
                        done = 1
                        break

                    if vector[bottom] > pivot:
                        vector[top] = vector[bottom]
                        break
                while not done:
                    top -= 1
                    if top == bottom:
                        done = 1
                        break

                    if vector[top]  < pivot:
                        vector[bottom] = vector[top]
                        break
            vector[top] = pivot
            return top
        if start < end:
            split = partition(vector, start, end)
            self.quick_sort(vector, start, split-1)
            self.quick_sort(vector, split+1, end)
        else:
            return

    def count_sort(self, nums, max_value):
        output = [0 for i in range(len(nums))]
        count = [0 for i in range(max_value+1)]

        for i in nums:
            count[i] += 1

        for i in range(max_value+1):
            count[i] += count[i-1]

        for i in range(len(nums)-1, -1, -1):
            output[count[nums[i]]-1] = nums[i]
            count[nums[i]] -= 1

        return output

    def radix_sort(self, random_list):
        len_random_list = len(random_list)
        modulus = 10
        div = 1
        while True:
            # empty array, [[] for i in range(10)]
            new_list = [[], [], [], [], [], [], [], [], [], []]
            for value in random_list:
                least_digit = value % modulus
                least_digit //= div
                new_list[least_digit].append(value)
            modulus = modulus * 10
            div = div * 10

            if len(new_list[0]) == len_random_list:
                return new_list[0]

            random_list = []
            rd_list_append = random_list.append
            for x in new_list:
                for y in x:
                    rd_list_append(y)

