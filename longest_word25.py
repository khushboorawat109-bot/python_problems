

sentence = input()

words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)
print("Length:", len(longest))