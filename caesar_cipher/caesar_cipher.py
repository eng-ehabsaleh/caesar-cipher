import nltk
import re
from nltk.corpus import words, names
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()

upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


upper_list = list(upperCase)

lower_list = list(lowerCase)


def encrypt(plain_text, key):
    encrypted = ''
    for character in plain_text:
        if character not in upper_list and character not in lower_list:
            char = re.sub(r'[^A-Za-z]+', ' ', character)
            encrypted += char
        elif character in upper_list:
            char = (upper_list.index(character) + key) % 26
            encrypted += upper_list[char]
        else:
            char = (lower_list.index(character) + key) % 26
            encrypted += lower_list[char]
    return encrypted


def decrypt(plain_text, key):
    return encrypt(plain_text, -key)


def count_words(plain_text):
    candidate_words = plain_text.split()
    word_count = 0
    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+', '', candidate)
        if word.lower() in word_list or word in name_list:
            print("english word", word)
            word_count += 1
    return word_count


def crack(plain_text):
    text = ''
    for key in range(26):
        starter_word = decrypt(plain_text, key)
        word_count = count_words(starter_word)
        percentage = int(word_count / len(starter_word.split()) * 100)
        if percentage > 35:
            text += starter_word
            print(text, percentage)


if __name__ == "__main__":
    encrypted_smaple = encrypt('It was the best of times', 2)
    encrypted_smaple2 = encrypt('it was the worst of times', 2)
    decrypted_smaple = decrypt(encrypted_smaple, 2)
    decrypted_smaple2 = decrypt(encrypted_smaple, 2)
    decrypted_smaple_without_the_key = crack(encrypted_smaple)
    decrypted_smaple_without_the_key2 = crack(encrypted_smaple2)
    print(encrypted_smaple)
    print(decrypted_smaple)
    print(decrypted_smaple_without_the_key)
    print("############################################################")
    print(encrypted_smaple2)
    print(decrypted_smaple2)
    print(decrypted_smaple_without_the_key2)
