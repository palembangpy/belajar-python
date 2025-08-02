# print("Hello World!")

'''
0. Hello World [x]
1. Variable [x]
2. Tipe Data [x]
3. Tipe Anotasi [x]
4. Looping [x]
5. Operasi Perbandingan [x]
6. if..elif..else [x]
7. Fungsi [x]
8. Error Handling [x]
9. Import [x]
10. Project Kalkulator Sederhana [x]
'''

'''
snake_case
camelCase
UPPERCASE
'''

# text = "Halo Python!" #string
# number = 26 # integer
# desimal = 10.13 # float
# is_admin = False # boolean
# daftar = ["Udin", "Surendang", 26, ["Berenang", "Membaca", "Memanah"]] # list
# host = ("localhost", 5000) # tuple
# unique = {"Udin", 123, 90.6, 55, 55, "Udin", "Udin"} # set
# pustaka = {"nama": "Udin Surendang", "umur": 26, "hobby": ["Berenang", "Membaca", "Memanah"]}

# TODO For Loop
# h = 0
# for i in range(11):
#     print(i)
#     i += h

# TODO While Loop
# i: int = 7
# while True:
#     print(i)
#     i += 1

# TODO Operator Perbandingan
'''
== > < <= >= ! != 

&& || ! and or not
'''

# username: str = "udinsurendang"
# password: str = "rahasiA"

# if username != username.lower() or password != password.lower():
#     print("username mengandung kalimat kapital.")
# elif password == "secret":
#     print("Anda Login...")
# else:
#     print("Direct...")

# def sapa(nama: str, ucapan: str) -> str:
#     return f"Selamat datang, {nama}\n{ucapan}"

# try:
#     # sapa("Udin Surendang")
#     print(89/0)

# except TypeError as te:
#     raise TypeError("Kamu kurang memasukan 1 argumen.")
# except ZeroDivisionError as zde:
#     raise ZeroDivisionError("Ooops!!",)

# TODO Imports
# from module import tambah, kurang, kali

# print("Hasilnya:", tambah(6, 9))
# print("Hasilnya:", kurang(6, 9))
# print("Hasilnya:", kali(6, 9))

while True:
    input_1 = float(input("Masukan bilangan pertama: "))
    input_2 = input("Masukan jenis operator aritmatika (+, -, x, /): ")
    input_3 = float(input("Masukan bilangan kedua: "))

    if input_2 == "+":
        print("Hasil:", input_1 + input_3)
    elif input_2 == "-":
        print("Hasil:", input_1 - input_3)
    elif input_2 == "x":
        print("Hasil:", input_1 * input_3)
    elif input_2 == "/":
        print("Hasil:", input_1 / input_3)
    else:
        print("Kami hanya menerima 4 operator aritmatika")



'''
Versi Rilis Python 
v0.9 - 1991 (Versi Awal)
v1.0 - 1994
v2.0 - 2000
v3.0 - 2008
'''

