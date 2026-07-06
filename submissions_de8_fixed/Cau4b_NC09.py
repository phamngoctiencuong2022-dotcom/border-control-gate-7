# Câu 4b: Ghi các dòng chứa từ "Python" vào file python_lines.txt
try:
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    python_lines = [line for line in lines if 'Python' in line]
    with open('python_lines.txt', 'w', encoding='utf-8') as f:
        f.writelines(python_lines)
    print(f"Wrote {len(python_lines)} lines")
except FileNotFoundError:
    print("File not found")
