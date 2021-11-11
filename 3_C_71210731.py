alas = int(input("Masukan Alas Atap: "))
tinggi = int(input("Masukan Tinggi Atap: "))
tembok = int(input("Masukan Tinggi Tembok: "))

S = (tinggi * alas) / 2  
P = tembok * tembok
H = S + P
T = H / 5
print(f'Rumah tersebut membutuhkan {T} sak semen')
