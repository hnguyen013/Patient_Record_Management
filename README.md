# HỆ THỐNG QUẢN LÝ BỆNH ÁN

## 1. Giới thiệu dự án

Đây là chương trình **quản lý bệnh án phòng khám cơ bản**, được xây dựng bằng ngôn ngữ lập trình **Python** theo phương pháp **lập trình thủ tục**.

Chương trình chạy trên môi trường **CLI – Command Line Interface**, cho phép người dùng thao tác trực tiếp thông qua menu trong cửa sổ console. Hệ thống hỗ trợ quản lý danh sách bệnh nhân, bao gồm các chức năng như thêm bệnh nhân, hiển thị danh sách, tìm kiếm, sắp xếp, thống kê, chỉnh sửa, xóa dữ liệu, lưu dữ liệu và xuất báo cáo.

Dự án được thực hiện nhằm vận dụng các kiến thức đã học trong học phần **Phương pháp lập trình**, bao gồm:

- Sử dụng hàm để chia nhỏ chương trình.
- Sử dụng vòng lặp để xây dựng menu tương tác.
- Sử dụng cấu trúc điều kiện để xử lý lựa chọn của người dùng.
- Sử dụng danh sách và từ điển để quản lý dữ liệu.
- Kiểm tra dữ liệu đầu vào.
- Đọc, ghi và xuất dữ liệu ra file.
- Trình bày dữ liệu dưới dạng bảng có định dạng.

---

## 2. Đề tài lựa chọn

**Topic 7: Patient Record Management**

Tên đề tài tiếng Việt:

**Hệ thống quản lý bệnh án**

Đề tài tập trung xây dựng một chương trình đơn giản để quản lý thông tin bệnh nhân trong phòng khám. Mỗi bệnh nhân được xem là một bản ghi dữ liệu, gồm các thông tin cơ bản như:

- Mã bệnh nhân
- Họ và tên
- Tuổi
- Chẩn đoán bệnh

---

## 3. Mục tiêu của chương trình

Chương trình được xây dựng với các mục tiêu chính sau:

1. Giúp người dùng quản lý danh sách bệnh nhân một cách đơn giản.
2. Cho phép thêm, xem, tìm kiếm, sắp xếp, chỉnh sửa và xóa thông tin bệnh nhân.
3. Hỗ trợ thống kê số lượng bệnh nhân và độ tuổi trung bình.
4. Hỗ trợ phân nhóm bệnh nhân theo độ tuổi.
5. Lưu dữ liệu để có thể sử dụng lại trong các lần chạy chương trình sau.
6. Xuất báo cáo tổng hợp ra file văn bản.
7. Rèn luyện tư duy lập trình thủ tục và cách tổ chức chương trình theo từng hàm riêng biệt.

---

## 4. Công nghệ và thư viện sử dụng

Dự án sử dụng các công nghệ và thư viện sau:

| Thành phần | Vai trò |
|---|---|
| Python | Ngôn ngữ lập trình chính |
| PrettyTable | Hiển thị dữ liệu dưới dạng bảng đẹp, dễ nhìn |
| JSON | Lưu trữ dữ liệu bệnh nhân có cấu trúc |
| TXT | Xuất báo cáo thống kê dạng văn bản |
| CLI | Giao diện dòng lệnh để người dùng tương tác với chương trình |

Thư viện ngoài cần cài đặt:

    pip install prettytable

---

## 5. Cấu trúc dữ liệu

Trong chương trình, mỗi bệnh nhân được lưu dưới dạng một dictionary gồm các trường thông tin:

    {
        "id": "BN01",
        "name": "Nguyen Van A",
        "age": 25,
        "diagnosis": "Cam cum"
    }

Danh sách bệnh nhân được lưu trong một list:

    patients = [
        {
            "id": "BN01",
            "name": "Nguyen Van A",
            "age": 25,
            "diagnosis": "Cam cum"
        },
        {
            "id": "BN02",
            "name": "Tran Thi B",
            "age": 40,
            "diagnosis": "Dau dau"
        }
    ]

Cách tổ chức này giúp chương trình dễ dàng thêm, sửa, xóa, tìm kiếm, sắp xếp và thống kê dữ liệu.

---

## 6. Các file trong dự án

| Tên file | Chức năng |
|---|---|
| `main.py` | File chứa mã nguồn chính của chương trình |
| `patients.json` | File lưu trữ dữ liệu bệnh nhân dưới dạng JSON |
| `patients_report.txt` | File báo cáo thống kê được xuất ra từ chương trình |
| `README.md` | File mô tả dự án, hướng dẫn chạy chương trình và tự đánh giá |

---


## 7. Chức năng chính của chương trình

Chương trình có các chức năng chính sau:

### 7.1. Tiếp nhận bệnh nhân mới

Người dùng có thể nhập thông tin bệnh nhân mới gồm:

- Mã bệnh nhân
- Họ và tên
- Tuổi
- Chẩn đoán bệnh

