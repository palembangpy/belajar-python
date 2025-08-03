class Karyawan:
    
    def __init__(self, nama: str, umur: int, gaji: int | float) -> None:
        self.nama = nama # public
        self.umur = umur # public
        self.__gaji = gaji # private

    def get_gaji(self) -> float:
        return self.__gaji

    def set_gaji(self, set_gaji: float) -> float:
        self.__gaji = set_gaji
        return self.__gaji