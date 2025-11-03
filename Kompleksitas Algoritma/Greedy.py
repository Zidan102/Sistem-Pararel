jumlah_uang = int(input("Masukkan jumlah uang: "))

uang = list(map(int, input("Masukkan daftar nilai koin (misal: 100000 50000 20000 10000 5000 2000 1000): ").split()))

uang.sort(reverse=True)

print("\nKombinasi koin yang digunakan:")
total_uang = 0
remaining = jumlah_uang

for uang in uang:
    count = remaining // uang
    if count > 0:
        print(f"{uang} x {count}")
        total_uang += count
        remaining %= uang

print(f"\nJumlah total koin: {total_uang}")