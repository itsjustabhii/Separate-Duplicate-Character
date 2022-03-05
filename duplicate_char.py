from collections import Counter
from string import punctuation

#punctuation is a pre-initialized string used as string constant.

def display_characters(input, special):
    #Counter() is a container that stores elements
    count = Counter(input)
    count_dict = count.get  #Count() is a built-in function, returns the count of an element in a list
    distinct = set(input)   #Distinct obtains unique elements
    repeated = [i for i in list(distinct) if(count_dict(i) > 1)]    #Checks for repeated characters
    flattened_repeated = [item for sublist in repeated for item in repeated]
    non_repeated = [i for i in list(distinct) if(count_dict(i) == 1)]   #Checks for unique characters
    special_characters = list(special.intersection(distinct))   #Checks for special characters
    return (flattened_repeated, non_repeated, special_characters)


input = ("a", "b", "c", "a", "d", "$", "$", "@", "f")
special = set(punctuation)
(repeated_chars, unrepeated_chars,
 special_characters) = display_characters(input, special)

print(repeated_chars)
print(unrepeated_chars)
print(special_characters)
