# Strings in Python

## 1. Reverse a String
```python
def reverse_string(s):
    return s[::-1]

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
```

## 2. Check if a String is a Palindrome
```python
def is_palindrome(s):
    return s == s[::-1]

# Example usage
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

## 3. Find the First Non-Repeating Character
```python
def first_unique_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    return -1

# Example usage
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("aabb"))      # Output: -1
```

## 4. Count the Occurrences of a Character in a String
```python
def char_frequency(s, char):
    return s.count(char)

# Example usage
print(char_frequency("hello world", "o"))  # Output: 2
```

## 5. Check if Two Strings are Anagrams
```python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
```

## 6. Find the Longest Common Prefix
```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example usage
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Output: ""
```

