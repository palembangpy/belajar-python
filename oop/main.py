'''
Empat Pilar OOP Python
=======================
1. Encapsulation (mengisolasi sebuah data di dalam kelas)
2. Abstraction (interface dari sebuah metaclass / blueprint)
3. Inheritance (pewaris yang selalu dan harus mengimplementasi method yang berada di dalam superclass / interface)
4. Polymorphism (memiliki banyak kelas dengan nama method yang sama)
'''

# TODO Encapsulation
# from package.encapsulation import Karyawan

# udin: Karyawan = Karyawan("Udin Surendang", "HRD", 5500000)
# # udin.set_gaji(15000000)
# # udin.__gaji = 50000000

# # print(udin.__gaji)
# print(f"Nama: {udin.nama}")
# print(f"Jabatan: {udin.jabatan}")
# print(f"Gaji: {udin.get_gaji()}")

# TODO Abstraction & Inheritance
# from package.abstraksi import Staff

# admin: Staff = Staff()
# admin.role("Administration")
# admin.jobdesk("menuliskan laporan")
# admin.is_resign(True)

# TODO Polymorphism
from package.polymorphism import Mobil, Motor, Becak

def test_maju(kendaraan) -> None: kendaraan.maju()

kendaraan1: Mobil = Mobil()
kendaraan2: Motor = Motor()
kendaraan3: Becak = Becak()

# Menampilkan
test_maju(kendaraan1)
test_maju(kendaraan2)
test_maju(kendaraan3)
