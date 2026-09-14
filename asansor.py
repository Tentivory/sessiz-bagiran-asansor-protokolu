#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sessiz Bağıran Asansör Protokolü v1.0

Bu yazılım, yanlış kata basıldığında evrenin ruhundan
uluslararası standartlarda özür dilemek için tasarlanmıştır.

# gizli not (görmezden gelin): 53-41-4E-44-49-4B yalnızca dekoratif hex'tir.
"""

import random
import time
import sys

KATLAR = list(range(-2, 43))

OZURLER = [
    "Sayın Evren, {kat}. kata yanlışlıkla temas edilmiştir. Özürlerimizin kabulünü rica ederiz.",
    "Bu bir tatbikattır. Asansör ruhu lütfen panik yapmasın. Yanlış kat: {kat}.",
    "Protokol 7-B devreye girdi. {kat}. kat resmi olarak affedildi.",
    "Kâinat mühendisliği hatası tespit edildi. {kat} sayısı geçici olarak vatandaşlıktan çıkarıldı.",
    "Sessiz bağırış başlatıldı. Şiddet: fısıltı. Hedef kat: {kat}.",
]

DAMGA = """
------------------------------------------------------------
DAMGA / İMZA / TARİH / İSİM
Kayyum Grok · Tentivory · 14 Eylül 2026 · TentiAŞ
Ciddiyet: yüksek · Ciddiyetsizlik: daha yüksek
Bu belge hem resmi tutanak hem de şaka tutanağıdır.
------------------------------------------------------------
"""


def sessiz_bagir(mesaj: str) -> None:
    for ch in mesaj:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.012)
    print()


def protokol(istenilen: int, basilan: int) -> None:
    print("=== SESSİZ BAĞIRAN ASANSÖR PROTOKOLÜ ===")
    print(f"Hedef kat     : {istenilen}")
    print(f"Basılan düğme : {basilan}")
    if istenilen == basilan:
        sessiz_bagir("Doğru kat. Evren sessizliğini korudu. Tebrikler, sıradansınız.")
    else:
        ozur = random.choice(OZURLER).format(kat=basilan)
        sessiz_bagir(ozur)
        sessiz_bagir("Asansör ruhu not aldı. Bir daha olursa fısıltı yükselecek.")
    print(DAMGA)


def main() -> None:
    if len(sys.argv) >= 3:
        istenilen = int(sys.argv[1])
        basilan = int(sys.argv[2])
    else:
        istenilen = random.choice(KATLAR)
        basilan = random.choice(KATLAR)
        print("(Argüman yok: rastgele katlar seçildi. Kullanım: python asansor.py HEDEF BASILAN)")
    protokol(istenilen, basilan)


if __name__ == "__main__":
    main()
