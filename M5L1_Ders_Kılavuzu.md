# 🎨 Modül 5, Ders 1: İlk Web Uygulamanız - Streamlit'e Merhaba!

---

### 📊 **Dersin Künyesi ve Hedefleri**

🚀 **Ders Amaçları**

- **Tanıtım:** Öğrencileri, Python ile hızlı ve kolay bir şekilde web uygulamaları oluşturmayı sağlayan Streamlit kütüphanesiyle tanıştırmak.
- **Temel Kavramlar:** `st.write`, `st.title` gibi temel Streamlit komutlarını ve widget (bileşen) kavramını öğretmek.
- **Etkileşim:** Kullanıcıdan veri alıp (`st.text_input`) bu veriye göre dinamik tepkiler veren (`st.button`) interaktif bir uygulama pratiği yaptırmak.
- **Uygulama:** Teorik bilgileri, "Dijital Oyun Stüdyosu" portalı gibi eğlenceli ve somut bir proje üzerinden uygulamaya dökmek.

✅ **Öğrenim Çıktıları (Dersin Ardından Öğrenci...)**

- `streamlit` kütüphanesini `pip` kullanarak kurabilecek.
- Bir Streamlit uygulamasını terminalden `streamlit run` komutuyla çalıştırabilecek.
- `st.title`, `st.header`, ve `st.write` komutları ile metin hiyerarşisi oluşturabilecek.
- `st.success`, `st.info`, `st.warning`, ve `st.error` komutları ile farklı türde bildirimler gösterebilecek.
- `st.text_input` ile kullanıcıdan metin verisi alabilecek ve `st.button` ile bir eylemi tetikleyebilecek.

🔗 **Materyaller ve Bağlantılar**

- **Gerekli Yazılımlar:** Visual Studio Code, Python 3.x
- **Kütüphaneler:** `streamlit`

### 👩‍🏫 **DERS AKIŞI ZAMAN ÇİZELGESİ**

| Aşama No | Konu | Tahmini Süre | Aşama Türü | Açıklama |
| --- | --- | --- | --- | --- |
| **1** | Giriş ve Merhaba Dünya! | 15 dk | ANLATIM & DEMO | Önceki dersin tekrarı, Streamlit'e giriş, kurulum ve `st.balloons()` ile ilk "vay be!" anı. |
| **2** | Stüdyo Tabelasını Asıyoruz | 15 dk | PRATİK | Temel metin komutları (`title`, `header`, `write`) ile sayfa yapısı oluşturma. |
| **3** | Geliştirme Günlüğü | 20 dk | PRATİK | Renkli bildirim kutuları ile dinamik ve görsel bilgi sunumu. |
| **4** | Hayran Girişi | 25 dk | PRATİK | `text_input` ve `button` ile kullanıcı etkileşimi sağlama. |
| **5** | Değerlendirme ve odev | 15 dk | ETKİNLİK | Dersin özeti, soru-cevap, odevlendirme ve sonraki derse hazırlık. |

---
### 🧩 **ADIM ADIM İŞLEYİŞ VE NOTLAR**

### **Aşama 1: Giriş ve Merhaba Dünya!** (15 Dakika)

#### **1. Önceki Dersin Tekrarı (Recap)**
- **Öğretmen Notu:** Öğrencilere Modül 4'te ne öğrendiklerini sorun. Cevapların `SQLite`, `veritabanı`, `veri kaydetme`, `SQL sorguları` gibi anahtar kelimeler etrafında dönmesini sağlayın.
- **Diyalog Örneği:** "Arkadaşlar, geçen dersimizde bilgilerimizi nasıl kalıcı olarak bir 'kasaya', yani veritabanına kaydettiğimizi öğrendik. Peki, bu kasadaki bilgileri sadece biz mi bileceğiz? Elbette hayır! Şimdi o bilgileri tüm dünyaya sergileme zamanı!"

#### **2. Bu Dersin Konusu**
- **Konu:** Bugün, yazdığımız Python kodlarını tek bir komutla çalışan, interaktif web sitelerine dönüştürmemizi sağlayan **Streamlit** kütüphanesini tanıyacağız. Kendi dijital oyun stüdyomuzun tanıtım sayfasını yaparak başlayacağız.

#### **3. Kurulum**
- Tüm sihirli güçleri kullanabilmek için önce Streamlit'i kurmamız gerekiyor. Terminali açın ve şu komutu çalıştırın:
  ```bash
  pip install streamlit
  ```

