class Mahasiswa:
    def __init__(self,nim,nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self,nilai):
        self.daftar_nilai.append(nilai)

    def hitung_rata_rata(self):
        if len(self.daftar_nilai) == 0:
            return 0
        return sum(self.daftar_nilai) / len(self.daftar_nilai)

    def tampilkan_data(self):
        rata = self.hitung_rata_rata()
        print(f'NIM: {self.nim} | Nama: {self.nama} | Rata-rata: {rata:.2f}')

