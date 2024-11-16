# E-Mail-Cleaner

Bu uygulama, kullanıcıların Gmail hesaplarına bağlanarak belirli kriterlere göre (tarih veya gönderen kişi) istenmeyen e-postaları toplu olarak silmelerini sağlar. Python kullanılarak geliştirilen bu uygulama, kullanıcı dostu bir GUI arayüzüne sahiptir.

## 🚀 Özellikler
- **🔒 Güvenli IMAP Bağlantısı:** Gmail hesabınıza güvenli bir şekilde bağlanır.
- **🔍 Filtreleme:** Gönderen adresi veya belirli bir tarihe göre e-postaları filtreler.
- **📄 Listeleme:** Filtrelenen e-postaların başlıklarını görüntüler.
- **🗑️ Toplu Silme:** Filtrelenen e-postaları kullanıcı onayı aldıktan sonra toplu olarak silebilir.

## 🛠️ Gereksinimler
- Python 3.x
- Gmail hesabı
- Aşağıdaki Python kütüphaneleri:
  - **imaplib** (Standart kütüphane)
  - **email** (Standart kütüphane)
  - **tkinter** (Standart kütüphane)
  - **datetime** (Standart kütüphane)

## Önemli

Google, güvenlik nedeniyle doğrudan şifre kullanımını engeller. Bu sorunu çözmek için aşağıdaki adımları izleyin:

1. IMAP Erişimini Açın
- Gmail hesabınıza giriş yapın.
- Ayarlar > Tüm Ayarları Görüntüle > Yönlendirme ve POP/IMAP sekmesine gidin.
- IMAP erişimi etkinleştir seçeneğini seçin ve kaydedin.
  
2. Uygulama Şifresi Oluşturun
- Google hesabınızda 2 Adımlı Doğrulama etkin değilse etkinleştirmeniz gerekir.
- Google Hesap Güvenliği sayfasına gidin.
- Uygulama Şifreleri kısmından yeni bir şifre oluşturun ve bunu kullanın.
