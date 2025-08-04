# TODO Ecapsulation

'''
1. Kelas
2. Atribut Kelas
3. Method Kelas 
'''
class Karyawan:
    nama: str = ""
    jabatan: str = ""
    __gaji: int | float = 0

    # Initialize / Construct
    def __init__(self, nama: str, jabatan: str, gaji: int | float) -> None:
        Karyawan.nama = nama
        Karyawan.jabatan = jabatan
        Karyawan.__gaji = gaji
    
    def get_gaji(self) -> int | float:
        return Karyawan.__gaji

    def set_gaji(self, gaji_sekarang: int) -> int | float:
        Karyawan.__gaji = gaji_sekarang
        return Karyawan.__gaji

