from services.db_handler import insert_citizen, update_citizen, delete_citizen, search_by_perID, search_by_name

def main():
    print("=== QUẢN LÝ DÂN SỐ (CLI MODE) ===")
    while True:
        print("\nChọn chức năng:")
        print("1. Thêm công dân")
        print("2. Cập nhật công dân")
        print("3. Xoá công dân")
        print("4. Tìm theo perID")
        print("5. Tìm theo tên")
        print("0. Thoát")

        choice = input("Lựa chọn của bạn: ")
        if choice == "1":
            perID = input("Mã định danh: ")
            name = input("Họ tên: ")
            dob = input("Ngày sinh (yyyy-mm-dd): ")
            sex = input("Giới tính (M/F): ")
            insert_citizen(perID, name, dob, sex)
            print("✅ Đã thêm.")
        elif choice == "2":
            perID = input("Mã định danh cần cập nhật: ")
            name = input("Tên mới (bỏ trống nếu không đổi): ")
            dob = input("Ngày sinh mới (yyyy-mm-dd, bỏ trống nếu không đổi): ")
            sex = input("Giới tính mới (M/F, bỏ trống nếu không đổi): ")
            update_citizen(perID, name or None, dob or None, sex or None)
            print("✅ Đã cập nhật.")
        elif choice == "3":
            perID = input("Mã định danh cần xoá: ")
            delete_citizen(perID)
            print("✅ Đã xoá.")
        elif choice == "4":
            perID = input("Nhập perID: ")
            result = search_by_perID(perID)
            print(result if result else "❌ Không tìm thấy.")
        elif choice == "5":
            name = input("Nhập tên: ")
            results = search_by_name(name)
            print(f"Tìm thấy {len(results)} kết quả:")
            for r in results:
                print(r)
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
