
from produk import Produk
from hash_table import InventarisProduk


def input_angka(pesan, tipe=int):
    while True:
        try:
            return tipe(input(pesan))
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def menu():
    print("\n=== INVENTARIS PRODUK ===")
    print("1. Tambah produk")
    print("2. Cari produk (by ID)")
    print("3. Hapus produk")
    print("4. Tampilkan semua produk")
    print("0. Keluar")


def main():
    inventaris = InventarisProduk()

    while True:
        menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            id_produk = input("ID Produk : ").strip()
            nama = input("Nama      : ").strip()
            harga = input_angka("Harga     : ")
            stok = input_angka("Stok      : ")
            kategori = input("Kategori  : ").strip()

            produk = Produk(
                id_produk, nama, harga, stok, kategori
            )

            if inventaris.tambah_produk(produk):
                print("Produk berhasil ditambahkan.")
            else:
                print("Gagal: ID produk sudah ada.")

        elif pilihan == "2":
            id_produk = input("ID Produk yang dicari: ").strip()
            hasil = inventaris.cari_produk(id_produk)

            print(hasil if hasil else "Produk tidak ditemukan.")

        elif pilihan == "3":
            id_produk = input("ID Produk yang dihapus: ").strip()

            if inventaris.hapus_produk(id_produk):
                print("Produk berhasil dihapus.")
            else:
                print("Produk tidak ditemukan.")

        elif pilihan == "4":
            daftar = inventaris.semua_produk()

            if not daftar:
                print("Inventaris masih kosong.")

            for p in daftar:
                print(p)

            print(f"Total: {inventaris.jumlah_produk()} produk")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()
