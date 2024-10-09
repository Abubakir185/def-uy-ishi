# 1. Parametrli funksiya uchun vazifa: - Parametr sifatida `name` qabul qiluvchi va 
# shu nom yordamida salomlashishni chop etadigan `say_salom(ism)` 
# funksiyasini yozing. - `say_hello()` funksiyasiga qo'ng'iroq qiling va unga salom aytish uchun turli nomlarni bering

def say_hello(name):
    print(f"Salom {name}")

say_hello("Ali")
say_hello("Abubakir")

def say_hello(name):
    print(f"Salom {name}")

ism = input("ism: ")
say_hello(ism)

# 2. Matematik amallar bilan funksiya uchun vazifa: - Ikkita `a` va `b` sonlarni parametr 
# sifatida qabul qiluvchi, ularni qo`shib, natijani qaytaruvchi `hisoblash_sum(a, b)` funksiyasini
#  yozing. - Turli qiymatlar bilan `hisoblash_sum()` funksiyasini chaqiring va natijani chop eting.

def hisoblash_sum(b,a):
    print(f"{a} + {b} = {a + b}")


son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))

hisoblash_sum(son1, son2)

# 3. Roʻyxatlar bilan ishlaydigan funksiya uchun topshiriq: - Parametr sifatida `raqamlar` ro'yxatini 
# oladigan va uning elementlarini ekranga chop etuvchi `chop etish_ro'yxati_raqamlar(raqamlar)` 
# funksiyasini yozing. - Turli raqamlar ro'yxati bilan `print_list_numbers()` funksiyasiga qo'ng'iroq qiling

list = [1, 4, 5, 7, 8]
list2 = [3, 6, 90, 12, 8]

def chop_etish(raqamlar):
    print(list)

chop_etish(list)
chop_etish(list2)


# 4. Shartli operatorlar bilan funksiya uchun vazifa: - Parametr sifatida “raqam” raqamini qabul qiladigan va 
# agar raqam juft bo‘lsa “To‘g‘ri”, toq bo‘lsa “Yo‘g‘on” qiymatini qaytaradigan “juft(raqam)” 
# funksiyasini yozing. - `is_even()` funksiyasini turli raqamlar bilan chaqiring va natijani chop eting. 

def is_even(raqam):
    if raqam % 2 == 0:
        print("To'g'ri")
    else:
        print("Yolg'on")


son = int(input("Raqam kiritng: "))

is_even(son)


#  5. Tsiklli funksiya uchun vazifa: - Parametr sifatida ikkita `start` va `end` raqamlarni oladigan va ekranda `start
# ` dan ` end`gacha bo`lgan raqamlarni chop etadigan `print_numbers(start, end) funksiyasini yozing. - Turli `start` 
# va `end` qiymatlari 
# bilan `print_numbers()` funksiyasini chaqiring.

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)

start = int(input("Start: "))
end = int(input("End: "))

print_numbers(start, end)