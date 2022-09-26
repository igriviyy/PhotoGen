# functions for face analyzing

from deepface import DeepFace
import json


def face_verify(img_1, img_2):  # comparing 1 to 1
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        # with open('result.json', 'w') as file:
        #     json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(result_dict)

        if result_dict.get('verified'):
            return "Passed! Let's go little soldier!!!"
        return 'Warning! Trespasser detected!!!'

    except Exception as _ex:
        return _ex


def face_recogn():  # comparing 1 with collection
    try:
        result = DeepFace.find(img_path='em1.jpg', db_path='Emilia')
        result = result.values.tolist()

        return result

    except Exception as _ex:
        return _ex


def face_analyze(img):  # get age, gender, race, emotion!!!
    try:
        result_dict = DeepFace.analyze(img_path=img, actions=['age', 'gender', 'race', 'emotion'])

        # with open('face_analyze.json', 'w') as file:
        #     json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(f'[+] Age: {result_dict.get("age")}')
        print(f'[+] Gender: {result_dict.get("gender")}')
        print('[+] Race:')

        for k, v in result_dict.get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print('[+] Emotions:')

        for k, v in result_dict.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

        # return result_dict

    except Exception as _ex:
        return _ex


def face_filter(img_path, age='1-99', gender='both'):
    try:
        result_dict = DeepFace.analyze(img_path, actions=['gender', 'age'])
        age_range = list(map(int, age.split('-')))
        if gender == 'both':
            if result_dict['age'] in range(age_range[0],  age_range[1] + 1):
                return True
        else:
            gender_dict = {'m': 'Man', 'f': 'Woman'}
            list_age_range = list(range(age_range[0],  age_range[1] + 1))
            if gender_dict[gender] == result_dict['gender'] and result_dict['age'] in list_age_range:
                return True
        return False

    except Exception as _ex:
        return _ex


def main():
    pass
    # print(face_verify(img_1='em1.jpg', img_2='em3.jpg'))
    # print(face_recogn())
    # face_analyze('em3.jpg')


if __name__ == '__main__':
    main()

