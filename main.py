from face_analyzer import face_filter
import requests
import sys
import os
import time
import re


def out_red(text):
    print("\033[31m{}\033[0m".format(text))


def quantity_input_verify():
    while True:
        try:
            quantity = int(input("How many photos do you need?\n"))
            if quantity <= 0:
                out_red('The number of photos should be more than zero!')
            else:
                return quantity
        except ValueError:
            out_red('You should enter a number!')


def gender_input_verify():
    while True:
        gender = input("Choose gender: M for male, F for female or press ENTER to skip...\n").lower()
        if gender == '':
            gender = 'both'
            return gender
        if gender not in ['m', 'f']:
            out_red('Invalid input!')
        else:
            return gender


def age_input_verify():
    while True:
        age = input("Choose age interval from 1 to 99 (for example, 5-15) or press ENTER to skip...\n")
        if age == '':
            age = '1-99'
            return age
        if not re.fullmatch(r'[1-9]\d-[1-9]\d', age) or int(age.split('-')[0]) > int(age.split('-')[1]):
            out_red("Chosen interval should be in format 'number1-number2', where 'number1' < 'number2' and both in [1; 99]")
        else:
            return age


def collect_photos():
    url = 'https://thispersondoesnotexist.com/image'

    quantity = quantity_input_verify()
    gender = gender_input_verify()
    age = age_input_verify()

    print('Attention! You may not get exactly what you need due to inaccuracy of calculations.')
    time.sleep(1)
    print()
    print('Downloading photos...')

    sys.stderr = open(os.devnull, 'w')

    count = 1

    while count <= quantity:
        time.sleep(1)

        img = requests.get(url)
        name = 'photos/photo' + str(count) + '.jpg'

        with open(name, 'wb') as file:
            file.write(img.content)

        if face_filter(name, gender=gender, age=age):
            # print(face_filter(name, gender=gender, age=age))
            print('\033[32mSUCCESS!\033[0m')
            count += 1
        else:
            os.remove(name)


def main():
    collect_photos()


if __name__ == '__main__':
    main()
