# Import the string utility module
import string_utils

# Sample text to test our functions
sample_text = "hello world from python"

print("--- Testing string_utils Module ---")
print(f"Original Text:  '{sample_text}'")

# 1. Test capitalize_words
capitalized = string_utils.capitalize_words(sample_text)
print(f"Capitalized:    '{capitalized}'")

# 2. Test reverse_string
reversed_txt = string_utils.reverse_string(sample_text)
print(f"Reversed:       '{reversed_txt}'")

# 3. Test word_count
count = string_utils.word_count(sample_text)
print(f"Word Count:     {count}")
