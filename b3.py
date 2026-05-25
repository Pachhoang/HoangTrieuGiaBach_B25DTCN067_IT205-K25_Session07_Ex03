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

#C1  Vì `strip()` trả về chuỗi mới và không thay đổi trực tiếp chuỗi gốc.
#C2  Vì `title()` chưa được gán lại vào biến `student_name`.
#C3  Vì `upper()` chỉ trả về chuỗi mới chứ không sửa trực tiếp biến.
#c4  Vì `lower()` chưa được gán lại cho biến `email`.
#c5  Cần gán kết quả xử lý lại cho biến, ví dụ: `student_name = student_name.strip()` 
