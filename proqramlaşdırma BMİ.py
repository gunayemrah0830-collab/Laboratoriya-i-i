ç=float(input("çəkinizi daxil edin"))
b=float(input("boyunuzu daxil edin"))
BKİ=ç/(b**2)
if BKİ<18.5:
    print("çəki azlığı")
elif BKİ<24.9:
    print("normal çəki")
elif BKİ<29.9:
    print("artıq çəki")
else:
    print("obese")