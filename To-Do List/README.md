# Yapılacaklar Listesi (To-Do List) Uygulaması

Proje Tanımı:
Bu proje, kullanıcıların görevlerini ekleyebileceği, tamamlayabileceği, silebileceği ve görüntüleyebileceği basit bir yapılacaklar listesi uygulaması sağlamaktadır. Kullanıcı, görevlerini organize etmek ve tamamlamak için çeşitli işlemleri gerçekleştirebilir.

## Kullanılan Sınıflar:

### Task Sınıfı:
- Amaç: Her bir görev için bir nesne oluşturmak. Bu nesne, görev adını ve tamamlanma durumunu saklar.
- Özellikler: 
  - `task_name`: Görevin adı.
  - `is_task_completed`: Görevin tamamlanıp tamamlanmadığını belirten bir boolean değer (varsayılan `False`).
- Metodlar:
  - `__str__`: Görevin adını ve tamamlanma durumunu yazdıran bir metod.

### TaskManager Sınıfı:
- Amaç: Görevleri eklemek, silmek, tamamlamak ve listelemek için kullanılan ana yönetim sınıfıdır.
- Özellikler:
  - `tasks`: Görevlerin listesi. Her görev, `Task` sınıfından bir nesne olarak saklanır.
- Metodlar:
  - `add_task`: Yeni bir görev ekler.
  - `delete_task`: Belirtilen indeks numarasına göre bir görevi siler.
  - `complete_task`: Belirtilen indeks numarasındaki görevi tamamlanmış olarak işaretler.
  - `show_tasks: Tüm görevleri gösterir. Görevlerin tamamlanma durumuna göre listeler.

## Ana İşlevler:
- Görev Ekleme: Yeni bir görev adı girilir ve görev listeye eklenir.
- Görev Gösterme: Eklenen görevler, tamamlanma durumlarına göre görüntülenir.
- Görev Tamamlama: Bir görev tamamlanmış olarak işaretlenir.
- Görev Silme: Listeden bir görev silinir.
- Çıkış: Programdan çıkılır.
