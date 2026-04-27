# Hệ thống quản lý bệnh án phòng khám

## 1. Giới thiệu dự án

Đây là chương trình quản lý bệnh án phòng khám cơ bản, được xây dựng bằng ngôn ngữ Python theo phương pháp lập trình thủ tục.

Chương trình chạy trên giao diện dòng lệnh, cho phép người dùng quản lý danh sách bệnh nhân, tìm kiếm bệnh nhân, sắp xếp dữ liệu, chỉnh sửa thông tin, xóa bệnh nhân, thống kê số liệu, lưu dữ liệu và xuất báo cáo.

Dự án được thực hiện nhằm vận dụng các kiến thức đã học về hàm, vòng lặp, cấu trúc điều kiện, xử lý dữ liệu và xử lý tệp trong Python.

---

## 2. Đề tài lựa chọn

**Topic 7: Patient/Clinic Record Management**

Tên đề tài tiếng Việt:

**Hệ thống quản lý bệnh án/phòng khám cơ bản**

Đề tài tập trung xây dựng một chương trình đơn giản để quản lý thông tin bệnh nhân trong phòng khám. Mỗi bệnh nhân có các thông tin cơ bản gồm mã bệnh nhân, họ tên, tuổi và chẩn đoán bệnh.

---

## 3. Chức năng chính của chương trình

Chương trình gồm các chức năng chính sau:

1. **Tiếp nhận bệnh nhân mới**

   Người dùng có thể nhập thông tin bệnh nhân gồm mã bệnh nhân, họ tên, tuổi và chẩn đoán.

2. **Hiển thị danh sách bệnh án**

   Chương trình hiển thị toàn bộ danh sách bệnh nhân dưới dạng bảng rõ ràng, dễ quan sát.

3. **Tìm kiếm bệnh nhân**

   Người dùng có thể tìm kiếm bệnh nhân theo mã ID hoặc theo tên. Chức năng tìm kiếm theo tên có hỗ trợ tìm gần đúng.

4. **Sắp xếp danh sách bệnh nhân**

   Chương trình cho phép sắp xếp danh sách bệnh nhân theo tên hoặc theo tuổi.

5. **Thống kê và tính toán số liệu**

   Chương trình thống kê tổng số bệnh nhân, tính độ tuổi trung bình và phân nhóm bệnh nhân theo độ tuổi.

6. **Chỉnh sửa thông tin bệnh nhân**

   Người dùng có thể chỉnh sửa họ tên, tuổi hoặc chẩn đoán của bệnh nhân dựa trên mã ID.

7. **Xóa thông tin bệnh nhân**

   Người dùng có thể xóa bệnh nhân khỏi danh sách dựa trên mã ID. Trước khi xóa, chương trình sẽ yêu cầu xác nhận để tránh xóa nhầm.

8. **Lưu dữ liệu**

   Dữ liệu bệnh nhân được lưu lại để khi mở chương trình lần sau vẫn có thể tiếp tục sử dụng.

9. **Xuất báo cáo**

   Chương trình có thể xuất báo cáo tổng hợp ra file văn bản để người dùng xem hoặc nộp.

---

## 4. Công nghệ sử dụng

Dự án sử dụng các công nghệ và thư viện sau:

- Python
- PrettyTable
- JSON
- File TXT
- Giao diện dòng lệnh

---

## 5. Cấu trúc dữ liệu

Mỗi bệnh nhân được lưu dưới dạng một bản ghi gồm các thông tin:

- Mã bệnh nhân
- Họ và tên
- Tuổi
- Chẩn đoán bệnh

Ví dụ một bản ghi bệnh nhân:

```json
{
    "id": "BN01",
    "name": "Nguyen Van A",
    "age": 25,
    "diagnosis": "Cam cum"
}
```

Danh sách bệnh nhân sẽ được lưu dưới dạng một danh sách các bản ghi.

---

## 6. Các file trong dự án

| Tên file | Chức năng |
|---|---|
| `main.py` | File chứa mã nguồn chính của chương trình |
| `patients.json` | File lưu trữ dữ liệu bệnh nhân |
| `patients_report.txt` | File báo cáo được xuất ra từ chương trình |
| `README.md` | File mô tả dự án và hướng dẫn sử dụng |

---

## 7. Giải thích việc sử dụng file JSON và TXT

Trong chương trình có sử dụng cả file JSON và file TXT vì hai loại file này có mục đích khác nhau.

File `patients.json` được dùng để lưu trữ dữ liệu chính của chương trình. JSON có cấu trúc rõ ràng, phù hợp để lưu danh sách bệnh nhân và đọc lại dữ liệu khi chạy chương trình lần sau.

File `patients_report.txt` được dùng để xuất báo cáo tổng hợp. File TXT có dạng văn bản đơn giản, dễ mở, dễ đọc và phù hợp để nộp hoặc in báo cáo.

Tóm lại:

| Loại file | Vai trò |
|---|---|
| JSON | Lưu trữ dữ liệu chính của chương trình |
| TXT | Xuất báo cáo cho người dùng |

---

## 8. Cài đặt thư viện cần thiết

Trước khi chạy chương trình, cần cài đặt thư viện PrettyTable bằng lệnh:

```bash
pip install prettytable
```

Nếu máy đã cài thư viện này thì có thể bỏ qua bước trên.

---

## 9. Cách chạy chương trình

Có thể chạy chương trình bằng Terminal, Command Prompt hoặc PyCharm.

Nếu chạy bằng Terminal hoặc Command Prompt, mở thư mục chứa file chương trình và nhập lệnh:

```bash
python main.py
```

