#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [n for n in num_list if n % 2 == 0]
    return num_list

def make_exclamation(sentence_list):
    exclamation_added = [n + "!" for n in sentence_list]
    return exclamation_added

print(make_exclamation(["Andreh", "Brian", "Andere"]))
