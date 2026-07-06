# Câu 4a: Đọc file và đếm tổng số dòng
try:
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(len(lines))
except FileNotFoundError:
    print("File not found")
