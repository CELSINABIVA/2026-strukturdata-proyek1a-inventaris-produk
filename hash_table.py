
class InventarisProduk:
    """ADT inventaris menggunakan Hash Table (dict)."""

    def __init__(self):
        self._data = {}

    def tambah_produk(self, produk):
        """Menambahkan produk, rata-rata O(1)."""
        if produk.id_produk in self._data:
            return False

        self._data[produk.id_produk] = produk
        return True

    def cari_produk(self, id_produk):
        """Mencari produk berdasarkan ID, rata-rata O(1)."""
        return self._data.get(id_produk)

    def hapus_produk(self, id_produk):
        """Menghapus produk, rata-rata O(1)."""
        if id_produk in self._data:
            del self._data[id_produk]
            return True

        return False

    def jumlah_produk(self):
        return len(self._data)

    def semua_produk(self):
        return list(self._data.values())
