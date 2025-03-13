nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")


if status.lower() == "tetap":
    gaji_pokok = 1000000
    bonus = {"a": 200000, "b": 400000, "c": 550000}.get(golongan.lower(), 0)
elif status.lower() == "honor":
    gaji_pokok = 750000
    bonus = {"a": 150000, "b": 275000, "c": 480000}.get(golongan.lower(), 0)
else:
    print("Status pegawai tidak valid!")
    exit()


gaji_total = gaji_pokok + bonus


print("Nama:", nama)
print("NIK:", nik)
print("Status:", status)
print("Golongan:", golongan)
print("Gaji Pokok: Rp{:,}".format(gaji_pokok))
print("Bonus: Rp{:,}".format(bonus))
print("Gaji Total: Rp{:,}".format(gaji_total))