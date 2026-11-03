"""Struktur data pembanding untuk benchmark.

Semua kelas punya method yang sama (ADT yang sama), sehingga struktur data
bisa diganti tanpa mengubah kode pemanggil:
    muat(daftar), tambah_produk(p), cari_produk(id), hapus_produk(id),
    semua_produk()
"""

import bisect


# ---------- 1. Hash Table (dict) ----------
class InventarisHashTable:
    def __init__(self):
        self._data = {}

    def muat(self, daftar):
        self._data = {p.id_produk: p for p in daftar}

    def tambah_produk(self, produk):
        if produk.id_produk in self._data:      # cek duplikat O(1)
            return False
        self._data[produk.id_produk] = produk
        return True

    def cari_produk(self, id_produk):
        return self._data.get(id_produk)        # O(1) rata-rata

    def hapus_produk(self, id_produk):
        return self._data.pop(id_produk, None) is not None

    def semua_produk(self):
        return list(self._data.values())


# ---------- 2. Array-based list (Python list) ----------
class InventarisList:
    def __init__(self):
        self._data = []

    def muat(self, daftar):
        self._data = list(daftar)

    def tambah_produk(self, produk):
        for p in self._data:                    # cek duplikat O(n)
            if p.id_produk == produk.id_produk:
                return False
        self._data.append(produk)               # append O(1) amortized
        return True

    def cari_produk(self, id_produk):
        for p in self._data:                    # linear search O(n)
            if p.id_produk == id_produk:
                return p
        return None

    def hapus_produk(self, id_produk):
        for idx, p in enumerate(self._data):    # cari O(n)
            if p.id_produk == id_produk:
                self._data.pop(idx)             # geser elemen O(n)
                return True
        return False

    def semua_produk(self):
        return list(self._data)


# ---------- 3. Linked List ----------
class NodeProduk:
    def __init__(self, data):
        self.data = data
        self.next = None


class InventarisLinkedList:
    def __init__(self):
        self.head = None

    def muat(self, daftar):
        self.head = None
        for p in daftar:
            node = NodeProduk(p)
            node.next = self.head
            self.head = node

    def tambah_produk(self, produk):
        cur = self.head
        while cur:                              # cek duplikat O(n)
            if cur.data.id_produk == produk.id_produk:
                return False
            cur = cur.next
        node = NodeProduk(produk)
        node.next = self.head                   # sisip di head O(1)
        self.head = node
        return True

    def cari_produk(self, id_produk):
        cur = self.head
        while cur:                              # telusuri node O(n)
            if cur.data.id_produk == id_produk:
                return cur.data
            cur = cur.next
        return None

    def hapus_produk(self, id_produk):
        prev, cur = None, self.head
        while cur:                              # cari node O(n)
            if cur.data.id_produk == id_produk:
                if prev:
                    prev.next = cur.next        # lepas node O(1)
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def semua_produk(self):
        hasil, cur = [], self.head
        while cur:
            hasil.append(cur.data)
            cur = cur.next
        return hasil


# ---------- 4. List terurut + Binary Search ----------
class InventarisTerurut:
    def __init__(self):
        self._id = []        # daftar ID terurut
        self._produk = []    # objek Produk, urutannya sejajar dengan _id

    def muat(self, daftar):
        urut = sorted(daftar, key=lambda p: p.id_produk)
        self._id = [p.id_produk for p in urut]
        self._produk = urut

    def tambah_produk(self, produk):
        pos = bisect.bisect_left(self._id, produk.id_produk)    # O(log n)
        if pos < len(self._id) and self._id[pos] == produk.id_produk:
            return False
        self._id.insert(pos, produk.id_produk)                  # geser O(n)
        self._produk.insert(pos, produk)
        return True

    def cari_produk(self, id_produk):
        pos = bisect.bisect_left(self._id, id_produk)           # O(log n)
        if pos < len(self._id) and self._id[pos] == id_produk:
            return self._produk[pos]
        return None

    def hapus_produk(self, id_produk):
        pos = bisect.bisect_left(self._id, id_produk)
        if pos < len(self._id) and self._id[pos] == id_produk:
            self._id.pop(pos)                                   # geser O(n)
            self._produk.pop(pos)
            return True
        return False

    def semua_produk(self):
        return list(self._produk)
