import os
import CRUD as CRUD

if __name__ == '__main__':
    sistemOperasi = os.name
    
    match sistemOperasi:
        case 'nt': os.system('cls')
    
    print('Selamat Datang di Program')
    print('Database Lagu 🎼  ')
    print('=========================\n')

    #cek database
    CRUD.initConsole()

    while True:
        match sistemOperasi:
            case 'nt': os.system('cls')
            
        print('Selamat Datang di Program')
        print('Database Lagu 🎼')
        print('=========================\n')

        print(f'1. Read Data')
        print(f'2. Create Data')
        print(f'3. Update Data')
        print(f'4. Delete Data\n')

        userOption = input('Input Option: ')

        match userOption:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': CRUD.delete_console()
        

        isDone = input('Exit Program (y/n)? ')
        if isDone == 'y' or isDone == 'Y':
            break
    print('\nThank You 🌼')