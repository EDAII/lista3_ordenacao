import os
import sys
from random import randint

class Vector:

    def vector_unsorted(vector_len):
        vector_desorganized =[]
        for each in range(vector_len):
            vector_desorganized.append(randint(0,999))
        return vector_desorganized

    def vector_sorted(vector_len):
        vector_organized =[]
        for each in range(vector_len):
            vector_organized.append(each)
        return vector_organized

    def vector_semi_unsorted(vector_len):
        vector_semi_desorganized =[]
        for each in range(vector_len):
            if each <= int(vector_len/2.0):
                vector_semi_desorganized.append(each)
            else:
                vector_semi_desorganized.append(randint(0,999))
        return vector_semi_desorganized

    def vector_decreasing(vector_len):
        vector_decreased = []
        for each in range(vector_len,0,-1):
            vector_decreased.append(each)
        return vector_decreased
    def vector_repeater(vector_len):
        vector_repeate = []
        for each in range(vector_len):
            if each <= int(vector_len/2.0):
                vector_repeate.append(each)
            else:
                vector_repeate.append(randint(0,50))
        return vector_repeate
