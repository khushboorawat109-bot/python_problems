s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")