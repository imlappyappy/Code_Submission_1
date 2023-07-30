# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 20:53:55 2023

@author: Shailesh
"""

def modify_string(s):
    modified_chars = set()
    new_string=list(s)
    for i in range(0,len(new_string)):
        ascii_value = ord(new_string[i])
        # Check if the character is an alphabetical value
        if 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
            # Check if the ASCII value is even
            if ascii_value % 2 == 0 and (i+1) not in modified_chars and new_string[i+1].isalpha():
                next_char = chr((ascii_value % 7) + ord(s[i + 1]))
                #next_char = chr(ascii_value + (ascii_value % 7))
                new_string[i]= chr(ascii_value)
                new_string[i+1]=next_char
                modified_chars.add(i+1)
            # check for next- non alpha and even value
            elif ascii_value % 2 == 0 and (i+1) not in modified_chars:
                new_string[i]= chr(ascii_value)
                new_string[i+1]=chr(83)
                modified_chars.add(i+1)
            # Check if the ASCII value is odd
            elif ascii_value % 2 != 0 and i > 0 and (i - 1) not in modified_chars:
                prev_char = chr(ord(new_string[i - 1]) - (ascii_value % 5))
                #prev_char = chr(ascii_value - (ascii_value % 5))
                new_string[i-1]=prev_char
                new_string[i]=chr(ascii_value)
                modified_chars.add(i-1)
            else:
                new_string[i]=new_string[i]
        else:
            new_string[i]=chr(83)

    return ''.join(new_string)

### output print
s = "sHQen}"
result = modify_string(s)
print("Modified String:", result)
