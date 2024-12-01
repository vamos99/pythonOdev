class User:
    def __init__(self, user_name, account_number, account_balance):
        self.user_name = user_name
        self.account_number = account_number
        self.account_balance = account_balance


class Bank:
    def __init__(self):
        self.users_list = []

    def create_account(self, user_name, account_number, initial_balance):
        self.users_list.append(User(user_name, account_number, initial_balance))
        print(f"Hesap oluşturuldu: {user_name}, Hesap No: {account_number}, Bakiye: {initial_balance} TL")

    def find_user_by_account_number(self, account_number):
        for user in self.users_list:
            if user.account_number == account_number:
                return user
        return None

    def deposit_money(self, account_number, amount):
        user = self.find_user_by_account_number(account_number)
        if user:
            user.account_balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {user.account_balance} TL")
        else:
            print("Hesap bulunamadı.")

    def withdraw_money(self, account_number, amount):
        user = self.find_user_by_account_number(account_number)
        if user:
            if user.account_balance >= amount:
                user.account_balance -= amount
                print(f"{amount} TL çekildi. Yeni bakiye: {user.account_balance} TL")
            else:
                print("Yetersiz bakiye.")
        else:
            print("Hesap bulunamadı.")

    def check_balance(self, account_number):
        user = self.find_user_by_account_number(account_number)
        if user:
            print(f"Hesap No: {account_number}, Bakiye: {user.account_balance} TL")
        else:
            print("Hesap bulunamadı.")


def main():
    bank = Bank()

    while True:
        print("\n1 - Hesap Oluştur")
        print("2 - Para Yatır")
        print("3 - Para Çek")
        print("4 - Bakiye Sorgula")
        print("5 - Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            name = input("Kullanıcı adı: ")
            acc_num = input("Hesap numarası: ")
            balance = float(input("Başlangıç bakiyesi: "))
            bank.create_account(name, acc_num, balance)

        elif choice == "2":
            acc_num = input("Hesap numarası: ")
            amount = float(input("Yatırılacak tutar: "))
            bank.deposit_money(acc_num, amount)

        elif choice == "3":
            acc_num = input("Hesap numarası: ")
            amount = float(input("Çekilecek tutar: "))
            bank.withdraw_money(acc_num, amount)

        elif choice == "4":
            acc_num = input("Hesap numarası: ")
            bank.check_balance(acc_num)

        elif choice == "5":
            print("Çıkıldı.")
            break

        else:
            print("Geçersiz seçim")
