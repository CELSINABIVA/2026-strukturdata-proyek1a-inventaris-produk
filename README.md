# 2026-daa-proyek1a-inventaris-produk
# Sistem Manajemen Inventaris Produk

Proyek 1a mata kuliah Struktur Data, Program Studi Teknik Informatika, Fakultas Sains dan Teknologi, UIN Sultan Syarif Kasim Riau.

- Nama: CELSI NABIVA
- NIM: 12550125685

## Deskripsi
Program ini mensimulasikan sistem inventaris produk e-commerce yang harus menangani jutaan data. Tiga operasi utamanya adalah menambah produk, mencari produk berdasarkan ID, dan menghapus produk.

Proyek ini membandingkan kompleksitas waktu (Big-O) tiga struktur data:
1. Python list (array-based)
2. Linked list (ADT buatan sendiri)
3. Hash table (Python dict)

Hasilnya, **hash table (dict)** dipilih karena tambah, cari, dan hapus berdasarkan ID unik rata-rata O(1).

## Struktur File

| File | Fungsi |
|---|---|
| `inventaris_produk.py` | Program CLI dengan ADT `InventarisProduk` berbasis dict (tambah, cari, hapus, tampilkan semua) |
| `benchmark.py` | Pengukuran waktu operasi pada dict, list, linked list, dan list terurut (binary search) |

## Cara Menjalankan

Pastikan Python 3 sudah terpasang. Tidak ada library tambahan yang dibutuhkan.
Menjalankan program inventaris:

```
python inventaris_produk.py
```

Menjalankan benchmark:

```
python benchmark.py
```

Benchmark mengukur rata-rata waktu per operasi (dalam mikrodetik) pada 1.000, 10.000, dan 100.000 produk.

## Menu Program

```
1. Tambah produk
2. Cari produk (by ID)
3. Hapus produk
4. Tampilkan semua produk
0. Keluar
```

## Kompleksitas Waktu

| Operasi | Python list | Linked List | Hash Table (dict) |
|---|---|---|---|
| Insert | O(1)* | O(1)* | O(1) rata-rata |
| Search by ID | O(n) | O(n) | O(1) rata-rata |
| Delete | O(n) | O(n) | O(1) rata-rata |

*Karena ID harus unik, insert pada list dan linked list wajib mengecek duplikat sehingga menjadi O(n).

## Hasil Benchmark (n = 100.000 produk, mikrodetik)

| Struktur | Tambah | Cari | Hapus | Tampil semua |
|---|---|---|---|---|
| dict | 0,21 | 0,26 | 0,28 | 1.079 |
| list | 2.351 | 1.354 | 2.546 | 2.613 |
| linked list | 3.435 | 1.682 | 3.393 | 4.286 |
| list terurut | 1,13 | 0,73 | 9,65 | 8.381 |

Angka dapat berbeda tergantung perangkat yang digunakan.

## Link Video Presentasi


