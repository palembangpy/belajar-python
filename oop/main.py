'''
Empat Pilar OOP Python
=======================
1. Encapsulation
2. Absctraction
3. Inheritance
4. Polymorphism
'''

# TODO Encapsulation
# from object_oriented.encapsulation import Karyawan

# udin: Karyawan = Karyawan("Udin Surendang", 26, 1500000)
# print(udin.nama)
# print(udin.umur)
# print(udin.__gaji)

# TODO Abstraction
# from object_oriented.abstrak import User

# class Student(User):

#     def nama(self, nama: str) -> None:
#         print(nama)

#     def belajar(self, pelajaran: str) -> None:
#         print(pelajaran)

# samsul: Student = Student()
# samsul.belajar("Belajar Python bersama PalembangPy")

# TODO Polymorphism
from object_oriented.polymorphism import Mobil, Motor, BecakMotor

def test_kendaraan(kendaraan) -> None:
    kendaraan.maju()

kendaraan1: Mobil = Mobil()
kendaraan2: Motor = Motor()
kendaraan3: BecakMotor = BecakMotor()

test_kendaraan(kendaraan1)
test_kendaraan(kendaraan2)
test_kendaraan(kendaraan3)
