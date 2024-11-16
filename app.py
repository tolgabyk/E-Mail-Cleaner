import imaplib
import email
from email.header import decode_header
from tkinter import *
from tkinter import messagebox
from datetime import datetime

class EmailCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-posta Temizleyici")
        self.root.geometry("400x350")

        # Giriş Bilgileri
        Label(root, text="E-posta Adresi:").pack(pady=5)
        self.email_entry = Entry(root, width=40)
        self.email_entry.pack()

        Label(root, text="Şifre:").pack(pady=5)
        self.password_entry = Entry(root, width=40, show="*")
        self.password_entry.pack()

        # Giriş Yap Butonu
        Button(root, text="Bağlan", command=self.connect_to_email).pack(pady=10)

        # Filtreleme Seçenekleri
        Label(root, text="Gönderen (opsiyonel):").pack(pady=5)
        self.sender_entry = Entry(root, width=40)
        self.sender_entry.pack()

        Label(root, text="Tarih (örn: 01-Nov-2024):").pack(pady=5)
        self.date_entry = Entry(root, width=40)
        self.date_entry.pack()

        # İşlem Butonları
        Button(root, text="E-postaları Listele", command=self.list_emails).pack(pady=10)
        Button(root, text="Seçilenleri Sil", command=self.delete_emails).pack(pady=5)

        # E-posta Id'leri ve Bağlantı Nesnesi
        self.email_ids = []
        self.mail = None

    def connect_to_email(self):
        """E-posta sunucusuna bağlanır."""
        email_address = self.email_entry.get()
        password = self.password_entry.get()

        try:
            self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
            self.mail.login(email_address, password)
            self.mail.select("inbox")
            messagebox.showinfo("Başarılı", "E-posta bağlantısı kuruldu.")
        except Exception as e:
            messagebox.showerror("Hata", f"Giriş başarısız: {str(e)}")

    def search_emails(self):
        """E-posta filtreleme işlemi yapılır."""
        sender = self.sender_entry.get()
        date = self.date_entry.get()
        search_criteria = []

        if sender:
            search_criteria.append(f'FROM "{sender}"')
        if date:
            try:
                datetime.strptime(date, "%d-%b-%Y")
                search_criteria.append(f'SINCE "{date}"')
            except ValueError:
                messagebox.showerror("Hata", "Tarih formatı hatalı. Örnek format: 01-Nov-2024")
                return []

        search_string = ' '.join(search_criteria) if search_criteria else 'ALL'
        status, messages = self.mail.search(None, search_string)
        self.email_ids = messages[0].split()
        return self.email_ids

    def list_emails(self):
        
        #Filtrelenen e-postaları listeler
        
        self.search_emails()

        if not self.email_ids:
            messagebox.showinfo("Bilgi", "Filtreye uyan e-posta bulunamadı.")
            return

        subjects = []
        for eid in self.email_ids[:10]:  # İlk 10 e-posta başlığını listele
            _, msg = self.mail.fetch(eid, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    subjects.append(subject)

        # Kullanıcıya mesaj göster
        if subjects:
            subject_list = "\n".join(subjects)
            messagebox.showinfo("E-postalar", f"Bulunan E-postalar:\n{subject_list}")
        else:
            messagebox.showinfo("Bilgi", "E-posta başlığı bulunamadı.")

    def delete_emails(self):
        """Filtrelenen e-postaları siler."""
        if not self.email_ids:
            messagebox.showerror("Hata", "Silinecek e-posta bulunamadı.")
            return

        if messagebox.askyesno("Onay", f"{len(self.email_ids)} adet e-posta silinecek. Emin misiniz?"):
            try:
                for eid in self.email_ids:
                    self.mail.store(eid, '+FLAGS', '\\Deleted')
                self.mail.expunge()
                messagebox.showinfo("Başarılı", f"{len(self.email_ids)} adet e-posta silindi.")
            except Exception as e:
                messagebox.showerror("Hata", f"Silme işlemi sırasında hata oluştu: {str(e)}")
        else:
            messagebox.showinfo("İptal", "Silme işlemi iptal edildi.")

if __name__ == "__main__":
    root = Tk()
    app = EmailCleanerApp(root)
    root.mainloop()
