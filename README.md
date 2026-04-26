# AdLex.uz

**Korrupsiyaga qarshi fuqarolik nazorat tizimi**

Ushbu loyiha O'zbekiston hududlarida joylashgan davlat tashkilotlari, muassasalar va mahallalar bo'yicha ochiq ma'lumotlar xaritasini taqdim etadi. Tizim orqali fuqarolar shikoyat yuborishi, byudjet sarflanishini kuzatishi va mansabdor shaxslar haqida ma'lumot olishi mumkin.

---

## Imkoniyatlar

- Interaktiv viloyat xaritasi — hodisalar zichligi bo'yicha rang ko'rsatkichi
- Tashkilotlar va mansabdor shaxslar ma'lumotlar bazasi
- Byudjet ajratmalari va bajarilish holati
- Fuqarolik shikoyatlarini qabul qilish va yo'naltirish tizimi
- Soha va hudud bo'yicha avtomatik statistika

## Texnologiyalar

- Vanilla HTML / CSS / JavaScript
- GitHub Pages (hosting)
- SVG xarita (O'zbekiston viloyatlari)

## Ishga tushirish

```bash
git clone https://github.com/USERNAME/shaffoflik-xaritasi.git
cd shaffoflik-xaritasi
# index.html faylini brauzerda oching
```

## GitHub Pages orqali joylash

1. Repository → **Settings** → **Pages**
2. Source: **GitHub Actions**
3. `main` branchiga push qiling — sayt avtomatik joylashadi

## Loyiha tuzilishi

```
shaffoflik-xaritasi/
├── index.html          # Asosiy ilova
├── README.md           # Hujjatlar
└── .github/
    └── workflows/
        └── deploy.yml  # Avtomatik joylash
```

## Litsenziya

MIT License — ochiq manba, erkin foydalanish mumkin.
