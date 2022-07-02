Öncelikle Flight Api'ye hoş geldiniz! Burada dökümanlarımıza ulaşmak için swagger entegrasyonu yapılmıştır.

Projeyi ayağa kaldırmak için en dış klasördeyken "docker compose up --build" komutu kullanılabilir. Burada ayağa kaldırdıktan sonra http://127.0.0.1:8000/tr/swagger/ aracılığıyla apilere erişim sağlanabilir.

Admin paneline erişim için http://127.0.0.1:8000/tr/admin/ sayfası kullanılabilir. Jazzmin entegre edilmiştir. Burada kullanıcı oluşturmak için proje ayaktayken python3 manage.py createsuperuser aracılığıyla super kullanıcı üretilebilir.

Projemizde airport ve flight olmak üzere iki ana başlık bulunmaktadır. Bunlara modelviewsetlerle erişim sağlanıyor. Aynı zamanda uçuş numarasına göre toplam getirilen uçuş sayısına da erişim sağlanabilir.