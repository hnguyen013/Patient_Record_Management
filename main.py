import os

# --- HÀM ĐIỀU KHIỂN CHÍNH (MAIN PROCESS) ---

def main():
    
    while True:
        #display_menu()
        choice = input("Mời bạn chọn chức năng (1-7): ")

        if choice == '1':
            print("\n[Tính năng Tìm kiếm: Sẽ cập nhật ở sau]")
        elif choice == '2':
            print("\n[Tính năng Tìm kiếm: Sẽ cập nhật ở sau]")
        elif choice == '3':
            print("\n[Tính năng Tìm kiếm: Sẽ cập nhật ở sau]")
        elif choice == '4':
            print("\n[Tính năng Tìm kiếm: Sẽ cập nhật ở sau]")
        elif choice == '5':
            print("\n[Tính năng Tìm kiếm: Sẽ cập nhật ở sau]")
        elif choice == '6':
            print("\n[Tính năng Tìm kiếm: Sẽ cập nhật ở sau]")
        elif choice == '7':
            print("Hệ thống đã đóng. Cảm ơn bạn!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 7.")

if __name__ == "__main__":
    main()