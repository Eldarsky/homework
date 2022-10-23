import re

while True:

    print('1. Считать имена и фамилии,\n2. Считать все ел. почты,\n3. Считать название файлов,\n4. Считать цвета,\n'
          '5. Выход')

    search = int(input('Выберите пункт 1-5: '))

    file_path = 'MOCK_DATA.txt'
    surname_name_patronymic = 'names.txt'
    email = 'email.txt'
    file_extension = 'file_extension.txt'
    color_code = 'color_code.txt'

    file_reader = open(file_path, mode='r', encoding='Latin-1')
    surname_name = open(surname_name_patronymic, mode='w', encoding='Latin-1')
    m = open(email, mode='w', encoding='Latin-1')
    f = open(file_extension, mode='w', encoding='Latin-1')
    c = open(color_code, mode='w', encoding='Latin-1')
    my_text_file = file_reader.read()

    if search == 1:
        what_search = r"[A-Z][a-z_-]+[\s][de\sA-Z'\s]+[a-zA-Z]+"
        results = re.findall(what_search, my_text_file)
        print(results)

        for item in results:
            print(item)
            surname_name.write(item + '\n')

    if search == 2:
        what_search = r"(\b[\w\-]+[@][\w\-]+(\.[\w\-]+)+)"
        results = re.findall(what_search, my_text_file)
        print(results)

        for item in results:
            print(item)
            m.write(item[0] + '\n')

        print(f'Total results of file : {str(len(results))}')

    if search == 3:
        what_search = r'[A-Z\s]+[a-zA-Z]+[.][a-z\d]+'
        results = re.findall(what_search, my_text_file)
        print(results)

        for item in results:
            print(item)
            f.write(item + '\n')

        print(f'Total results of file : {str(len(results))}')

    if search == 4:
        what_search = r'#[\d[a-z]\w+'
        results = re.findall(what_search, my_text_file)
        print(results)

        for item in results:
            print(item)
            c.write(item + '\n')

        print(f'Total results of file : {str(len(results))}')

    if search == 5:
        print('Программа завершена')
        break

