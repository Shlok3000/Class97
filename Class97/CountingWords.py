introString = input("Enter your String :")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount += 1
    if(i == " "):
        wordCount += 1

print("Number of Charcters in the string :", characterCount)
print("Number of Words in the string :", wordCount)