class Kutuphane:
    def _init_(self):
        self.dosya = open("kitaplar.txt", "a+")

    def _del_(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0)
        satirlar = self.dosya.readlines()
        for satir in satirlar:
            kitap_bilgisi = satir.strip().split(',')
            print(f"Kitap: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}")

    def kitap_ekle(self):
        ad = input("Kitabın adını girin: ")
        yazar = input("Kitabın yazarını girin: ")
        yayin_yili = input("Kitabın ilk yayın yılını girin: ")
        sayfa_sayisi = input("Kitabın sayfa sayısını girin: ")
        kitap_bilgisi = f"{ad},{yazar},{yayin_yili},{sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitap başarıyla eklendi.")

    def kitap_sil(self):
        ad = input("Silmek istediğiniz kitabın adını girin: ")
        self.dosya.seek(0)
        satirlar = self.dosya.readlines()
        guncellenmis_satirlar = []
        for satir in satirlar:
            if ad not in satir:
                guncellenmis_satirlar.append(satir)
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(guncellenmis_satirlar)
        print("Kitap başarıyla silindi.")

lib = Kutuphane()

while True:
    print("* MENÜ *")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldır")
    print("4) Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        lib.kitaplari_listele()
    elif secim == '2':
        lib.kitap_ekle()
    elif secim == '3':
        lib.kitap_sil()
    elif secim == '4':
        print("Programdan çıkılıyor.")
        break
    else:
         print("Geçersiz seçim.Lütfen geçerli bir seçenek giriniz.")