word = input("Enter the word: ")
second_word = []
second_word_check = ""
for i in word:
    second_word.insert(0,i)
for i in second_word:
    second_word_check += i
print(second_word_check)
if word == second_word_check:
    print("Its a pallendrome")
else:
    print("Its not a pallendrome")