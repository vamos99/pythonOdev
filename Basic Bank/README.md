Banka Sistemi Uygulaması

Proje Tanımı:
Bu proje, bir banka sistemi simülasyonu sağlar. Kullanıcılar hesap açabilir, para yatırabilir, para çekebilir ve bakiye sorgulaması yapabilirler.

Kullanılan Sınıflar:

User Sınıfı:

	•	Amaç: Kullanıcı bilgilerini saklar.
	•	Özellikler:
	•	user_name: Kullanıcının adı.
	•	account_number: Hesap numarası (her kullanıcı için benzersiz).
	•	account_balance: Hesap bakiyesi (başlangıç bakiyesi).

Bank Sınıfı:

	•	Amaç: Banka işlemlerini yönetir.
	•	Özellikler:
	•	users_list: Kullanıcıların listesi.
	•	Metodlar:
	•	create_account: Yeni bir hesap oluşturur.
	•	find_user_by_account_number: Hesap numarasına göre kullanıcıyı bulur.
	•	deposit_money: Kullanıcının hesabına para yatırır.
	•	withdraw_money: Kullanıcının hesabından para çeker.
	•	check_balance: Hesap bakiyesini sorgular.

Ana İşlevler:

	•	Hesap Oluşturma: Yeni bir kullanıcı hesabı oluşturulur (kullanıcı adı, hesap numarası ve başlangıç bakiyesi ile).
	•	Para Yatırma: Belirli bir hesaba para yatırılabilir.
	•	Para Çekme: Kullanıcı hesabından para çekilebilir (bakiye kontrolü yapılır).
	•	Bakiye Sorgulama: Hesap bakiyesi sorgulanabilir.
	•	Çıkış: Programdan çıkılır.
