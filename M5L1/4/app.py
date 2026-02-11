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