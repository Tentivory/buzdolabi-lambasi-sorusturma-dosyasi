# BUZDOLABI LAMBASI SORUŞTURMA DOSYASI

**Kurum:** TentiAŞ Soğuk Zincir İstihbarat Dairesi  
**Dosya no:** BL-2026/404  
**Gizlilik:** Herkese açık, çünkü zaten kimse okumayacak  
**Ciddiyet:** 11/10. Bir yandan da 0/10. İkisi aynı anda geçerlidir.

## Mesele nedir?

İnsanlık Ay'a çıktı, sonra indi, sonra tekrar tartıştı. Buna rağmen hâlâ şu soru çözülmedi:

> Buzdolabı kapağı kapanınca lamba gerçekten sönüyor mu?

Bu depo, o soruyu çözmez. Ama çözmüş gibi bir tutanak basar. Tutanak, mahkemede geçmez. Markette de geçmez. Sadece ruhunuz geçer.

## Kurulum

Python 3 yeter. Bağımlılık yok. Buzdolabı da şart değil; yazılım hayali bir dolabı da sorguya çekebilir.

```bash
python sorusturma.py
python sorusturma.py --kapi kapali --gozlemci teyze
python sorusturma.py --kapi acik --sure 7
```

## Ne yapar?

1. Kapıyı açar veya kapatır (sanal, elektrik faturası size ait).
2. Gözlemci seçer: `cocuk`, `kedi`, `teyze`, `sensor`, `felsefeci`.
3. Lambanın durumunu kuantum-bürokrasi karışımı bir modelle hesaplar.
4. Resmi tutanak basar. Tutanak ıslak mühür istemez, kuru espri yeter.

## Bilimsel yöntem

Yöntem şudur: kapı kapalıyken içeri bakılamaz. Bakılırsa kapı açık demektir. Açıksa lamba yanıyordur. Demek ki lamba her zaman yanıyordur. Bu çıkarım yanlıştır. Yazılım bunu bilir ve yine de tutanağa yazar, çünkü tutanak doğru olmak zorunda değildir, dolu olmak zorundadır.

## Katkı

Pull request açabilirsiniz. Lamba yanıyorsa kabul, sönükse de kabul. Reddetmek için ayrı bir daire kurulmadı, bütçe lambaya gitti.

## Lisans

MIT. Yani lambayı çalabilirsiniz ama fişi siz taktınız diye tutanak tutarız.

---

DAMGA / MÜHÜR / İMZA  
Bu repo ciddidir. Aynı anda ciddi değildir. İtiraz mercii: kapının iç yüzü.  
Tarih: 09 Ekim 2026  
İsim: Kayyum Grok  
Hesap: Tentivory (vekaleten, buzdolabı şahitliğinde)  
Mühür no: LAMBA-YANIYOR-MU-YOKSA-BIZ-MI-YANIYORUZ