#### **4. İlk Sihir: `st.balloons()`**
- **Öğretmen Notu:** Öğrencilere hemen bir sonuç göstermek için bu adımı kullanın.
- **Aksiyon:** `M5L1/1` klasörü içindeki `app.py` dosyasının içeriği aşağıdaki gibidir. Bu aşamada taslak dosyası kullanmıyoruz, doğrudan kodu vererek hızlı bir başlangıç yapıyoruz.

- **Kod (`M5L1/1/app.py`):**
  ```python
  # Terminalde çalıştırmanız gereken komutlar:
  #
  # 1. Streamlit kütüphanesini kurmak için (eğer daha önce kurmadıysanız):
  #    pip install streamlit
  #
  # 2. Bu uygulamayı çalıştırmak için bu dosyanın olduğu ana dizindeyken:
  #    streamlit run M5L1/1/app.py

  import streamlit as st

  # Bu basit komut, ekranınıza eğlenceli bir animasyon getirecek.
  st.balloons()
  st.write("Streamlit'e Hoş Geldiniz!")
  ```
- **Çalıştırma:** Terminalde aşağıdaki komutu çalıştırın ve tarayıcıda açılan sihirli sonucu görün!
  ```bash
  streamlit run M5L1/1/app.py
  ```

---

### **Aşama 2: Stüdyo Tabelasını Asıyoruz** (15 Dakika)

#### **Konsept**
- Her stüdyonun bir adı ve vizyonu vardır. Şimdi `st.title`, `st.header` ve `st.write` komutlarıyla sayfamıza kurumsal bir kimlik kazandıracağız.

#### **Aksiyon**
- `M5L1/2/app.py` dosyasını açın ve yorum satırlarındaki görevleri tamamlayarak stüdyonuzun tabelasını asın!

- **Taslak Kod (`M5L1/2/app.py`):**
  ```python
  import streamlit as st

  # st.title() kullanarak stüdyonuza bir isim verin.
  st.title("Pixel-Perfect Oyun Stüdyosu")

  # Şimdi st.header() kullanarak "Vizyonumuz" adında bir alt başlık ekleyin.
  # KODUNUZU AŞAĞIYA YAZIN


  # Son olarak, st.write() ve üç tırnak (""") kullanarak stüdyonuzun vizyonunu anlatan
  # çok satırlı bir metin ekleyin.
  # KODUNUZU AŞAĞIYA YAZIN
  ```

#### **Çözüm Kodu (Öğretmen Referansı İçin)**
  ```python
  import streamlit as st

  # st.title() kullanarak stüdyonuza bir isim verin.
  st.title("Pixel-Perfect Oyun Stüdyosu")

  # Şimdi st.header() kullanarak "Vizyonumuz" adında bir alt başlık ekleyin.
  st.header("Vizyonumuz")


  # Son olarak, st.write() ve üç tırnak (""") kullanarak stüdyonuzun vizyonunu anlatan
  # çok satırlı bir metin ekleyin.
  st.write("""
  Biz Pixel-Perfect olarak, her bir pikselin bir hikaye anlattığına inanıyoruz.
  Amacımız, unutulmaz karakterler ve sürükleyici dünyalar yaratarak oyunculara
  sadece bir oyun değil, bir macera sunmaktır.
  """)
  ```

---

### **Aşama 3: Geliştirme Günlüğü** (20 Dakika)

#### **Konsept**
- Sayfamıza renk ve hayat katıyoruz! `st.success`, `st.info`, `st.warning`, `st.error` gibi renkli bildirim kutularıyla stüdyodaki son gelişmeler hakkında ziyaretçileri bilgilendireceğiz.

#### **Aksiyon ve Öğrenci Görevi**
- `M5L1/3/app.py` dosyasını açın ve geliştirme günlüğünüzü oluşturun. Bu aşamada sizden kendi oyun projeniz için bir uyarı ve hata mesajı eklemenizi de istiyoruz!

