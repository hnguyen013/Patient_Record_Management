import os
import json
from prettytable import PrettyTable
from datetime import datetime


# --- UTILITY FUNCTIONS ---
def display_menu():
    print("\n" + "=" * 45)
    print("      HỆ THỐNG QUẢN LÝ BỆNH ÁN PHÒNG KHÁM")
    print("=" * 45)
    print("1. Tiếp nhận bệnh nhân mới (Nhập dữ liệu)")
    print("2. Hiển thị danh sách bệnh án (Bảng định dạng)")
    print("3. Tìm kiếm bệnh nhân (Theo ID hoặc Tên)")
    print("4. Sắp xếp danh sách bệnh nhân")
    print("5. Thống kê & Tính toán số liệu")
    print("6. Chỉnh sửa thông tin bệnh nhân")
    print("7. Xóa thông tin bệnh nhân")
    print("8. Lưu dữ liệu và xuất báo cáo (.txt)")
    print("9. Thoát chương trình")
    print("-" * 45)


def load_from_file(filename="patients.json"):
    patient_list = []
    if not os.path.exists(filename):
        return patient_list

    try:
        with open(filename, "r", encoding="utf-8") as f:
            patient_list = json.load(f)
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

    return patient_list


def save_to_file(patient_list, filename="patients.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(patient_list, f, ensure_ascii=False, indent=4)
        print(f"\n=> Đã lưu {len(patient_list)} bản ghi vào {filename} thành công!")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def build_pretty_table(patient_list, title="DANH SÁCH BỆNH NHÂN"):
    table = PrettyTable()
    table.title = title
    table.field_names = ["ID", "Họ Tên", "Tuổi", "Chẩn đoán"]
    table.align["ID"] = "l"
    table.align["Họ Tên"] = "l"
    table.align["Tuổi"] = "c"
    table.align["Chẩn đoán"] = "l"

    for p in patient_list:
        table.add_row([p["id"], p["name"], p["age"], p["diagnosis"]])

    return table


def export_report(patient_list, filename="patients_report.txt"):
    if not patient_list:
        print("\nKhông có dữ liệu để xuất báo cáo.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as f:
            report_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            f.write("=== BÁO CÁO HỆ THỐNG QUẢN LÝ PHÒNG KHÁM ===\n")
            f.write(f"Thời gian xuất báo cáo: {report_time}\n")
            f.write(f"Tổng số bệnh nhân: {len(patient_list)}\n")

            avg_age = sum(p['age'] for p in patient_list) / len(patient_list)
            f.write(f"Độ tuổi trung bình: {avg_age:.1f}\n")
            f.write("-" * 70 + "\n")

            table = build_pretty_table(patient_list, title="BÁO CÁO DANH SÁCH BỆNH NHÂN")
            f.write(str(table) + "\n")

            f.write("-" * 70 + "\n")
            f.write("Báo cáo được trích xuất tự động.\n")

        print(f"=> Đã xuất báo cáo thống kê tại '{filename}'")
    except Exception as e:
        print(f"Lỗi khi xuất báo cáo: {e}")


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
            if 0 < age < 150:
                break
            else:
                print("Lỗi: Tuổi phải nằm trong khoảng 1-150!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên cho tuổi!")

    diagnosis = input("Chẩn đoán bệnh: ").strip()

    new_patient = {
        "id": p_id,
        "name": name,
        "age": age,
        "diagnosis": diagnosis
    }
    patient_list.append(new_patient)
    print("=> Đã thêm bệnh nhân thành công!")

def update_patient(patient_list):
    if not patient_list:
        print("\n[!] Danh sách trống, không có dữ liệu để chỉnh sửa.")
        return

    print("\n--- CHỈNH SỬA THÔNG TIN BỆNH NHÂN ---")
    p_id = input("Nhập ID bệnh nhân cần chỉnh sửa: ").strip()

    for p in patient_list:
        if p["id"].lower() == p_id.lower():
            print("\nThông tin hiện tại của bệnh nhân:")
            table = build_pretty_table([p], title="BỆNH NHÂN CẦN CHỈNH SỬA")
            print(table)

            print("\nNhấn Enter nếu muốn giữ nguyên thông tin cũ.")

            new_name = input(f"Họ tên mới ({p['name']}): ").strip()
            if new_name:
                p["name"] = new_name

            while True:
                new_age = input(f"Tuổi mới ({p['age']}): ").strip()
                if not new_age:
                    break
                try:
                    new_age = int(new_age)
                    if 0 < new_age < 150:
                        p["age"] = new_age
                        break
                    else:
                        print("Lỗi: Tuổi phải nằm trong khoảng 1-150!")
                except ValueError:
                    print("Lỗi: Vui lòng nhập số nguyên cho tuổi!")

            new_diagnosis = input(f"Chẩn đoán mới ({p['diagnosis']}): ").strip()
            if new_diagnosis:
                p["diagnosis"] = new_diagnosis

            print("=> Đã cập nhật thông tin bệnh nhân thành công!")
            return

    print(f"[!] Không tìm thấy bệnh nhân có ID: {p_id}") 

def delete_patient(patient_list):
    if not patient_list:
        print("\n[!] Danh sách trống, không có dữ liệu để xóa.")
        return

    print("\n--- XÓA THÔNG TIN BỆNH NHÂN ---")
    p_id = input("Nhập ID bệnh nhân cần xóa: ").strip()

    for p in patient_list:
        if p["id"].lower() == p_id.lower():
            print("\nThông tin bệnh nhân cần xóa:")
            table = build_pretty_table([p], title="BỆNH NHÂN CẦN XÓA")
            print(table)

            confirm = input("Bạn có chắc chắn muốn xóa bệnh nhân này không? (y/n): ").strip().lower()

            if confirm == "y":
                patient_list.remove(p)
                print("=> Đã xóa bệnh nhân thành công!")
            else:
                print("=> Đã hủy thao tác xóa.")
            return

    print(f"[!] Không tìm thấy bệnh nhân có ID: {p_id}")

def display_patients(patient_list):
    if not patient_list:
        print("\n[!] Hiện chưa có bệnh án nào trong hệ thống.")
        return

    table = build_pretty_table(patient_list)
    print("\n" + str(table))


def search_patient(patient_list):
    if not patient_list:
        print("\n[!] Danh sách trống, không có dữ liệu để tìm kiếm.")
        return

    print("\n" + "-" * 35)
    print("      TÌM KIẾM BỆNH NHÂN")
    print("-" * 35)
    keyword = input("Nhập ID hoặc Tên bệnh nhân cần tìm: ").strip().lower()

    results = []
    for p in patient_list:
        if keyword == p['id'].lower() or keyword in p['name'].lower():
            results.append(p)

    if results:
        print(f"\n=> Tìm thấy {len(results)} kết quả phù hợp:")
        table = build_pretty_table(results, title="KẾT QUẢ TÌM KIẾM")
        print(table)
    else:
        print(f"[!] Không tìm thấy bệnh nhân nào khớp với từ khóa: '{keyword}'")


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
    if not patient_list:
        print("\n[!] Không có dữ liệu để thống kê.")
        return

    total_patients = len(patient_list)
    total_age = sum(p['age'] for p in patient_list)
    average_age = total_age / total_patients

    tre_em = 0
    nguoi_lon = 0
    nguoi_gia = 0

    for p in patient_list:
        if p['age'] < 18:
            tre_em += 1
        elif p['age'] <= 60:
            nguoi_lon += 1
        else:
            nguoi_gia += 1

    print("\n" + "=" * 35)
    print("      BÁO CÁO THỐNG KÊ Y TẾ")
    print("=" * 35)
    print(f"Tổng số bệnh nhân: {total_patients}")
    print(f"Độ tuổi trung bình: {average_age:.1f}")
    print("-" * 35)
    print(f"1. Trẻ em (<18t):        {tre_em} BN ({(tre_em / total_patients) * 100:.1f}%)")
    print(f"2. Người lớn (18-60t):   {nguoi_lon} BN ({(nguoi_lon / total_patients) * 100:.1f}%)")
    print(f"3. Người già (>60t):     {nguoi_gia} BN ({(nguoi_gia / total_patients) * 100:.1f}%)")
    print("=" * 35)


# --- Lựa chọn ---
def main():
    patient_records = load_from_file()

    while True:
        display_menu()
        choice = input("Mời bạn chọn chức năng (1-9): ")

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
            update_patient(patient_records)
        elif choice == '7':
            delete_patient(patient_records)
        elif choice == '8':
            save_to_file(patient_records)
            export_report(patient_records)
        elif choice == '9':
            save_to_file(patient_records)
            print("Hệ thống đã đóng. Cảm ơn bạn!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 9.")


if __name__ == "__main__":
    main()