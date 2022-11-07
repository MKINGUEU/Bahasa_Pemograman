def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = capucino * 10/100
    total = capucino+ppn
    print("Jumlah yang harus di bayarkan", total)

def teh():
    cap = "memilih teh"
    print(cap)
    teh= int(input("masukkan harga : "))
    ppn = teh * 10/100
    total = teh+ppn
    print("Jumlah yang harus di bayarkan", total)

def pilihan():
    print("Nim : 1234567")
    print("Nama : QWERTY")
    print("1. Capucino")
    print("2. Teh")
    print("3. exit")

while True:
    pilihan()
    pil=int(input("masukan pilihan : "))
    if pil==1:
        capucino()
    elif pil==2:
        teh()
    else :
        break
