# sample = 'a'
# sample_str = "abc"
# sample_str = """abc"""
# sample_str = "Today's weather is nice"
# 'Today's wather is nice' -> Invalid string

# sample_str = """Microsoft Windows [Version 10.0.22621.2861]
# (c) Microsoft Corporation. All rights reserved.

# Clink v1.6.0.3e6b73
# Copyright (c) 2012-2018 Martin Ridgers
# Portions Copyright (c) 2020-2023 Christopher Antos
# https://github.com/chrisant996/clink"""
# print(sample_str)

# Space will also be considered as a new line in the above example.

# sample_str = """Microsoft Windows [Version 10.0.22621.2861]\
# (c) Microsoft Corporation. All rights reserved.\
# Clink v1.6.0.3e6b73\
# Copyright (c) 2012-2018 Martin Ridgers\
# Portions Copyright (c) 2020-2023 Christopher Antos\
# https://github.com/chrisant996/clink"""
# print(sample_str)

# '\' is the escape character, python considers this a same line and print it is paragraph with spacing after each line. 

# sample_str = """Microsoft Windows [Version 10.0.22621.2861]
# (c) Microsoft Corporation. All rights reserved.

# Clink v1.6.0.3e6b73
# Copyright (c) 2012-2018 Martin Ridgers
# Portions Copyright (c) 2020-2023 Christopher Antos
# https://github.com/chrisant996/clink"""
# print(len(sample_str))

# print (sample_str.count("Microsoft"))

# Name = "Chikatla"
# print(Name.upper())
# print(Name.capitalize())

# ans = sample_str.split(" ") # splits based on space b/w words
# ans = sample_str.split("\n") # splits based on the lines
# ans = sample_str.splitlines()
# print (ans)

# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"

# Indexing
# print(sample_str[0])
# print(sample_str[2])
# print(sample_str[-1])
# print(sample_str[-2])

#Slicing
# print(sample_str[0:4]) # 0,1,2,3
# print(sample_str[:5]) # 0,1,2,3,4
# print(sample_str[20:]) # 20,21,....
# print(sample_str[-1:-4]) 
# (give empty string because it calculate from 0=start)
# start, start + 1, start + 2 ,.... end
# print(sample_str[-4:-1]) # -1,-2,-3,-4
# print(sample_str[:])
# print(sample_str[::2])
# start, start + 2, start + 4, .... end
# print(sample_str[1::2])

# [start:end:step]
# start: 0
# end: end
# step: -1
# print(sample_str[::-1]) # reverse the string

# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
# sample_str[0] = "P" # strings can't be changed
# print(sample_str)

# String Concatenation
# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
# sample_str = sample_str + " (c) Microsoft Corporation. All rights reserved."
# print(sample_str)

# sample_str = 'abc'
# sample_str *= 10
# print(sample_str)

# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
# sample_str = "{0}{1}".format(sample_str, "abc") # Microsoft Windows [Version 10.0.22621.2861]abc
# sample_str = "{1}{0}".format(sample_str, "abc") # gives abcMicrosoft Windows [Version 10.0.22621.2861]
# sample_str = 0, abc = 1
# print(sample_str)