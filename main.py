import os
from typing import Union
from random import randint
import sys

name: Union[str, None] = None
balans: Union[float, None] = None


def open_accaunt() -> None:
    global name
    global balans
    if name != None:
        print("Sizning akkauntingiz mavjud! \n")
    else:
        temp_name = input("Ismingizni kiriting!\n>>>")
        if temp_name.isalpha():
            name = temp_name
            balans = 0.0
            os.system("clear")
            print("Account Yaratildi✅\n")
        else:
            os.system("clear")
            print("Xatolik! Ismingizda belgi yoki raqam bo'lishi mumkin emas!\n")
        


def delete_accaunt() -> None:
    global name
    global balans
    if name == None:
        print("Sizda akkaunt mavjud emas!\n")
    else:
        os.system("clear")
        random_num = randint(1000, 9999)
        x = int(input(f"Akkauntingizni o'chirishingiz robot emasligingizni tastiqlang!\n({random_num}) kodini kiriting: "))
        if x == random_num:
            name = None
            balans = None
            os.system("clear")
            print("Akkauntingiz o'chirildi\n")
        else:
            os.system("clear")
            print("Siz kodni xato kiritingiz! Keynroq qaytatan xarakat qilib kuring\n")


def set_name() -> None:
    global name
    if name == None:
        print("Akkaunting yo'q! Iltimos \"Accaunt settings\" menusiga kirib accaunt yarating!\n")
    else:
        temp_name = input("Ismingizni kiriting!\n>>>")
        if temp_name.isalpha():
            name = temp_name
            os.system("clear")
        else:
            os.system("clear")
            print("Xatolik! Ismingizda belgi yoki raqam bo'lishi mumkin emas!\n")


def check_account() -> None:
    if name == None:
        print("Akkaunting yo'q! Iltimos \"Accaunt settings\" menusiga kirib accaunt yarating!\n")
    else:
        print(f"Assalomu aleykum {name}")
        print(f"Sizning balansingizda {balans}$ mavjud\n")


def deposit() -> None:
    global balans
    if name == None:
        print("Akkaunting yo'q! Iltimos \"Accaunt settings\" menusiga kirib accaunt yarating!\n")
    else:
        balans = float(input("Qancha pul qo'shmoqchisiz?\n>>>"))
        os.system("clear")


def withdraw() -> None:
    global balans
    if name == None:
        print("Akkaunting yo'q! Iltimos \"Accaunt settings\" menusiga kirib accaunt yarating!\n")
    else:
        withdraw_money = round(float(input("Qancha summa yechib olmoqchisiz?\n>>>")), 2)
        if balans < withdraw_money:
            print("Balansingizda yetarlicha mablag mavjut emas!")
        else:
            if withdraw_money >= 1:
                withdraw_kupyur(withdraw_money)
                balans = balans - withdraw_money
                input()
                os.system("clear")
            else:
                print("Eng kami 1$ chiqarib olasiz")



def withdraw_kupyur(amount):

    cent = amount % 1 
    cent = int(cent*10)
    cent = cent % 1

    c100 = int(amount // 100)
    amount = amount % 100

    c50 = int(amount // 50)
    amount = amount % 50

    c10 = int(amount // 10)
    amount = amount % 10

    c1 = int(amount // 1)
    amount = amount % 1
    if cent > 0 :
        if c100 > 0:
            print(f"Marxamat pulingizni oling!\n{c100}ta 100$ lik kupyura\n{c50}ta 50$ lik kupyura\n{c10}ta 10$ lik kupyura\n{c1}ta 1$ lik kupyura\n{cent}ta 1cent lik tanga")
        elif c50 > 0:
            print(f"Marxamat pulingizni oling!\n{c50}ta 50$ lik kupyura\n{c10}ta 10$ lik kupyura\n{c1}ta 1$ lik kupyura\n{cent}ta 1cent lik tanga")
        elif c10 > 0:
            print(f"Marxamat pulingizni oling!\n{c10}ta 10$ lik kupyura\n{c1}ta 1$ lik kupyura\n{cent}ta 1cent lik tanga")
        else:
            print(f"Marxamat pulingizni oling!\n{c1}ta 1$ lik kupyura\n{cent}ta 1cent lik tanga")
    else:
        if c100 > 0:
            print(f"Marxamat pulingizni oling!\n{c100}ta 100$ lik kupyura\n{c50}ta 50$ lik kupyura\n{c10}ta 10$ lik kupyura\n{c1}ta 1$ lik kupyura")
        elif c50 > 0:
            print(f"Marxamat pulingizni oling!\n{c50}ta 50$ lik kupyura\n{c10}ta 10$ lik kupyura\n{c1}ta 1$ lik kupyura")
        elif c10 > 0:
            print(f"Marxamat pulingizni oling!\n{c10}ta 10$ lik kupyura\n{c1}ta 1$ lik kupyura")
        else:
            print(f"Marxamat pulingizni oling!\n{c1}ta 1$ lik kupyura")




def accaunt_set() -> None:
    while True:
        print("<<< Account Settings >>>")
        print("    1 – Account Yaratish")
        print("    2 – Ismni o'zgartirish")
        print("    3 - Accountni O'chirish")
        print("    4 - Bosh menu ga qaytish")        
        tanlov = input("\n>>>")
        os.system("clear")

        if tanlov == "1":
            open_accaunt()
        elif tanlov == "2":
            set_name()
        elif tanlov == "3":
            delete_accaunt()
        elif tanlov == "4":
            main()
        else:
            print("Mavjut bo'lmagan buyruq! Qaytatan urinib ko'ring 👇\n")

def main() -> None:
    while True:
        print("<<< Siz Bosh Saxifadasiz >>>")
        print("    1 – Account Settings")
        print("    2 – Mening Hisobim")
        print("    3 - Pul qo'shish")
        print("    4 - Pul chiqarish")
        print("    5 - Dasturdan chiqish(exit)")
        tanlov = input("\n>>>")
        os.system("clear")

        if tanlov == "1":
            accaunt_set()
        elif tanlov == "2":
            check_account()
        elif tanlov == "3":
            deposit()
        elif tanlov == "4":
            withdraw()
        elif tanlov == "5":
            sys.exit()
        else:
            print("Mavjut bo'lmagan buyruq! Qaytatan urinib ko'ring 👇\n")
        

main()