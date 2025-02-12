class akunbank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def deposit(self, jumlah):
        self.saldo += jumlah
        return f"Saldo anda sekarang: Rp.{self.saldo}"
        
rekening = akunbank("Wannn Sion", 500000)
print(rekening.deposit(200000))