Chương trình có kiểm tra dữ liệu đầu vào để hạn chế lỗi khi nhập.

### 7.2. Hiển thị danh sách bệnh án

Chức năng này hiển thị toàn bộ danh sách bệnh nhân hiện có trong hệ thống dưới dạng bảng rõ ràng.

Thông tin hiển thị gồm:

- ID
- Họ tên
- Tuổi
- Chẩn đoán

Dữ liệu được trình bày bằng thư viện PrettyTable nên dễ quan sát hơn so với việc in dữ liệu thông thường.

### 7.3. Tìm kiếm bệnh nhân

Chương trình hỗ trợ tìm kiếm bệnh nhân theo:

- Mã bệnh nhân
- Họ tên bệnh nhân

Ngoài tìm kiếm theo mã ID chính xác, chương trình còn hỗ trợ tìm kiếm gần đúng theo tên. Ví dụ, người dùng chỉ cần nhập một phần tên, chương trình vẫn có thể tìm các bệnh nhân phù hợp.

### 7.4. Sắp xếp danh sách bệnh nhân

Chương trình cho phép sắp xếp danh sách bệnh nhân theo các tiêu chí như:

- Sắp xếp theo tên
- Sắp xếp theo tuổi

Chức năng này giúp dữ liệu dễ theo dõi hơn, đặc biệt khi danh sách bệnh nhân có nhiều bản ghi.

### 7.5. Thống kê và tính toán số liệu

Chương trình thực hiện các thống kê cơ bản trên tập dữ liệu bệnh nhân, gồm:

- Tổng số bệnh nhân
- Độ tuổi trung bình
- Số lượng bệnh nhân theo nhóm tuổi

Các nhóm tuổi được phân loại như sau:

| Nhóm tuổi | Điều kiện |
|---|---|
| Trẻ em | Dưới 18 tuổi |
| Người lớn | Từ 18 đến 60 tuổi |
| Người già | Trên 60 tuổi |

### 7.6. Chỉnh sửa thông tin bệnh nhân

Người dùng có thể chỉnh sửa thông tin bệnh nhân dựa trên mã ID.

Các thông tin có thể chỉnh sửa gồm:

- Họ tên
- Tuổi
- Chẩn đoán bệnh

Chức năng này giúp cập nhật dữ liệu khi thông tin bệnh nhân có thay đổi.

### 7.7. Xóa thông tin bệnh nhân

Người dùng có thể xóa bệnh nhân khỏi danh sách thông qua mã ID.

Trước khi xóa, chương trình yêu cầu người dùng xác nhận để tránh trường hợp xóa nhầm dữ liệu.

### 7.8. Lưu dữ liệu

Chương trình có chức năng lưu dữ liệu bệnh nhân vào file `patients.json`.

Khi mở chương trình ở lần sau, dữ liệu đã lưu có thể được tải lại để tiếp tục sử dụng.

### 7.9. Xuất báo cáo

Chương trình có thể xuất báo cáo thống kê ra file `patients_report.txt`.

Báo cáo giúp tổng hợp tình trạng dữ liệu hiện tại của hệ thống và có thể dùng để xem lại hoặc nộp bài.

---

## 8. Menu chương trình

Khi chạy chương trình, hệ thống sẽ hiển thị menu như sau:

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

Người dùng nhập số từ `1` đến `9` để chọn chức năng tương ứng.

Nếu người dùng nhập sai lựa chọn, chương trình sẽ thông báo lỗi và yêu cầu nhập lại thay vì bị dừng đột ngột.

---

## 9. Kiểm tra dữ liệu đầu vào

Chương trình có kiểm tra dữ liệu đầu vào đối với các thông tin quan trọng.

Các điều kiện kiểm tra gồm:

| Dữ liệu | Cách kiểm tra |
|---|---|
| Mã bệnh nhân | Không được để trống |
| Mã bệnh nhân | Không được trùng với bệnh nhân đã có |
| Tên bệnh nhân | Không được để trống |
| Tuổi | Phải là số nguyên |
| Tuổi | Phải nằm trong khoảng hợp lý từ 1 đến 149 |

---

## 10. Các hàm chính trong chương trình

Chương trình được chia thành nhiều hàm nhỏ để dễ quản lý, đúng định hướng lập trình thủ tục và thiết kế Top-Down.

| Tên hàm | Chức năng |
|---|---|
| `display_menu()` | Hiển thị menu chính của chương trình |
| `load_from_file()` | Tải dữ liệu bệnh nhân từ file JSON |
| `save_to_file()` | Lưu dữ liệu bệnh nhân vào file JSON |
| `build_pretty_table()` | Tạo bảng hiển thị danh sách bệnh nhân |
| `export_report()` | Xuất báo cáo thống kê ra file TXT |
| `add_patient()` | Thêm bệnh nhân mới |
| `display_patients()` | Hiển thị danh sách bệnh nhân |
| `search_patient()` | Tìm kiếm bệnh nhân theo ID hoặc tên |
| `sort_patients()` | Sắp xếp danh sách bệnh nhân |
| `statistics_patients()` | Thống kê và tính toán số liệu |
| `update_patient()` | Chỉnh sửa thông tin bệnh nhân |
| `delete_patient()` | Xóa bệnh nhân khỏi danh sách |
| `main()` | Điều khiển luồng chạy chính của chương trình |

