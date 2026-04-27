# Hệ thống quản lý bệnh án phòng khám

## 1. Giới thiệu dự án

Đây là chương trình quản lý bệnh án phòng khám cơ bản, được xây dựng bằng ngôn ngữ Python theo hướng lập trình thủ tục.

Chương trình chạy trên giao diện dòng lệnh (CLI), cho phép người dùng quản lý danh sách bệnh nhân, tìm kiếm, sắp xếp, thống kê và xuất báo cáo dữ liệu.

Đề tài được xây dựng theo yêu cầu Mini Project - Procedural Programming Application.

## 2. Chức năng chính

Chương trình gồm các chức năng:

1. Tiếp nhận bệnh nhân mới
2. Hiển thị danh sách bệnh án dưới dạng bảng
3. Tìm kiếm bệnh nhân theo ID hoặc tên
4. Sắp xếp danh sách bệnh nhân theo tên hoặc tuổi
5. Thống kê số lượng bệnh nhân và độ tuổi trung bình
6. Xuất báo cáo ra file TXT
7. Lưu và tải dữ liệu bằng file JSON
8. Thoát chương trình

## 3. Cấu trúc dữ liệu

Mỗi bệnh nhân gồm các thông tin:

- ID bệnh nhân
- Họ và tên
- Tuổi
- Chẩn đoán bệnh

Ví dụ:

```json
{
    "id": "BN01",
    "name": "Nguyen Van A",
    "age": 25,
    "diagnosis": "Cảm cúm"
}