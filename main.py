import os
# --- FUNCTIONS ---
def display_menu():
    print("\n" + "="*45)
    print("      HỆ THỐNG QUẢN LÝ BỆNH ÁN PHÒNG KHÁM")
    print("="*45)
    print("1. Tiếp nhận bệnh nhân mới (Nhập dữ liệu)")
    print("2. Hiển thị danh sách bệnh án (Bảng định dạng)")
    print("3. Tìm kiếm bệnh nhân (Theo ID hoặc Tên)")
    print("4. Sắp xếp danh sách bệnh nhân")
    print("5. Thống kê & Tính toán số liệu")
    print("6. Lưu dữ liệu và xuất báo cáo (.txt)")
    print("7. Thoát chương trình")
    print("-" * 45)

# --- Lựa chọn ---
def main():
    
    while True:
        display_menu()
        choice = input("Mời bạn chọn chức năng (1-7): ")

        if choice == '1':
            print("\n[Tính năng Sẽ cập nhật ở sau]")
        elif choice == '2':
            print("\n[Tính năng Sẽ cập nhật ở sau]")
        elif choice == '3':
            print("\n[Tính năng Sẽ cập nhật ở sau]")
        elif choice == '4':
            print("\n[Tính năng Sẽ cập nhật ở sau]")
        elif choice == '5':
            print("\n[Tính năng Sẽ cập nhật ở sau]")
        elif choice == '6':
            print("\n[Tính năng Sẽ cập nhật ở sau]")
        elif choice == '7':
            print("Hệ thống đã đóng. Cảm ơn bạn!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 7.")

if __name__ == "__main__":
    main()