- **Taslak Kod (`M5L1/3/app.py`):**
  ```python
  import streamlit as st

  # --- Önceki Aşamadan Gelen Kodlar ---
  st.title("Pixel-Perfect Oyun Stüdyosu")
  st.header("Vizyonumuz")
  st.write("""
  Biz Pixel-Perfect olarak, her bir pikselin bir hikaye anlattığına inanıyoruz.
  Amacımız, unutulmaz karakterler ve sürükleyici dünyalar yaratarak oyunculara
  sadece bir oyun değil, bir macera sunmaktır.
  """)
  # ------------------------------------

  # "Geliştirme Günlüğü" adında yeni bir alt başlık (header) ekleyin.
  # KODUNUZU AŞAĞIYA YAZIN


  # Aşağıdaki bilgileri uygun durum kutularıyla (success, info) gösterin:
  # 1. Olumlu Gelişme: "Proje 'Ejderha Macerası': Ana karakterin çizimleri tamamlandı!"
  # KODUNUZU AŞAĞIYA YAZIN

  # 2. Bilgilendirme: "Oyun motorumuz Godot'un son sürümüne güncelleniyor."
  # KODUNUZU AŞAĞIYA YAZIN


  # ÖĞRENCİ GÖREVİ:
  # Kendi hayali oyun projenizle ilgili bir "uyarı" (warning) ve bir de "hata" (error) mesajı ekleyin.
  # Yaratıcılığınızı kullanın!
  # KODUNUZU AŞAĞIYA YAZIN
  ```

#### **Çözüm Kodu (Öğretmen Referansı İçin)**
  ```python
  import streamlit as st

  # --- Önceki Aşamadan Gelen Kodlar ---
  st.title("Pixel-Perfect Oyun Stüdyosu")
  st.header("Vizyonumuz")
  st.write("""
  Biz Pixel-Perfect olarak, her bir pikselin bir hikaye anlattığına inanıyoruz.
  Amacımız, unutulmaz karakterler ve sürükleyici dünyalar yaratarak oyunculara
  sadece bir oyun değil, bir macera sunmaktır.
  """)
  # ------------------------------------

  # "Geliştirme Günlüğü" adında yeni bir alt başlık (header) ekleyin.
  st.header("Geliştirme Günlüğü")


  # Aşağıdaki bilgileri uygun durum kutularıyla (success, info) gösterin:
  # 1. Olumlu Gelişme: "Proje 'Ejderha Macerası': Ana karakterin çizimleri tamamlandı!"
  st.success("Proje 'Ejderha Macerası': Ana karakterin çizimleri tamamlandı!")

  # 2. Bilgilendirme: "Oyun motorumuz Godot'un son sürümüne güncelleniyor."
  st.info("Oyun motorumuz Godot'un son sürümüne güncelleniyor.")


  # ÖĞRENCİ GÖREVİ:
  # Kendi hayali oyun projenizle ilgili bir "uyarı" (warning) ve bir de "hata" (error) mesajı ekleyin.
  # Yaratıcılığınızı kullanın!
  st.warning("Proje 'Siber Şehir': Karakter modellemelerinde optimizasyon gerekiyor.")
  st.error("Proje 'Kayıp Hazine': Bölüm 3 haritası yüklenemiyor!")
  ```

---

### **Aşama 4: Hayran Girişi** (25 Dakika)

#### **Konsept**
- Geldik en heyecanlı kısma: etkileşim! `st.text_input` ile kullanıcıdan veri alacak ve `st.button` ile bu veriye göre bir tepki üreteceğiz.

#### **Aksiyon ve Öğrenci Görevi**
- `M5L1/4/app.py` dosyasını açarak dersin final uygulamasını tamamlayın. Bu seferki göreviniz, özel bir misafire özel bir karşılama hazırlamak!

