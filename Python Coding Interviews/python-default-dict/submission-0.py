from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    char_dict = defaultdict(int)

    for char in s:
        char_dict[char] += 1
    
    return char_dict


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    num_dict = defaultdict(list)

    for idx in range(len(nums)):
        for jdx in range(1, len(nums[idx])):
            num_dict[nums[idx][0]].append(nums[idx][jdx])
    
    return num_dict

    pass


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
