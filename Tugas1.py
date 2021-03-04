while True:
  try:
    x = float(input("Masukkan angka: "))
    if x >= 0 or x < 0:
        if x >= 0:
            if x == 0:
                print("nol")
            else:
                print("angka positif")
        else:
            print("angka negatif")
        break
    print("Masukkan angka")
  except Exception as e:
    print("Masukkan angka")