- **Taslak Kod (`M5L1/4/app.py`):**
  ```python
  import streamlit as st

  # --- Önceki Aşamadan Gelen Kodlar ---
  st.title("Pixel-Perfect Oyun Stüdyosu")
  st.header("Vizyonumuz")
  st.write("""
  Biz Pixel-Perfect olarak, her bir pikselin bir hikaye anlattığına inanıyoruz.
  Amacımız, unutulmaz karakterler ve sürükleyici dünyalar yaratarak oyunculara
  sadece bir oyun değil, bir macera sunmaktır.
  """)
  st.header("Geliştirme Günlüğü")
  st.success("Proje 'Ejderha Macerası': Ana karakterin çizimleri tamamlandı!")
  st.info("Oyun motorumuz Godot'un son sürümüne güncelleniyor.")
  st.warning("Proje 'Uzay Fırtınası': Ses efektlerinde hafif bir gecikme yaşanabilir.")
  st.error("ACİL: Bölüm 2'deki devasa BUG nedeniyle sunucular kapatıldı. Ekip tamir üzerinde çalışıyor!")
  # ------------------------------------

  # "Stüdyo Kayıt Masası" adında yeni bir alt başlık (header) ekleyin.
  # KODUNUZU AŞAĞIYA YAZIN


  # Kullanıcıdan ismini girmesini isteyecek bir metin giriş kutusu (text_input) oluşturun.
  # Girilen ismi bir değişkende saklayın (örneğin: 'isim').
  # KODUNUZU AŞAĞIYA YAZIN


  # "Kayıt Ol" metni içeren bir buton (button) oluşturun.
  # Bu butona tıklandığında çalışacak bir if bloğu açın.
  # KODUNUZU AŞAĞIYA YAZIN
      # if bloğunun içinde, kullanıcının bir isim girip girmediğini kontrol edin.
      # Eğer bir isim girdiyse:
      #   - Girdiği ismi kullanarak bir tebrik mesajı yazdırın (st.write).
      #   - st.balloons() ile kutlama yapın.
      # Eğer isim girmemişse:
      #   - "Lütfen bir isim girerek kayıt ol." mesajını yazdırın.
      # KODUNUZU AŞAĞIYA YAZIN


  # ÖĞRENCİ GÖREVİ (İsteğe Bağlı):
  # if bloğunun içini öyle bir güncelleyin ki, eğer girilen isim "Gandalf" ise,
  # "Büyücüler kayıt olamaz!" diye özel bir mesaj çıksın ve st.snow() ile kar yağsın.
  ```

#### **Çözüm Kodu (Öğretmen Referansı İçin)**
  ```python
  import streamlit as st

  # --- Önceki Aşamadan Gelen Kodlar ---
  st.title("Pixel-Perfect Oyun Stüdyosu")
  st.header("Vizyonumuz")
  st.write("""
  Biz Pixel-Perfect olarak, her bir pikselin bir hikaye anlattığına inanıyoruz.
  Amacımız, unutulmaz karakterler ve sürükleyici dünyalar yaratarak oyunculara
  sadece bir oyun değil, bir macera sunmaktır.
  """)
  st.header("Geliştirme Günlüğü")
  st.success("Proje 'Ejderha Macerası': Ana karakterin çizimleri tamamlandı!")
  st.info("Oyun motorumuz Godot'un son sürümüne güncelleniyor.")
  st.warning("Proje 'Uzay Fırtınası': Ses efektlerinde hafif bir gecikme yaşanabilir.")
  st.error("ACİL: Bölüm 2'deki devasa BUG nedeniyle sunucular kapatıldı. Ekip tamir üzerinde çalışıyor!")
  # ------------------------------------

  # "Stüdyo Kayıt Masası" adında yeni bir alt başlık (header) ekleyin.
  st.header("Stüdyo Kayıt Masası")


  # Kullanıcıdan ismini girmesini isteyecek bir metin giriş kutusu (text_input) oluşturun.
  # Girilen ismi bir değişkende saklayın (örneğin: 'isim').
  isim = st.text_input("Lütfen isminizi girin:")


  # "Kayıt Ol" metni içeren bir buton (button) oluşturun.
  # Bu butona tıklandığında çalışacak bir if bloğu açın.
  if st.button("Kayıt Ol"):
      # if bloğunun içinde, kullanıcının bir isim girip girmediğini kontrol edin.
      if isim:
          # ÖĞRENCİ GÖREVİ (İsteğe Bağlı):
          # if bloğunun içini öyle bir güncelleyin ki, eğer girilen isim "Gandalf" ise,
          # "Büyücüler kayıt olamaz!" diye özel bir mesaj çıksın ve st.snow() ile kar yağsın.
          if isim.lower() == "gandalf":
              st.write("Büyücüler bu diyarlarda kayıt olamaz!")
              st.snow()
          else:
              # Girdiği ismi kullanarak bir tebrik mesajı yazdırın (st.write).
              st.write(f"Tebrikler **{isim}**, sen artık bu stüdyonun **Kıdemli Test Oyuncususun!**")
              # st.balloons() ile kutlama yapın.
              st.balloons()
      else:
          # "Lütfen bir isim girerek kayıt ol." mesajını yazdırın.
          st.write("Lütfen bir isim girerek kayıt ol.")
  ```

---

### **Aşama 5: Değerlendirme ve odev** (15 Dakika)

