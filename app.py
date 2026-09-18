# Pseudo-code:
# 1. Ask the user to type a sentence.
# 2. Save that sentence in a variable.
# 3. Split the sentence into separate words.
# 4. Count how many words are in the list.
# 5. Print the result.


def count_words(sentence):
    words = sentence.split()
    return len(words)


user_sentence = input("I am a writer ")
word_count = count_words(user_sentence)
print(f"I am a writer {4} words.")


