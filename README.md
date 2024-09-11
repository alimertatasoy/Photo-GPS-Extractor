# EXIF Data Viewer

Bu Python uygulaması, bir görsel dosyasının EXIF verilerini okuyarak GPS bilgilerini gösteren basit bir GUI (grafiksel kullanıcı arayüzü) sağlar. Tkinter kütüphanesi kullanılarak geliştirilmiştir ve Pillow kütüphanesi kullanılarak görsel dosyalarının EXIF verileri alınır.

## Özellikler

- Görsel dosyalarını yükleyebilir.
- EXIF verilerini ve özellikle GPS bilgilerini gösterir.
- GPS koordinatlarını (enlem ve boylam) ekranda görüntüler.

## Gereksinimler

- Python 3.x
- Pillow (PIL) kütüphanesi
- Tkinter kütüphanesi (Python ile birlikte gelir)

## Kurulum

1. Python ve gerekli kütüphaneleri yükleyin:
    ```bash
    pip install pillow
    ```

2. `exif_viewer.py` dosyasını indirin.

## Kullanım

1. Uygulamayı çalıştırın:
    ```bash
    python exif_viewer.py
    ```

2. **"Yükle"** düğmesine tıklayarak bir görsel dosyası seçin.

3. Seçilen görselin EXIF verileri ve varsa GPS bilgileri ekranda görüntülenir.

4. GPS bilgileri ekranda gösterilecektir.

## Kod Açıklamaları

- **`get_exif_data(image_path)`**: Verilen dosya yolundaki görselin EXIF verilerini alır.
- **`get_lat_lon(exif_data)`**: EXIF verilerinden GPS bilgilerini ayrıştırır ve enlem ile boylamı hesaplar.
- **`convert_to_degrees(value)`**: GPS koordinatlarını derece cinsinden dönüştürür.
- **`upload_file()`**: Kullanıcıdan bir dosya seçmesini sağlar ve EXIF verilerini gösterir.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

## Katkıda Bulunanlar

- [Sizin İsminiz] - Proje sahibi ve geliştirici

