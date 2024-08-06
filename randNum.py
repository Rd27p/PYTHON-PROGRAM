import random

def tebak_angka():
    angkaTebakan = random.randint(1, 1000)
    percobaan = 0

    print("Tebaklah angka 1 sampai dengan 1000")

    while True:
        tebak = int(input("Masukkan Tebakan kamu!: "))
        percobaan += 1

        if tebak < angkaTebakan:
            print("Lebih Tinggi")
        elif tebak > angkaTebakan:
            print("Lebih Rendah")
        else:
            print(f"Selamat kamu berhasil menebak angkanya dalam {percobaan} percobaan.")
            break

if __name__ == "__main__":
    tebak_angka()
