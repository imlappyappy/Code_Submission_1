# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 19:55:50 2023

@author: Shailesh
"""

def shortest_substrings(s, x):
    substrings = []
    for i in range(len(s)):
        for j in range(i + x, len(s) + 1):
            if s[i] == s[j - 1] and j - i >= x:
                substrings.append(s[i:j])
                break
    shortest_length = min(len(substring) for substring in substrings)
    shortest_substrings = [substring for substring in substrings if len(substring) == shortest_length]
    return shortest_substrings

# Example usage:
s = "abccdbacca"
x1 = 3
print("x =", x1 ,shortest_substrings(s, x1))
x2 = 4  
print("x =", x2 ,shortest_substrings(s, x2))
x3 = 5
print("x =", x3 ,shortest_substrings(s, x3))
x4 = 6
print("x =", x4 ,shortest_substrings(s, x4))
