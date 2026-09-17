'''
words = input('Enter a Word: ')
vowels = 'aeiouAEIOU'
consonants_str = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
vowel_count = 0
consonant_count = 0

print("Vowels found:")
for i in words:
        if i in vowels:
              vowel_count += 1
              print(f'{i} is a vowel')

print("\nConsonants found:")
for i in words:
        if i in consonants_str:
              consonant_count += 1
              print(f'{i} is a consonant')

print(f"\nTotal vowels: {vowel_count}")
print(f"Total consonants: {consonant_count}")












words = input('Enter a Word: ')
vowels = 'aeiouAEIOU'
count = 0
for i in words:
        if i in vowels:
              count += 1
              print(f'{i} is a vowel')
print(count)


digits = (1,2,3,1,5,3)
empty_list = []
for i in digits:
    if digits.count(i) > 1 and i not in empty_list:
        empty_list.append(i)
        print(f'{i} is a duplicate')
'''


words = 'python is a programming language'
for i in words:
    if i == ' ':
        continue
    print(i)
