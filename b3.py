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
# - raw_data là dữ liệu đầu vào kiểu string chứa thông tin nhiều nhân viên.
# - data_list là list sau khi tách raw_data bằng dấu "|".
# - parts là list chứa từng thông tin nhân viên sau khi split(";").
# - choice là dữ liệu người dùng nhập từ bàn phím để chọn menu.
# - search_id là mã nhân viên nhập vào để tìm kiếm.
#
# - Output:
#   + Hiển thị dữ liệu gốc.
#   + Hiển thị dữ liệu đã chuẩn hóa:
#       ID viết hoa
#       Họ tên viết hoa chữ cái đầu
#       SĐT được che 6 số đầu hoặc báo Invalid Format
#       Phòng ban viết hoa
#   + Hiển thị kết quả tìm kiếm nhân viên hoặc thông báo không tìm thấy.
#   + Hiển thị thông báo lỗi nếu nhập menu không hợp lệ.


# C2: Đề xuất giải pháp
# - Dùng split("|") để tách từng nhân viên trong raw_data.
# - Dùng split(";") để tách từng trường dữ liệu của nhân viên.
# - Dùng strip() để loại bỏ khoảng trắng dư thừa.
# - Dùng upper() chuẩn hóa emp_id và department.
# - Dùng title() chuẩn hóa name.
# - Dùng replace("-", "") để xóa dấu "-" trong số điện thoại.
# - Dùng isdigit() kiểm tra số điện thoại có hợp lệ hay không.
# - Dùng list employees để lưu danh sách nhân viên.
# - Dùng dictionary để lưu thông tin từng nhân viên.
# - Dùng while True để tạo menu chạy liên tục.
# - Dùng isdigit() và range(1,5) để kiểm tra menu hợp lệ.
# - Dùng strip().upper() khi tìm kiếm để hỗ trợ nhập thường hoặc dư khoảng trắng.


# C3: Thiết kế thuật toán / Mô tả luồng chương trình
# B1: Khởi tạo raw_data và employees = [].
# B2: Tách dữ liệu nhân viên bằng split("|").
# B3: Duyệt từng item trong data_list:
#       - Tách dữ liệu bằng split(";")
#       - Chuẩn hóa ID, tên, SĐT, phòng ban
#       - Kiểm tra SĐT bằng isdigit()
#       - Nếu hợp lệ -> che 6 số đầu
#       - Nếu sai -> gán "Invalid Format"
#       - Lưu dữ liệu vào employees
# B4: Hiển thị menu bằng vòng lặp while True.
# B5: Người dùng nhập choice.
# B6: Nếu nhập sai:
#       - In thông báo lỗi
#       - continue quay lại menu
# B7: Nếu chọn 1:
#       - Hiển thị raw_data
# B8: Nếu chọn 2:
#       - Duyệt employees và in dữ liệu chuẩn hóa
# B9: Nếu chọn 3:
#       - Nhập search_id
#       - Tìm kiếm nhân viên theo ID
#       - Nếu tìm thấy -> hiển thị thông tin
#       - Nếu không -> báo không tìm thấy
# B10: Nếu chọn 4:
#       - In thông báo thoát
#       - break kết thúc chương trình
