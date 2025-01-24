# Hangman in Python
import random
from word_dict_hangman import word_dict

def choose_word():
    word = random.choice(list(word_dict.keys()))
    info = word_dict[word]
    return word, info

def display_hint(hint, category):
    print(f"Chủ đề: {category}")
    print(f"Từ này có {len(hint)} kí tự: ")
    print(" ".join(hint))
    print()

def main():
    word, info = choose_word()
    category = info["category"]
    meaning = info["meaning"]
    hint = ["_"] * len(word)
    wrong_guesses = 0
    guessed = set()
    max_attempts = 6

    while wrong_guesses < max_attempts:
        display_hint(hint, category)
        guess = input("Dự đoán: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Vui lòng nhập một chữ cái!")
            continue

        if guess in guessed:
            print(f"Chữ '{guess}' đã được đoán trước đó!")
            continue

        guessed.add(guess)

        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Sai! Bạn còn {max_attempts - wrong_guesses} lượt đoán.")

        if "_" not in hint:
            print("Chúc mừng! Bạn đã đoán đúng từ:", word.upper())
            print(f"{word.capitalize()}: {meaning}")
            break
    else:
        print("Thua rồi! Kết quả là:", word.upper())
        print(f"{word.capitalize()}: {meaning}")

if __name__ == "__main__":
    main()