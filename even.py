# In an even word, each letter occurs an even number of times.
# Write a function solution that, given a string S consisting of N characters, returns the minimum number of letters that must be deleted to obtain an even word.
# Examples:
# 1. Given S = "acbcbba", the function should return 1 (one letter b must be deleted).
# 2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted).
# 3. Given S = "aaaa", your function should return 0 (there is no need to delete any letters).
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [0..200,000];
# # string S is made only of lowercase letters (a−z) 

#SOLUTION
def min_deletions_to_even_word(s):
    
    from collections import Counter
    char_count = Counter(s)
    
    deletions = sum(count % 2 for count in char_count.values())
    
    return deletions

print(min_deletions_to_even_word("acbcbba"))
# print(min_deletions_to_even_word("axaxaxa"))
# print(min_deletions_to_even_word("aaaa"))