class KeretaApi(object):
    def __init__(self,namakereta,relasi,kelas):
        self.namakereta=namakereta
        self.relasi=relasi
        self.kelas=kelas
    
    def info(self):
        print(f"Nama Kereta : {self.namakereta}, Relasi : {self.relasi}, Kelas : {self.kelas}")

class ArgoWilis(KeretaApi):
    def __init__(self,namakereta,relasi,kelas,hargatiket,jadwal):
        super().__init__(namakereta,relasi,kelas)
        self.hargatiket=hargatiket
        self.jadwal=jadwal
    
    def WilisTiket(self):
        print("Tiket Tersedia")
        
    def info_wilis(self):
        print(f"Harga Tiket : {self.hargatiket}, Jadwal : {self.jadwal}")

class ArgoDwipangga(KeretaApi):
    def __init__(self,namakereta,relasi,kelas,hargatiket,jadwal):
        super().__init__(namakereta,relasi,kelas)
        self.hargatiket=hargatiket
        self.jadwal=jadwal
    
    def DwipanggaTiket(self):
        print("Tiket Tersedia")
    
    def info_dwipangga(self):
        print(f"Harga tiket : {self.hargatiket}, Jadwal : {self.jadwal}")