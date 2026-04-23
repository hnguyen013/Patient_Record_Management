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
def save_to_file(patient_list, filename="patients.txt"):
    """Lưu dữ liệu vào tệp văn bản [cite: 34, 46, 77]"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for p in patient_list:
                # Dùng dấu | để phân cách các trường dữ liệu
                line = f"{p['id']}|{p['name']}|{p['age']}|{p['diagnosis']}\n"
                f.write(line)
        print(f"\n=> Đã lưu {len(patient_list)} bản ghi vào {filename} thành công!")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

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

def search_patient(patient_list):
    if not patient_list:
        print("\n[!] Danh sách trống, không có dữ liệu để tìm kiếm.")
        return
    print("\n" + "-"*35)
    print("      TÌM KIẾM BỆNH NHÂN")
    print("-" * 35)
    keyword = input("Nhập ID hoặc Tên bệnh nhân cần tìm: ").strip().lower()

    results = []
    for p in patient_list:
        # 1. Tìm chính xác theo ID 
        # 2. Tìm kiếm chuỗi con theo Tên (Advanced Search - khớp một phần) 
        if keyword == p['id'].lower() or keyword in p['name'].lower():
            results.append(p)

    if results:
        print(f"\n=> Tìm thấy {len(results)} kết quả phù hợp:")
        display_patients(results) # Tận dụng hàm hiển thị bảng đã viết 
    else:
        print(f" [!] Không tìm thấy bệnh nhân nào khớp với từ khóa: '{keyword}'")

def sort_patients(patient_list):
    if not patient_list:
        print("\n[!] Danh sách trống, không có dữ liệu để sắp xếp.")
        return

    print("\n--- TÙY CHỌN SẮP XẾP ---")
    print("1. Sắp xếp theo Tên (A-Z)")
    print("2. Sắp xếp theo Tuổi (Tăng dần)")
    sub_choice = input("Mời bạn chọn (1-2): ")

    if sub_choice == '1':
        patient_list.sort(key=lambda x: x['name'].lower())
        print("=> Đã sắp xếp danh sách theo Tên (A-Z).")
    elif sub_choice == '2':
        patient_list.sort(key=lambda x: x['age'])
        print("=> Đã sắp xếp danh sách theo Tuổi tăng dần.")
    else:
        print("Lựa chọn không hợp lệ, quay lại menu chính.")
        return
    display_patients(patient_list)


def statistics_patients(patient_list):
    """Thực hiện tính toán và thống kê dữ liệu bệnh nhân"""
    if not patient_list:
        print("\n[!] Không có dữ liệu để thống kê.")
        return

    total_patients = len(patient_list)
    
    # 1. Tính toán cơ bản: Tuổi trung bình
    total_age = sum(p['age'] for p in patient_list)
    average_age = total_age / total_patients

    # 2. Thống kê nâng cao: Phân nhóm theo độ tuổi (Grouping)
    tre_em = 0    # < 18 tuổi
    nguoi_lon = 0 # 18 - 60 tuổi
    nguoi_gia = 0 # > 60 tuổi

    for p in patient_list:
        if p['age'] < 18:
            tre_em += 1
        elif p['age'] <= 60:
            nguoi_lon += 1
        else:
            nguoi_gia += 1

    print("\n" + "="*35)
    print("      BÁO CÁO THỐNG KÊ Y TẾ")
    print("="*35)
    print(f"Tổng số bệnh nhân: {total_patients}")
    print(f"Độ tuổi trung bình: {average_age:.1f}")
    print("-" * 35)
    print(f"1. Trẻ em (<18t):  {tre_em} BN ({(tre_em/total_patients)*100:.1f}%)")
    print(f"2. Người lớn (18-60t): {nguoi_lon} BN ({(nguoi_lon/total_patients)*100:.1f}%)")
    print(f"3. Người già (>60t):   {nguoi_gia} BN ({(nguoi_gia/total_patients)*100:.1f}%)")
    print("="*35)

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
            search_patient(patient_records)
        elif choice == '4':
            sort_patients(patient_records)
        elif choice == '5':
            statistics_patients(patient_records)
        elif choice == '6':
            save_to_file(patient_records)
            print("\n[Tính năng Sẽ cập nhật ở sau]")
        elif choice == '7':
            save_to_file(patient_records)
            print("Hệ thống đã đóng. Cảm ơn bạn!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 7.")

if __name__ == "__main__":
    main()