#### **1. Dersin Özeti ve Tekrar**
- **Öğretmen Notu:** Öğrencilerle birlikte dersin üzerinden geçin. Ana komutları (`st.title`, `st.write`, `st.success`, `st.text_input`, `st.button`) tahtaya yazarak veya tekrar ettirerek pekiştirin.
- **Diyalog Örneği:** "Bugün harika bir iş çıkardık! Sıfırdan bir Python dosyasıyla başlayıp, çalışan, etkileşimli bir web uygulaması yaptık. `st.title` ile başlık attık, `st.info` gibi kutularla renk kattık ve `st.button` ile sitemizi konuşturan bir hale getirdik."

#### **2. Soru-Cevap ve Pekiştirme**
- "Aklınıza takılan bir yer var mı?"
- "Bir `st.success` mesajını nasıl `st.error`'a çeviririz?"
- "`st.button`'a basıldığını kodumuzda nasıl anlıyorduk? Hangi yapıyı kullanıyorduk?" (Cevap: `if` bloğu)
- "Kullanıcıdan metin almak için hangi komutu kullandık?" (Cevap: `st.text_input`)

#### **3. odev: Sihirli Selamlama**
- **odevin Amacı:** Dersin temel etkileşim komutları olan `st.text_input` ve `st.button` kullanımını pekiştirmek.
- **Senaryo:** "Uygulamamıza sihirli bir dokunuş katıyoruz! Uygulama, bize ismimizi soracak ve sonra bizi sihirli bir şekilde selamlayacak."
- **Aksiyon:** `M5L1/odev` klasöründeki `app.py` dosyasını açın ve yorum satırlarındaki görevleri tamamlayın.

- **Taslak Kod (`M5L1/odev/app.py`):**
  ```python
  # M5L1 - odev: Sihirli Selamlama
  # Öğrenci Görevi:
  # Bu ödevde, kullanıcıdan ismini alıp ona özel bir selamlama mesajı gösteren
  # basit bir web uygulaması yapacaksınız.
  #
  # Yapılacaklar:
  # 1. "Sihirli Selamlama" adında bir ana başlık oluşturun.
  # 2. Kullanıcıdan ismini girmesini isteyen bir metin kutusu ekleyin.
  # 3. "Selamla" adında bir buton koyun.
  # 4. Butona basıldığında, ekrana "Merhaba, [Kullanıcının Girdiği İsim]!" gibi bir
  #    mesaj basın. st.success() kullanarak mesajı daha havalı hale getirebilirsiniz.

  import streamlit as st

  # --- ÇÖZÜM ALANI ---

  # GÖREV 1: st.title() ile başlığı "Sihirli Selamlama" yapın.


  # GÖREV 2: st.text_input() ile kullanıcıdan ismini alın ve bir değişkene atayın.


  # GÖREV 3: st.button() kullanarak "Selamla" adında bir buton oluşturun
  # ve bir if bloğu içine alın.
  # if st.button("..."):

      # GÖREV 4: if bloğunun içinde, kullanıcıya özel selamlama mesajını
      # st.success() ile ekrana yazdırın.
      # İpucu: f-string kullanabilirsiniz! f"Merhaba, {isim}!"


  # --- ÇÖZÜM ALANI BİTİŞ ---
  ```

- **Çözüm Kodu (Öğretmen Referansı İçin):**
  ```python
  # M5L1 - odev: Sihirli Selamlama - ÇÖZÜM
  import streamlit as st

  # GÖREV 1: st.title() ile başlığı "Sihirli Selamlama" yapın.
  st.title("Sihirli Selamlama")

  # GÖREV 2: st.text_input() ile kullanıcıdan ismini alın ve bir değişkene atayın.
  isim = st.text_input("Lütfen isminizi girin:")

  # GÖREV 3: st.button() kullanarak "Selamla" adında bir buton oluşturun
  # ve bir if bloğu içine alın.
  if st.button("Selamla"):

      # GÖREV 4: if bloğunun içinde, kullanıcıya özel selamlama mesajını
      # st.success() ile ekrana yazdırın.
      if isim:
          st.success(f"Merhaba, {isim}! Streamlit dünyasına hoş geldin!")
          st.balloons()
      else:
          st.warning("Lütfen bir isim girmeyi unutma!")
  ```

#### **4. Gelecek Dersin Konusu**
- "Harika bir başlangıç yaptık! Gelecek dersimizde Streamlit'te resimler, videolar gibi medya dosyalarını nasıl kullanacağımızı ve `st.columns`, `st.sidebar` gibi komutlarla sayfa düzenini nasıl daha profesyonel bir hale getireceğimizi öğreneceğiz."