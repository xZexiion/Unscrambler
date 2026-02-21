import random
with open("words.txt", "r") as file1, open("specials.txt", "r") as file2:
    words = [line.strip() for line in file1.readlines()]
    other_words = [line.strip() for line in file2.readlines()]
all_words = words + other_words
word = random.choice(all_words)
char_list = list(word)
random.shuffle(char_list)
scrambled = "".join(char_list)

attempts = 1
print(scrambled)

while attempts == 1:
    print(f"You only have one attempt. Choose wisely.")
    guess = input("Guess the word: ").strip().lower()
    if guess == word:
        print(f"Yes! The word was {word}!")
        break
    
    if len(guess) != len(word) or not guess.isalpha():
        print("You're not that stupid are you?")
        continue
    
    else:
        attempts -= 1
        print(f"Unlucky! The word was {word}!")