raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

employees = []

data_list = raw_data.split("|")

for item in data_list:
    parts = item.split(";")

    emp_id = parts[0].strip().upper()
    name = parts[1].strip().title()
    phone = parts[2].strip().replace("-", "")
    department = parts[3].strip().upper()

    if phone.isdigit():
        masked_phone = "******" + phone[-4:]
    else:
        masked_phone = "Invalid Format"

    employees.append({
        "id": emp_id,
        "name": name,
        "phone": masked_phone,
        "department": department
    })

while True:
    print("\n===== MENU =====")
    print("1. Xem dữ liệu gốc")
    print("2. Xem dữ liệu chuẩn ")
    print("3. Tìm kiếm nhân viên theo ID")
    print("4. Thoát")

    choice = input("Nhập lựa chọn: ")

    if not choice.isdigit() or int(choice) not in range(1, 5):
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice == 1:
        print("\nDữ liệu gốc:")
        print(raw_data)

    elif choice == 2:
        print("\nDữ liệu chuẩn:")
        for emp in employees:
            print(f"ID: {emp['id']}")
            print(f"Họ tên: {emp['name']}")
            print(f"SĐT: {emp['phone']}")
            print(f"Phòng ban: {emp['department']}")
            print("----------------------")

    elif choice == 3:
        search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
        found = False
        for emp in employees:
            if emp["id"] == search_id:
                print("\nTìm thấy nhân viên")
                print(f"ID: {emp['id']}")
                print(f"Họ tên: {emp['name']}")
                print(f"SĐT: {emp['phone']}")
                print(f"Phòng ban: {emp['department']}")
                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == 4:
        print("Thoát chương trình")
        break

# C1: Phân tích Input / Output
# - Input:
#   + raw_data: kiểu string chứa danh sách nhân viên.
#   + choice: dữ liệu người dùng nhập từ bàn phím.
#   + search_id: mã nhân viên cần tìm.
#
# - Output:
#   + Hiển thị dữ liệu gốc.
#   + Hiển thị dữ liệu đã chuẩn hóa:
#       ID viết hoa
#       Họ tên chuẩn hóa
#       SĐT được che 6 số đầu hoặc báo Invalid Format
#       Phòng ban viết hoa
#   + Hiển thị kết quả tìm kiếm nhân viên.
#   + Thông báo lỗi khi nhập sai menu hoặc không tìm thấy nhân viên.


# C2: Đề xuất giải pháp
# - Dùng split("|") để tách từng nhân viên.
# - Dùng split(";") để tách thông tin từng nhân viên.
# - Dùng strip() để xóa khoảng trắng thừa.
# - Dùng upper() chuẩn hóa ID và phòng ban.
# - Dùng title() chuẩn hóa họ tên.
# - Dùng replace("-", "") để xóa dấu "-" trong số điện thoại.
# - Dùng isdigit() kiểm tra số điện thoại hợp lệ.
# - Dùng list + dictionary để lưu dữ liệu nhân viên.
# - Dùng vòng lặp while True để hiển thị menu liên tục.
# - Kiểm tra menu hợp lệ bằng isdigit() và range(1,5).
# - Tìm kiếm nhân viên bằng cách so sánh ID sau khi strip() và upper().


# C3: Thiết kế thuật toán / Pseudocode
# B1: Khởi tạo raw_data và danh sách employees rỗng.
# B2: Tách dữ liệu từng nhân viên bằng split("|").
# B3: Với mỗi nhân viên:
#       - Tách thông tin bằng split(";")
#       - Chuẩn hóa ID, tên, SĐT, phòng ban
#       - Kiểm tra SĐT hợp lệ
#       - Lưu vào employees
# B4: Hiển thị menu bằng vòng lặp while True.
# B5: Người dùng nhập lựa chọn.
# B6: Nếu nhập sai -> báo lỗi và quay lại menu.
# B7: Nếu chọn 1 -> hiển thị dữ liệu gốc.
# B8: Nếu chọn 2 -> hiển thị dữ liệu chuẩn hóa.
# B9: Nếu chọn 3 -> nhập ID và tìm kiếm nhân viên.
# B10: Nếu chọn 4 -> thoát chương trình.
