#!/usr/bin/python
#Insertion sort is not a fast sorting algorithm.
#It uses nested loops to sort. This makes it slow.
#runs in O(n^2)

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i -1
        while numbers[j] > numbers[j+1] and j >= 0:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            j -=1
    return numbers

numbers = [int(i) for i in input().split()]
print(insertion_sort(numbers))