Việc chia chương trình thành nhiều hàm giúp mã nguồn rõ ràng hơn, dễ kiểm tra lỗi và dễ mở rộng thêm chức năng nếu cần.

---

## 11. Ví dụ sử dụng chương trình

### 11.1. Ví dụ thêm bệnh nhân

    Nhập mã bệnh nhân: BN01
    Nhập họ tên: Nguyen Van A
    Nhập tuổi: 25
    Nhập chẩn đoán: Cam cum
    => Đã thêm bệnh nhân thành công!

### 11.2. Ví dụ hiển thị danh sách bệnh nhân

    +------+----------------+------+----------------+
    | ID   | Họ Tên         | Tuổi | Chẩn đoán      |
    +------+----------------+------+----------------+
    | BN01 | Nguyen Van A   | 25   | Cam cum        |
    | BN02 | Tran Thi B     | 40   | Dau dau        |
    +------+----------------+------+----------------+

### 11.3. Ví dụ thống kê

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

---

## 12. Chức năng nâng cao đã thực hiện

Ngoài các chức năng cơ bản, chương trình có thêm một số chức năng nâng cao:

### 12.1. Tìm kiếm gần đúng

Người dùng có thể nhập một phần tên bệnh nhân để tìm kiếm. Ví dụ, nếu có bệnh nhân tên `Nguyen Van A`, người dùng chỉ cần nhập `Nguyen` hoặc `Van` thì chương trình vẫn có thể tìm được.

Chức năng này đáp ứng yêu cầu **Advanced Search & Filter**.

### 12.2. Thống kê theo nhóm tuổi

Chương trình không chỉ tính tổng số bệnh nhân và tuổi trung bình, mà còn phân loại bệnh nhân theo nhóm tuổi:

- Trẻ em
- Người lớn
- Người già

Chức năng này đáp ứng yêu cầu **Advanced Statistics – Grouping data**.

### 12.3. Lưu trữ dữ liệu bằng JSON

Chương trình sử dụng file `patients.json` để lưu trữ và đọc lại danh sách bệnh nhân.

Chức năng này đáp ứng yêu cầu **Advanced Storage – JSON**.

### 12.4. Chỉnh sửa và xóa dữ liệu

Chương trình có thêm chức năng chỉnh sửa và xóa bệnh nhân theo mã ID. Đây là hai chức năng giúp chương trình có tính thực tế hơn trong quá trình quản lý dữ liệu.

---

## 13. Tự đánh giá theo thang điểm

Dựa trên tiêu chí chấm điểm của đề bài, chương trình được tự đánh giá như sau:

| STT | Tiêu chí | Điểm tối đa | Tự chấm | Giải thích |
|---|---|---:|---:|---|
| 1 | CLI Menu System | 1.0 | 1.0 | Có menu rõ ràng, chạy trên console, dùng vòng lặp để lặp lại menu cho đến khi thoát |
| 2 | Data Input & Validation | 1.0 | 1.0 | Thêm được bệnh nhân mới, có kiểm tra ID rỗng, ID trùng và tuổi phải là số |
| 3 | Data Display | 1.0 | 1.0 | Dữ liệu được hiển thị bằng bảng PrettyTable rõ ràng, dễ nhìn |
| 4 | Basic Search | 1.0 | 1.0 | Tìm kiếm được bệnh nhân theo ID hoặc tên |
| 5 | Sorting Mechanism | 1.0 | 1.0 | Có chức năng sắp xếp danh sách bệnh nhân theo tên hoặc tuổi |
| 6 | Basic Calculation | 1.0 | 1.0 | Có tính tổng số bệnh nhân, tuổi trung bình và thống kê nhóm tuổi |
| 7 | TXT File Handling | 1.0 | 1.0 | Có xuất báo cáo ra file TXT, dữ liệu chính được lưu bằng JSON thay vì TXT theo yêu cầu nâng cao |
| 8 | Advanced Complex Logic | 1.0 | 1.0 | Có tìm kiếm gần đúng và thống kê theo nhóm tuổi |
| 9 | JSON / DBMS | 1.0 | 1.0 | Có lưu và tải dữ liệu bằng file JSON có cấu trúc |
| 10 | Git & Modular Code | 1.0 | 1.0 | Code được chia thành nhiều hàm rõ ràng và có README; repository GitHub có trên 3 commit |

### Tổng điểm tự đánh giá: 10 / 10

---

## 14. Thông tin sinh viên

Sinh viên thực hiện: **Trần Hạnh Nguyên**

Môn học: **Phương pháp lập trình**

Giảng viên: **Trần Văn Long**

Khoa: **Tin học**