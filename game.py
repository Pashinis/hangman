import random

my_list = ["car", "dog", "sheep"]

def get_random_word_from_list(words_list: list) -> str:
    return random.choice(words_list)

def mask_word(word: str) -> str:
    return len(word) * "_"

zodis = mask_word("namas") 
print(zodis)
# def suma(skaicius1: int, skaicius2: int) -> int:
#     return skaicius1 + skaicius2

# rezultatas = suma(2, 2)

# print(rezultatas)
# word = get_random_word_from_list(my_list)

# print(word)

