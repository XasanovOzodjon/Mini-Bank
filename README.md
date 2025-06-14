
# 🏦 Mini Bank

**Mini Bank** — bu terminalda ishlovchi Python asosidagi soddalashtirilgan bank ilovasi bo‘lib, foydalanuvchiga akkaunt yaratish, balansni ko‘rish, pul qo‘shish, pul yechish (kupyura formatida) kabi funksiyalarni taklif qiladi.

---

## 📌 Xususiyatlari

- 🆕 Akkaunt yaratish, o‘chirish va ismni o‘zgartirish
- 💰 Pul qo‘shish va chiqarish (min 1$)
- 🧾 Pul chiqarishda kupyuralar sonini hisoblab beradi
- 🧍‍♂️ Har bir foydalanuvchi faqat o‘z seansida ishlaydi (global sessiya)
- 🧼 Terminal avtomatik tozalanadi (`clear` komanda orqali)

---

## 🖥️ Ekran lavhalari (CLI menyular)

```
<<< Siz Bosh Saxifadasiz >>>
    1 – Account Settings
    2 – Mening Hisobim
    3 - Pul qo'shish
    4 - Pul chiqarish
    5 - Dasturdan chiqish(exit)
```

```
<<< Account Settings >>>
    1 – Account Yaratish
    2 – Ismni o'zgartirish
    3 - Accountni O'chirish
    4 - Bosh menu ga qaytish
```

---

## 🚀 Ishga tushirish

1. Python 3 o‘rnatilganligiga ishonch hosil qiling.
2. Konsolda quyidagi buyruqni bajarish orqali faylni ishga tushiring:

```bash
python3 main.py
```

> **MacOS foydalanuvchilari uchun** `os.system("clear")` terminalni tozalaydi. Windows foydalanuvchilari uchun `cls` bilan almashtirish mumkin.

---

## 🧩 Bog‘liq kutubxonalar

- `random` — akkauntni o‘chirishda CAPTCHA kodi uchun
- `typing.Union` — qiymatlar bo‘lishi yoki bo‘lmasligi mumkinligini belgilash
- `os` — terminalni tozalash uchun
- `sys` — dasturdan chiqish uchun

---

## 💸 Kupyura hisoblash funksiyasi

`withdraw_kupyur(amount)` funksiyasi chiqarilgan pulni quyidagi formatda taqdim etadi:

```
Marxamat pulingizni oling!
2ta 100$ lik kupyura
1ta 50$ lik kupyura
3ta 10$ lik kupyura
1ta 1$ lik kupyura
```

---

## ⚠️ Cheklovlar

- Faqat **bitta foydalanuvchi** bilan ishlaydi (global o'zgaruvchilar orqali).
- Foydalanuvchi nomida raqam yoki belgi bo‘lishi mumkin emas.
- Balans 1$ dan kam bo‘lsa, pul yechib bo‘lmaydi.

---

## 📄 Litsenziya

Ushbu loyiha shunchaki o‘rganish maqsadida yaratilgan. Istalgancha o‘zgartirib, foydalanishingiz mumkin.

---

## 👤 Muallif

- Ism: **Ozodjon Xasanov**
- Til: Python
- Maqsad: Terminalda soddalashtirilgan bank ilovasi yasash orqali dasturlashni mustahkamlash
