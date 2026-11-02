"""Benchmark: dict vs list vs linked list vs list terurut (binary search).
Mengukur rata-rata waktu per operasi (mikrodetik) untuk tambah, cari, hapus,
dan tampil semua."""

import bisect
import random
import time


# ---------- 1. Hash Table (dict) ----------
class InvDict:
    def __init__(self):
        self.d = {}

    def muat(self, ids):
        self.d = {i: f"Produk-{i}" for i in ids}

    def tambah(self, i):
        if i in self.d:
            return False
        self.d[i] = f"Produk-{i}"
        return True

    def cari(self, i):
        return self.d.get(i)

    def hapus(self, i):
        return self.d.pop(i, None) is not None

    def semua(self):
        return list(self.d.values())


# ---------- 2. Python list ----------
class InvList:
    def __init__(self):
        self.a = []

    def muat(self, ids):
        self.a = [(i, f"Produk-{i}") for i in ids]

    def tambah(self, i):
        for k, _ in self.a:          # cek duplikat O(n)
            if k == i:
                return False
        self.a.append((i, f"Produk-{i}"))
        return True

    def cari(self, i):
        for k, v in self.a:          # linear O(n)
            if k == i:
                return v
        return None

    def hapus(self, i):
        for idx, (k, _) in enumerate(self.a):
            if k == i:
                self.a.pop(idx)      # geser elemen O(n)
                return True
        return False

    def semua(self):
        return [v for _, v in self.a]


# ---------- 3. Linked List ----------
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class InvLinkedList:
    def __init__(self):
        self.head = None

    def muat(self, ids):
        self.head = None
        for i in ids:
            n = Node(i, f"Produk-{i}")
            n.next = self.head
            self.head = n

    def tambah(self, i):
        cur = self.head
        while cur:                   # cek duplikat O(n)
            if cur.key == i:
                return False
            cur = cur.next
        n = Node(i, f"Produk-{i}")
        n.next = self.head           # sisip di head O(1)
        self.head = n
        return True

    def cari(self, i):
        cur = self.head
        while cur:
            if cur.key == i:
                return cur.val
            cur = cur.next
        return None

    def hapus(self, i):
        prev, cur = None, self.head
        while cur:
            if cur.key == i:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def semua(self):
        hasil, cur = [], self.head
        while cur:
            hasil.append(cur.val)
            cur = cur.next
        return hasil


# ---------- 4. List terurut + Binary Search ----------
class InvTerurut:
    def __init__(self):
        self.k = []

    def muat(self, ids):
        self.k = sorted(ids)

    def tambah(self, i):
        pos = bisect.bisect_left(self.k, i)      # O(log n)
        if pos < len(self.k) and self.k[pos] == i:
            return False
        self.k.insert(pos, i)                    # geser O(n)
        return True

    def cari(self, i):
        pos = bisect.bisect_left(self.k, i)      # O(log n)
        if pos < len(self.k) and self.k[pos] == i:
            return f"Produk-{i}"
        return None

    def hapus(self, i):
        pos = bisect.bisect_left(self.k, i)
        if pos < len(self.k) and self.k[pos] == i:
            self.k.pop(pos)                      # geser O(n)
            return True
        return False

    def semua(self):
        return [f"Produk-{i}" for i in self.k]


def ukur(fungsi, argumen):
    """Rata-rata waktu per panggilan, dalam mikrodetik."""
    mulai = time.perf_counter()
    for a in argumen:
        fungsi(a)
    selesai = time.perf_counter()
    return (selesai - mulai) / len(argumen) * 1_000_000


def jalankan(n, q=100):
    random.seed(42)
    ids = list(range(1, n + 1))
    random.shuffle(ids)
    id_cari = random.sample(ids, q)
    id_hapus = random.sample(ids, q)
    id_baru = list(range(n + 1, n + 1 + q))

    kelas = [("dict", InvDict), ("list", InvList),
             ("linked list", InvLinkedList), ("list terurut", InvTerurut)]

    print(f"\n=== n = {n:,} produk (rata-rata {q} operasi, satuan mikrodetik) ===")
    print(f"{'Struktur':<14}{'Tambah':>12}{'Cari':>12}{'Hapus':>12}{'Tampil':>14}")
    for nama, K in kelas:
        s = K()
        s.muat(ids)
        t_cari = ukur(s.cari, id_cari)
        t_tambah = ukur(s.tambah, id_baru)
        t_hapus = ukur(s.hapus, id_hapus)
        t_semua = ukur(lambda _: s.semua(), [0] * 5)
        print(f"{nama:<14}{t_tambah:>12.2f}{t_cari:>12.2f}"
              f"{t_hapus:>12.2f}{t_semua:>14.2f}")


if __name__ == "__main__":
    for n in (1_000, 10_000, 100_000):
        jalankan(n)
