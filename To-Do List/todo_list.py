#Proje Tanımı: 
""" 
Bir yapılacaklar listesi uygulaması oluşturun. Kullanıcı görev ekleyebilir, görevleri tamamlandı olarak işaretleyebilir ve tamamlananları silebilir.

İstenilen Özellikler:
- Görev ekleme.
- Görevleri tamamlama ve tamamlandı olarak işaretleme.
- Görev listesini görüntüleme (tamamlananlar ve tamamlanmayanlar ayrı listelerde tutulabilir).
- Görev silme.
- Verileri bir .txt dosyasına kaydetme ve program çalıştığında yeniden yükleme.
    ! txt yerine json da yapmayı tercih ettim.

Yönerge:
Bir Task (Görev) sınıfı oluşturun. Bu sınıf, görev adı ve tamamlanma durumunu (True/False) saklasın.
Bir TaskManager sınıfı oluşturun. Bu sınıf, görevlerin eklenmesi, silinmesi ve yönetilmesi için gerekli metotları içersin.
"""
import json

class Task:
    def __init__(self, task_name, is_task_completed=False):
        self.task_name = task_name
        self.is_task_completed = is_task_completed

    def __str__(self):
        if self.is_task_completed:
            status = "Tamamlandı"
        else:
            status = "Tamamlanmadı"
        return f"{self.task_name} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append({"name": task_name, "completed": False})
        print(f"Görev eklendi: {task_name}")
    
    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks): 
            task = self.tasks.pop(task_index)
            print(f"Görev silindi: {task['name']}")
        else:
            print("Geçersiz görev numarası")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Görev tamamlandı: {self.tasks[task_index]['name']}")
        else:
            print("Geçersiz görev numarası!")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("Görev yok.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task}")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\n1 - Görevleri göster")
        print("2 - Görev ekle")
        print("3 - Görev sil")
        print("4 - Görev tamamla")
        print("5 - Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            task_manager.show_tasks()

        elif choice == "2":
            task_name = input("Görev adı: ")
            task_manager.add_task(task_name)

        elif choice == "3":
            task_index = input("Silmek istediğiniz görev numarasını: ")
            if task_index.isdigit():
                task_manager.delete_task(int(task_index))
            else:
                print("Geçersiz numara")

        elif choice == "4":
            task_index = input("Tamamlamak istediğiniz görev numarasını: ")
            if task_index.isdigit():
                task_manager.complete_task(int(task_index))
            else:
                print("Geçersiz numara")
        elif choice == "5":
            print("Çıkıldı.")
            break
        else:
            print("Geçersiz seçenek!")