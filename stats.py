def get_num_words(text):
    return len(text.split())    

def count_characters(text):
    char_count = {}
    
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    chars_list = []
    for char, num in num_chars_dict.items():
        chars_list.append({"char": char, "num": num})
    chars_list.sort(key=sort_on,  reverse=True)
    return chars_list