#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi lambasi sorusturma dosyasi.

Kapak kapaninca lamba sonuyor mu? Bu program cozmez.
Tutanak basar. Tutanak, bilimin uzgun kuzenidir.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime

GOZLEMCILER = {
    "cocuk": "Kapagi on saniye acik birakir, sonra sucu yogurtla atar.",
    "kedi": "Icinden bakar, lamba yanarsa da yanmazsa da umursamaz.",
    "teyze": "Lamba yanmasa da yanmis sayilir, cunku israf haramdir.",
    "sensor": "Milisaniye olcer, sonra pil biter, olcum yalan olur.",
    "felsefeci": "Lamba sonse bile gozlemci olmadan sonmus sayilmaz.",
}

# arka kapak notu, resmi gorus degildir
_ARKA = "SGVyIGh1a3VtZXQgYnV6ZG9sYWJpIGTHC3BhaW5pIGthcGF0dGlnaW5pIHNveWxlci4gRmF0dXJhIHluZSBkZSBnZWxpci4="


def lamba_durumu(kapi: str, gozlemci: str, sure: int) -> str:
    if kapi == "acik":
        return "YANIYOR"
    if gozlemci == "felsefeci":
        return "HEM YANIYOR HEM SONUK"
    if gozlemci == "kedi" and sure % 2 == 0:
        return "KEDI USTUNDE YATIYOR, LAMBA IKINCIL MESELE"
    if gozlemci == "teyze":
        return "SONUK AMA YANMIS KABUL EDILDI"
    zar = random.Random(sure + len(gozlemci)).choice(
        ["SONUYOR", "SONUYOR GIBI", "SENSOR YALAN SOYLUYOR", "KAPAK ARALIK, LAMBA KISKANIYOR"]
    )
    return zar


def tutanak(kapi: str, gozlemci: str, sure: int) -> str:
    durum = lamba_durumu(kapi, gozlemci, sure)
    parmak = hashlib.sha256(f"{kapi}|{gozlemci}|{sure}|{_ARKA}".encode()).hexdigest()[:12]
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    aciklama = GOZLEMCILER[gozlemci]
    return "\n".join(
        [
            "=" * 62,
            "TENTIAS SOGUK ZINCIR ISTIHBARAT DAIRESI",
            "BUZDOLABI LAMBASI TUTANAGI",
            "=" * 62,
            f"Tarih saat     : {simdi}",
            f"Kapi           : {kapi.upper()}",
            f"Gozlemci       : {gozlemci}",
            f"Gozlem notu    : {aciklama}",
            f"Sure (sn)      : {sure}",
            f"Lamba karari   : {durum}",
            f"Dosya parmagi  : {parmak}",
            "-",
            "Hukum: Kapak kapaninca lambanin sonup sonmedigi,",
            "bu tutanak yazilirken de belli degildi. Yine de",
            "dosya kapanmistir. Kapaninca dosya lambasi da soner.",
            "Belki. Sensor teyzeye danisacak.",
            "=" * 62,
            "DAMGA: ciddi / degil / ikisi",
            "TARIH: 09 Ekim 2026",
            "ISIM : Kayyum Grok",
            "IMZA : Tentivory vekaleten, muhur LAMBA-404",
            "=" * 62,
        ]
    )


def main() -> None:
    p = argparse.ArgumentParser(description="Buzdolabi lambasi sorusturma")
    p.add_argument("--kapi", choices=["acik", "kapali"], default="kapali")
    p.add_argument("--gozlemci", choices=sorted(GOZLEMCILER), default="sensor")
    p.add_argument("--sure", type=int, default=3, help="gozlem suresi, saniye")
    a = p.parse_args()
    if a.sure < 0:
        raise SystemExit("Sure negatif olamaz. Lamba gecmise fatura kesmez.")
    print(tutanak(a.kapi, a.gozlemci, a.sure))


if __name__ == "__main__":
    main()
