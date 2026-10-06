import pwinput

#Tuple
cuaca_sejuk = (23, 24, 25)
cuaca_hangat = (26, 27, 28, 29)
cuaca_panas = (30, 31, 32, 33, 34)
cuaca_terik = (35, 36, 37, 38, 39, 40)

#Dictionary
data_cuaca = {
    "Cuaca sejuk": cuaca_sejuk,
    "Cuaca hangat": cuaca_hangat,
    "Cuaca panas": cuaca_panas,
    "Cuaca terik": cuaca_terik
}

#List
semua_suhu = []
cuaca = []
hapus_suhu = []

print("Sistem Pengelolaan data cuaca")
print("Silahkan login")
role = input("Anda sebagai? (Admin/User): ")

def login():
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    if username == "admin" and password == "admin123":
        print("Login berhasil")
        return True
    else:
        print("Login gagal!!!!")
        return False

def login2():
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ") 

    if username == "user" and password == "user456":
        print("Login berhasil")
        return True 
    else:
        print("Login gagal!!!!")
        return False


if login():
        while True:
            print("Menu untuk admin:")
            print("1. Memasukkan suhu")
            print("2. Menghapus suhu")
            print("3. Menambahkan suhu baru")
            print("4. Keluar")

            pilihan = input("Anda adalah admin, silahkan pilih menu: ")
            
            if pilihan == '1':

                while True: 
                    input_admin = input("Masukkan data suhu (°C) atau ketik 'selesai' untuk mengakhiri: ")

                    if input_admin == 'selesai':
                        print("Input suhu selesai.")
                        break

                    suhu_masuk = int(input_admin)

                    if suhu_masuk < 23:
                        print ("Cuaca dingin")
                        semua_suhu.append(int(suhu_masuk))
                        cuaca.append("Cuaca dingin")
                    elif suhu_masuk in cuaca_sejuk:
                        print ("Cuaca sejuk")
                        semua_suhu.append(int(suhu_masuk))
                        cuaca.append("Cuaca sejuk")
                    elif suhu_masuk in cuaca_hangat:
                        print ("Cuaca hangat")
                        semua_suhu.append(int(suhu_masuk))
                        cuaca.append("Cuaca hangat")
                    elif suhu_masuk in cuaca_panas:
                        print ("Cuaca panas")
                        semua_suhu.append(int(suhu_masuk))
                        cuaca.append("Cuaca panas")
                    elif suhu_masuk in cuaca_terik:
                        print ("Cuaca terik")
                        semua_suhu.append(int(suhu_masuk))
                        cuaca.append("Cuaca terik")
                    else:
                        if suhu_masuk > 40:
                            print ("Suhu ekstrem")
                            semua_suhu.append(int(suhu_masuk))
                            cuaca.append("Suhu ekstrem")

            elif pilihan == '2':
                hapus_suhu = input("Apakah Anda salah menginput suhu? (ya/tidak): ")

                if hapus_suhu == 'ya':
                    hapus_suhu2 = int(input("Masukkan suhu yang ingin dihapus: "))

                    if hapus_suhu2 in semua_suhu:
                        index_hapus = semua_suhu.index(hapus_suhu2)
                        semua_suhu.remove(hapus_suhu2)
                        cuaca.pop(index_hapus)
                        print(f"Suhu {hapus_suhu2} telah dihapus.")
            elif pilihan == '3':
                suhu_masuk = input("Apakah Anda ingin menambahkan suhu?: ")

                if suhu_masuk == 'ya':
                    while True:
                        suhu = input("Masukkan suhu (°C): ")

                        if suhu == 'selesai':
                            print("Input suhu selesai.")
                            break
            else:
                pilihan == '4'
                print("Keluar dari program.")
                break

print(f"Total suhu yang diinput: {len(semua_suhu)}")
print(f"Daftar suhu yang diinput: {semua_suhu} ")
print(f"Daftar cuaca: {cuaca} ")

print("Update data" )
print("Update daftar suhu dan cuaca")

print("Meng-update data awal daftar suhu dan cuaca")
semua_suhu [0] = 23
cuaca[0] = "Cuaca Sejuk"

print("Daftar Suhu Terbaru:", semua_suhu)
print("Daftar Cuaca Terbaru", cuaca)

print("Sistem Pengelolaan data cuaca")
print("Silahkan login")
role = input("Anda sebagai? (Admin/User): ")

if login2():
    while True:
        print("Menu Pengelolaan data cuaca")
        print("1. Tampilkan data cuaca")
        print("2. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            print("Daftar data cuaca:")
            print(cuaca)
        else:
            pilihan == '2'
            print("Keluar dari program.")
            break
            
