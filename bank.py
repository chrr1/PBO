class Rekening:
    def __init__(self,saldo):
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor tidak valid")
    
    def tarik(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Penarikan tidak valid")

rekening = Rekening(1000000)
print(rekening.saldo)

rekening.setor(500000)
print(rekening.saldo)

rekening.tarik(200000)
print(rekening.saldo)