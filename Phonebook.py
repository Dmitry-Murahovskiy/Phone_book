def work_with_Phonebook():
    choice = show_menu()
    Phone_book = read_txt('ZAPISULKA.txd')
    
    
    
    while choice == 8:
        if choice == 1:
            print_result(Phone_book)
        elif choice == 2:
            last_name = input('Заряжай фамилию')
            print(find_by_lastname(Phone_book, last_name))
        elif choice == 3:
            last_name = input('Заряжай фамилию')
            new_number = input('Введите новый номерок')
            print(change_number(Phone_book,last_name,new_number))
        elif choice == 4:
            last_name = input('Заряжай фамилию')
            print(delete_by_lastname(Phone_book, last_name))
        elif choice == 5:
            number = input('Введите номер')
            print(find_by_number(Phone_book, number))
        elif choice == 6:
            user_data = ('Ввудите новые данные: ')
            add_user(Phone_book, user_data)
            write_txt('ZAPISULKA.txd', Phone_book)
        elif choice == 7:
            src_file = input('Введите имя нового файла: ')
            dst_file = input('Ввудите имя целевого файла: ')
            line_num = int(input('Ввудите номер строки для копирования: '))
            copy_line(src_file, dst_file, line_num)
            print(f'Строчка {line_num} из файла {src_file} копирована в {dst_file}')
            
            
        choice = show_menu()
        if choice == 8:
            write_txt('ZAPISULKA.txd', Phone_book)
            break
        
        
def show_menu():
    print('Меню дня:')
    print('1. Показать телефоную книгу')
    print('2. Найти по фамилии')
    print('3. изменить номер')
    print('4. удалить по фамилии')
    print('5. Найти по номеру')
    print('6. добавить новый контакт')
    print('7. Копировать данные из одного файла в другой')
    print('8. выход')
    while True:
        try:
            choice = int(input('Выберите пункт меню'))
            if 1 <= choice <= 8:
                    return choice
            else:
                print('Неверный выбор. Ввудите другой пункт меню от 1 до 8.')
        except ValueError:
            print('Неверный ввод. Вудите цифру.')
            
            
def read_txt(filename):
    Phone_book = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(['Фамилия', 'Имя', 'Tелефон', 'описание'], line.strip().split(',')))
            Phone_book.append(record)
        return Phone_book
    
def write_txt(filename, Phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in Phone_book:
            phout.write(','.join(record.values()) + '\n')
            
def print_result(Phone_book):
    for record in Phone_book:
        print(record)
        
def find_by_lastname(Phone_book, last_name):
    result = [record for record in Phone_book if record['фамилия'] ==last_name]
    if result:
        return result
    else:
        return 'Абонент не найден'
    
def change_number(Phone_book, last_name, new_number):
    for record in Phone_book:
        if record['фамилия'] == last_name:
            record['телефон'] = new_number
            return 'номер изменен'
        return 'контанкт не найден'
    
def delete_by_lastname(Phone_book, lastname):
    Phone_book[:] = [record for record in Phone_book if record['фамилия']!= lastname]
    return 'контанкт удален'

def find_by_number(Phone_book, number):
    result = [record for record in Phone_book if record['телефон'] == number]
    if result:
        return result
    else:
        return 'абонент не найден'
    
def add_user(Phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    Phone_book.append(record)
    
def copy_line(src_file, dst_file, line_num):
    with open(src_file, 'r', encoding='utf-8') as src:
        lines = src.readlines()
        if line_num > 0 and line_num <= len(lines):
            line_to_copy = lines[line_num - 1]
            with open(dst_file, 'a', encoding='utf-8') as dst:
                dst.write(line_to_copy)
                
        else:
            print('не правилньный номер строки')
            
work_with_Phonebook()       
                
            
            
            