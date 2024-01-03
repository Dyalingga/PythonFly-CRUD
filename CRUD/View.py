from . import Operasi

def read_console():
    data_file = Operasi.read()

    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'

    #header
    print('\n'+'='*100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    print('-'*100)
    
    #data
    for index,data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}', end='')

    #footer
    print('='*100+'\n')

def create_console():
    print('\n\n'+'='*100)
    print('Silahkan tambah data lagu 🎶\n')

    judul = input('Judul\t: ')
    penulis = input('Penulis\t: ')
    while True:
        try:
            tahun = int(input('Tahun\t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun harus 4 digit angka(yyyy)!')
        except:
            print('Tahun harus 4 digit angka(yyyy)!')
    
    Operasi.create(judul, penulis, tahun)
    print('\nBerikut data baru anda')
    read_console()

def update_console():
    read_console()
    while (True):
        no_buku = int(input('Pilih Nomor Lagu yang ingin diupdate: '))
        data_buku = Operasi.read(index=no_buku)
    
        if data_buku:
            break
        else:
            print('Nomor tidak valid, masukan lagi!')
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    judul = data_break[2]
    data_add = data_break[1]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        print('\n'+'='*100)
        print('Silahkan pilih data yang ingin diubah')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. Penulis\t: {penulis:.40}')
        print(f'3. Tahun\t: {tahun:4}')

        user_option = input('Pilih data [1,2,3]: ')
        print('\n'+'='*100)

        match user_option:
            case '1': judul = input('Masukkan Judul baru: ')
            case '2': penulis = input('Masukkan Penulis baru: ')
            case '3':
                while True:
                    try:
                        tahun = int(input('Tahun\t: '))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print('Tahun harus 4 digit angka(yyyy)!')
                    except:
                        print('Tahun harus 4 digit angka(yyyy)!')
            case _: print('Index tidak valid!')

        print('Data baru anda')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. Penulis\t: {penulis:.40}')
        print(f'3. Tahun\t: {tahun:4}')

        isDone = input('Apakah data sudah sesuai(y/n)? ')
        if isDone == 'y' or isDone == 'Y':
            break
    
    Operasi.update(no_buku,pk,data_add,judul,penulis,tahun)

def delete_console():
    read_console()
    while (True):
        no_buku = int(input('Pilih Nomor Lagu yang ingin dihapus: '))
        data_buku = Operasi.read(index=no_buku)
    
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            judul = data_break[2]
            data_add = data_break[1]
            penulis = data_break[3]
            tahun = data_break[4][:-1]
    
            print('\n'+'='*100)
            print('Data yang ingin anda hapus')
            print(f'1. Judul\t: {judul:.40}')
            print(f'2. Penulis\t: {penulis:.40}')
            print(f'3. Tahun\t: {tahun:4}')
            isDone = input('Apakah anda yakin(y/n)? ')
            if isDone == 'y' or isDone == 'Y':
                Operasi.delete(no_buku) 
                break
        else:
            print('Nomor tidak valid, masukan lagi!')
    
    print('Data berhasil dihapus')