Nếu chạy bằng PyCharm:

1. Mở thư mục dự án trong PyCharm.
2. Mở file `main.py`.
3. Nhấn nút **Run**.
4. Sử dụng các chức năng theo menu hiển thị trong cửa sổ console.

---

## 10. Menu chương trình

Khi chạy chương trình, hệ thống sẽ hiển thị menu như sau:

```text
=============================================
      HỆ THỐNG QUẢN LÝ BỆNH ÁN PHÒNG KHÁM
=============================================
1. Tiếp nhận bệnh nhân mới (Nhập dữ liệu)
2. Hiển thị danh sách bệnh án (Bảng định dạng)
3. Tìm kiếm bệnh nhân (Theo ID hoặc Tên)
4. Sắp xếp danh sách bệnh nhân
5. Thống kê & Tính toán số liệu
6. Chỉnh sửa thông tin bệnh nhân
7. Xóa thông tin bệnh nhân
8. Lưu dữ liệu và xuất báo cáo (.txt)
9. Thoát chương trình
---------------------------------------------
```

Người dùng nhập số từ 1 đến 9 để chọn chức năng tương ứng.

---

## 11. Kiểm tra dữ liệu đầu vào

Chương trình có kiểm tra một số dữ liệu quan trọng khi nhập thông tin bệnh nhân.

Các điều kiện kiểm tra gồm:

- Mã bệnh nhân không được để trống.
- Mã bệnh nhân không được trùng với bệnh nhân đã có trong hệ thống.
- Tuổi phải là số nguyên.
- Tuổi phải nằm trong khoảng hợp lý, từ 1 đến 149.

Các trường họ tên và chẩn đoán là dữ liệu dạng văn bản nên chương trình cho phép người dùng nhập linh hoạt hơn.

---

## 12. Các hàm chính trong chương trình

| Tên hàm | Chức năng |
|---|---|
| `display_menu()` | Hiển thị menu chính |
| `load_from_file()` | Tải dữ liệu từ file JSON |
| `save_to_file()` | Lưu dữ liệu vào file JSON |
| `build_pretty_table()` | Tạo bảng hiển thị dữ liệu |
| `export_report()` | Xuất báo cáo ra file TXT |
| `add_patient()` | Thêm bệnh nhân mới |
| `display_patients()` | Hiển thị danh sách bệnh nhân |
| `search_patient()` | Tìm kiếm bệnh nhân |
| `sort_patients()` | Sắp xếp danh sách bệnh nhân |
| `statistics_patients()` | Thống kê dữ liệu bệnh nhân |
| `update_patient()` | Chỉnh sửa thông tin bệnh nhân |
| `delete_patient()` | Xóa thông tin bệnh nhân |
| `main()` | Điều khiển luồng chạy chính của chương trình |

---

## 13. Chức năng nâng cao

Ngoài các chức năng cơ bản, chương trình còn có một số chức năng nâng cao:

1. **Tìm kiếm gần đúng**

   Người dùng có thể nhập một phần tên bệnh nhân để tìm kiếm thay vì phải nhập chính xác toàn bộ tên.

2. **Thống kê theo nhóm**

   Chương trình phân loại bệnh nhân theo nhóm tuổi gồm trẻ em, người lớn và người già.

3. **Lưu trữ dữ liệu bằng JSON**

   Chương trình sử dụng file JSON để lưu trữ dữ liệu có cấu trúc, giúp việc đọc và ghi dữ liệu thuận tiện hơn.

4. **Chỉnh sửa và xóa dữ liệu**

   Chương trình cho phép cập nhật hoặc xóa thông tin bệnh nhân theo mã ID, giúp hệ thống có tính ứng dụng thực tế hơn.

---

## 14. Ví dụ kết quả hiển thị

Ví dụ hiển thị danh sách bệnh nhân:

```text
+------------------------------------------------+
|              DANH SÁCH BỆNH NHÂN              |
+------+----------------+------+----------------+
| ID   | Họ Tên         | Tuổi | Chẩn đoán      |
+------+----------------+------+----------------+
| BN01 | Nguyen Van A   | 25   | Cam cum        |
| BN02 | Tran Thi B     | 40   | Dau dau        |
+------+----------------+------+----------------+
```

Ví dụ thống kê:

```text
===================================
      BÁO CÁO THỐNG KÊ Y TẾ
===================================
Tổng số bệnh nhân: 2
Độ tuổi trung bình: 32.5
-----------------------------------
1. Trẻ em (<18t):        0 BN (0.0%)
2. Người lớn (18-60t):   2 BN (100.0%)
3. Người già (>60t):     0 BN (0.0%)
===================================
```

---

## 15. Ghi chú

- Chương trình chạy trên giao diện dòng lệnh.
- Dữ liệu được tự động tải từ file `patients.json` khi chương trình bắt đầu.
- Dữ liệu được lưu lại khi người dùng chọn chức năng lưu hoặc thoát chương trình.
- File `patients_report.txt` được tạo khi người dùng chọn chức năng xuất báo cáo.
- Nếu file `patients.json` chưa tồn tại, chương trình sẽ bắt đầu với danh sách bệnh nhân rỗng.
- Sau khi thêm, chỉnh sửa hoặc xóa dữ liệu, người dùng nên chọn chức năng lưu hoặc thoát chương trình để dữ liệu được ghi vào file.

---

## 16. Thông tin sinh viên

Sinh viên thực hiện: **Trần Hạnh Nguyên**

Môn học: **Phương pháp lập trình**

Giảng viên: **Trần Văn Long**

Khoa: **Tin Học**

