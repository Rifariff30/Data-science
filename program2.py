def count_word(text):
    words=text.split()
    return len(words)
user_input=input("enter a sentence or paragraph")
total_words=count_word(user_input)
print(f"total words: {total_words}")