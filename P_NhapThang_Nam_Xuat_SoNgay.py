thang = int(input("Nhập tháng : "))  # Nhập tháng từ người dùng và chuyển sang kiểu số nguyên
nam = int(input("Nhập năm : "))  # Nhập năm từ người dùng và chuyển sang kiểu số nguyên

# Tính số ngày của tháng và in ra kết quả
print("Tháng", thang, "có", 31 if thang in [1, 3, 5, 7, 8, 10, 12] else 30 if thang in [4, 6, 9, 11] else 29 if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0) else 28 if thang == 2 else "không hợp lệ", "ngày")
