#!/usr/bin/python

def bubblesort(numbers):
    for i in range(0, len(numbers)-1):
        for j in range(0, len(numbers) -1 -i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


numbers = [int(i) for i in input().split()]
print(bubblesort(numbers))
