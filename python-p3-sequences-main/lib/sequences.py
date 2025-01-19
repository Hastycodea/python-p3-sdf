#!/usr/bin/env python3

def print_fibonacci(length):
    if(length == 1):
        print([0])
        return
    elif(length == 0):
        print([])
        return
    elif(length == 2):
        print([0, 1])
        return
    
    sequence = [0, 1]
    
    for i in range(2, length):
        sequence.append(sequence[-1] + sequence[-2])

    print(sequence)
    return



