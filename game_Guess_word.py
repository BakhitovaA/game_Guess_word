import random

words_bank = (
    'автострада', 'бензин', 'инопланетянин', 'самолет',
    'библиотека', 'шайба', 'олимпиада', 'весна',
    'шахматы'
)

secret_word = random.choice(words_bank)

gamer_word = ['*'] * len(secret_word)
print(f'Загадано слово: {"".join(gamer_word)}. Длина: {len(gamer_word)} символов (используется русский алфавит)')
print("У вас есть 8 попыток, чтобы отгадать слово")

errors_cnt = 0
while True:
    letter = input('Введите одну букву: ').lower()
    if len(letter) != 1:
        print('Введено ноль или более одного символа. Не считается за попытку.')
        continue

    if letter in secret_word:
        print('Такая буква есть!')
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[idx] = letter
        if gamer_word.count('*') == 0:
            print('Поздравляю! Вы выиграли!')
            print(f'Было загадано слово: {secret_word.upper()}')
            break
    else:
        print('Нет такой буквы...')
        errors_cnt += 1
        print('Ошибок допущено:', errors_cnt)
        if errors_cnt == 8:
            print('К сожалению, вы проиграли...')
            print(f'Было загадано слово: {secret_word}')
            break
    print(''.join(gamer_word))
