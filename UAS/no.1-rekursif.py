def faktorial(i):
   if i == 1:
      return (i)
   else:
      return (i*faktorial(i-1))

bil = int(input("Masukan Bilangannya : "))

print("%d! = %d" % (bil, faktorial(bil)))