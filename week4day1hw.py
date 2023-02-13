# Exercise #1
# Reverse the list below in-place using an in-place algorithm.
# Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
def reverse(a_list):
    left = 0
    right = len(a_list) - 1
    
    while left <= right:
        a_list[left], a_list[right] = a_list[right][::-1], a_list[left][::-1]
        left += 1
        right -= 1
    return a_list
output1 = reverse(words)    
print(f'\n{output1}')

# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
def word_count(string):
    word_lst = string.lower().split()
    word_lst.sort()
    word_dict = {}
    for word in word_lst:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    return word_dict

output2 = word_count(a_text)
print(f'\n{output2}')


# Exercise #3
# Write a program to implement a Linear Search Algorithm.
# Hint: Linear Searching will require searching a list for a given number.¶
# If number is not present return -1

nums_list = [10,23,45,70,11,15]
target = 70

def linear_search(a_list, target):
    for i in range(len(a_list)):
        if a_list[i] == target:
            return i
    return -1

output3 = linear_search(nums_list,target)

if output3 != -1:
    print(f'\n{target} found at index: {output3}\n')
else:
    print (f'\n{target} not found !!!\n')
