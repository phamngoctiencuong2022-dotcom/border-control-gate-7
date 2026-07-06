# Câu 4c: Thêm vào cuối file input.txt dòng: "MSSV: [MSSV của bạn]"
mssv = input().strip()
try:
    with open('input.txt', 'a', encoding='utf-8') as f:
        f.write(f"MSSV: {mssv}\n")
    print("Added successfully")
except FileNotFoundError:
    print("File not found")
