import os
# --- UTILITY FUNCTIONS ---
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
def load_from_file(filename="patients.txt"):
    patient_list = []
    if not os.path.exists(filename):
        return patient_list
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    patient = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": int(parts[2]),
                        "diagnosis": parts[3]
                    }
                    patient_list.append(patient)
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    return patient_list

# ----- CORE FUNCTIONS -----
def add_patient(patient_list):
    print("\n--- NHẬP THÔNG TIN BỆNH NHÂN MỚI ---")
    while True:
        p_id = input("Nhập ID bệnh nhân: ").strip()
        if any(p['id'] == p_id for p in patient_list):
            print("Lỗi: ID này đã tồn tại trong hệ thống!")
        elif not p_id:
            print("Lỗi: ID không được để trống!")
        else:
            break
    name = input("Nhập Họ và Tên: ").strip()
    while True:
        try:
            age = int(input("Nhập tuổi: "))
            if 0 < age < 150: break
            else: print("Lỗi: Tuổi phải nằm trong khoảng 1-150!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên cho tuổi!")

    diagnosis = input("Chẩn đoán bệnh: ").strip()

    new_patient = {"id": p_id, "name": name, "age": age, "diagnosis": diagnosis}
    patient_list.append(new_patient)
    print("=> Đã thêm bệnh nhân thành công!")

def display_patients(patient_list):
    if not patient_list:
        print("\n[!] Hiện chưa có bệnh án nào trong hệ thống.")
        return

    print("\n" + "-"*75)
    print(f"{'ID':<10} | {'Họ Tên':<25} | {'Tuổi':<8} | {'Chẩn đoán':<25}")
    print("-"*75)
    for p in patient_list:
        print(f"{p['id']:<10} | {p['name']:<25} | {p['age']:<8} | {p['diagnosis']:<25}")
    print("-"*75)
    
# --- Lựa chọn ---
def main():
    patient_records = load_from_file()
    while True:
        display_menu()
        choice = input("Mời bạn chọn chức năng (1-7): ")

        if choice == '1':
            add_patient(patient_records)
        elif choice == '2':
            display_patients(patient_records)
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