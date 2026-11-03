
class Produk:
    """Data satu produk."""

    def __init__(self, id_produk, nama, harga, stok, kategori):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

    def __str__(self):
        return (
            f"[{self.id_produk}] {self.nama} | "
            f"Rp{self.harga:,} | stok: {self.stok} | "
            f"kategori: {self.kategori}"
        )
