def tambah(x, y)
  return x+y

def kurang(x, y)
  return x-y

def kali(x, y)
  return x*y

def bagi(x, y)
  return x/y

#########LOGO#########
logo():"""
_  _ ____ _    _  _ _  _ _    ____ ___ ____ ____ 
|_/  |__| |    |_/  |  | |    |__|  |  |  | |__/ 
| \_ |  | |___ | \_ |__| |___ |  |  |  |__| |  \ 
                                                 
•=========================================•
• Author   : Iwan Hadiansah ID
• File     : By > Iwan Hadiansah ID
• Facebook : Iwan Hadiansah ID
• WhatsApp : Usaha Sendiri Ya Ngab
• github   : https://github.com/IWAN-404
•=========================================•"""
• Tools Kalkulator By : Iwan Hadiansah ID
print"•====================================•"
print" 1•=> perjumlahan"
print" 2•=> perkurangan"
print" 3•=> perkalian"
print" 4•=> pembagiann"
print"•====================================•"

pilih•=> input("•pilih > ")
bil1•=> int(input("Masukan Bilangan Pertama > "))
bil2•=> int(input("Masukan Bilangan Kedua > "))


if pilih•=> 1:
    print" ", bil1, "+", bil2, "=", tambah(bil1, bil2)
    
elif pilih•=> 2:
    print" ", bil1, "-", bil2, "=", kurang(bil1, bil2)
    
elif pilih•=> 3:
    print" ", bil1, "*", bil2, "=" kali(bil1, bil2)
    
elif pilih•=> 4:
    print" ", bil1, "/" bil2, "=" bagi(bil1, bil2)