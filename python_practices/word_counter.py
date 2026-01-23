def word_counter(sentence):
    words = sentence.split()
    total_words = len(words)
    unique_words = len(set(words))
    return total_words, unique_words

text = input("Enter a sentence: ")

total, unique = word_counter(text)

print("Total words:", total)
print("Unique words:", unique)