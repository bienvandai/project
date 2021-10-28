
from SinhVien import sinhvien

list = []

while True:
    print(f'''
        0. Thoát chương trình
        1. Thêm sinh viên
        2. Sửa thông tin sinh viên
        3. Xóa sinh viên
        4. Tìm kiếm sinh viên
        5. Hiển thị sinh viên
    ''')
    select = input("Chọn chức năng: \n")

    if str(select).isdigit():
        select = int(select)
        
    # 0.Thoát chương trình
        if select == 0:
            break
    # 1.Thêm sinh viên
        elif select == 1:
            print("\n---- THÊM SINH VIÊN ----\n")

            id = input("Nhập mã sinh viên: ")
            name = input("Nhập tên sinh viên: ")
            age = input("Tuổi: ")
            gender = input("Nhập giới tính: ")
            majors = input("Nhập ngành học: ")
            course = input("Nhập khóa: ")
            sv = sinhvien(id, name, age, gender, majors, course)
            list.append(sv)
    # 2.Sửa thông tin sinh viên
        elif select == 2:
            print("\n---- SỬA THÔNG TIN SINH VIÊN ----\n")
            id = input("Nhập mã sinh viên cần sửa thông tin: ")
            for i in list:
                if i.get_id() == id:
                    i.set_name(input("Nhập tên: "))
                    i.set_age(input("Tuổi: "))
                    i.set_gender(input("Nhập Giới tính: "))
                    i.set_majors(input("Nhập nghành học: "))
                    i.set_course(input("Nhập khóa: "))
                    
                    i.show_info()
    # 3.Xóa sinh viên
        elif select == 3:
            while True:
                print("\n---- XÓA SINH VIÊN ----\n")
                id = input("Nhập mã sinh viên cần xóa: ")
                delete = input("Bạn có chắc chắn muốn xóa sinh viên này(y/n): ")
                if delete == "y":
                    for i in list:
                        if i.get_id() == id:
                            list.remove(i)
                            print("\nBạn đã xóa thành công")
                    break
                elif delete == "n":
                    break
                else:
                    print("Bạn phải chọn đúng câu trả lời y=Có, n=Không")
    # 4.Xem thông tin sinh viên
        elif select == 4:
            print("\n---- TÌM KIẾM SINH VIÊN ----\n")
            name = input("Nhập tên sinh viên cần tìm: ")
            for i in list:
                if i.get_name() == name:
                    i.show_info()
    #5.hiển thị tất cả
        elif select == 5:
            if len(list) == 0:
                print("\nHiện tại không có sinh viên nào ở trong danh sách, vui lòng chọn chức năng thêm sinh với với phím tắt là 1 để thêm sinh viên vào danh sách\n")
            else:
                print("\n")
                for i in list:
                    i.show_info()
                print(f"\nHiện có {len(list)} sinh viên trong danh sách \n")

    else:
        print("\nBạn phải nhập số tương ứng với chức năng mà bạn muốn. Vui lòng nhập lại")

        