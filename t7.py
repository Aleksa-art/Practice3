vowels = ['a', 'e', 'i', 'y', 'o', 'u', 'A', 'E', 'I', 'Y', 'O', 'U']
consonants = ['B', 'C', 'D', 'F', 'G', 'H','J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

print("Only in English!")

word = input()
countVowels = 0
countConsonants = 0

for i in range(len(word)):
    if word[i] in vowels:
        countVowels += 1
    elif word[i] in consonants:
        countConsonants += 1
    else:
        continue
    
print(f"Vowels: {countVowels}, consonants: {countConsonants}")
