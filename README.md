# GES
Türkiye'nin Haziran ayındaki güneş enerjisi üretim tahminini yapmaya çalıştık.

## GES EDA 

Epiaş Şeffaflık Platformundan Çekilmiş 18 Güneş enerjisi santralinin 2020 Ocak ayından itibaren verilerinin
çok temel özelliklerini inceledim.

## GES Time Series Trial 

Yukarıda bahsedilen verilerin trend mevsimsellik vb özelliklerini incelemeyi hedeflediğim, AR MA ve ARIMA ile 
model oluşturmayu denediğim bir notebook.

## Güneş Üretim Vs Hava Durumu

7 farklı lokasyonun Radyans(Ne kadar Güneş vuruyor verisi) ile Sıcaklık verisinin Türkiye'de en yüksek enerji üretimine sahip santrallerinin üretimleri ile 
korelasyonunun ve santrallerin üretimlerinin kendi aralarındaki korelasyonunu incelediğimiz bir notebook

## Türkiye Haziran Ayı Ges Üretim Tahminleme

Bu klasörde bulunan kodlar kullanılarak Türkiye'nin Haziran ayı enerji üretimine göre tahminleme yapılabilir.

### Ges_Weather_RnR 

Bu kodda incelemek istediğiniz santralin ismini ve tarihi girerek modele hazır hale getirebilirseniz. Veya birden fazla santralleri toplayabilirsiniz.

### Gesler

Bu kod ana kodda kullanılan bütün fonksiyonları içerir

### Upload Data
Veriyi yükleyen kod

### RF
Random Forest ile tahminlemede bulunmak için Grid Search ile parametreleri ayarlayan kod bu klasörde. 
Diğer algoritmalar da bu dosyaya eklenecektir.


### indir

Bu kodu kullanarak Epiaş'dan verileri indirebilirsiniz.
