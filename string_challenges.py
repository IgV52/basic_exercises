# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
chars = ('а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я')
counter = 0
for char in word:
    if char.lower() in chars:
        counter += 1
    else:
        counter
print(counter)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
print(len(sentence))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for word in sentence:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
total_word = 0
averange_word = 0
total_char = 0
for word in sentence:
    total_char += len(word)
    total_word += 1
averange_word = total_char / total_word
print(averange_word)
