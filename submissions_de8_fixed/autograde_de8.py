import subprocess
import os
import ast
from test_de8 import tests

def normalize(s):
    return s.lower().replace(" ", "").replace(":", "").replace("=", "").strip()

def run_code(file, input_data):
    try:
        result = subprocess.run(
            ["python", file],
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3
        )
        output = result.stdout.decode().strip().splitlines()
        return [line.strip() for line in output if line.strip()]
    except subprocess.TimeoutExpired:
        return ["loiquathoigian"]
    except Exception as e:
        return [f"error: {str(e)}"]

def is_dict_expected(expected):
    return isinstance(expected, dict)

def test_dict_output(output, expected_dict):
    for line in output:
        try:
            d = ast.literal_eval(line)
            if isinstance(d, dict) and d == expected_dict:
                return True
        except:
            continue
    return False

def test_normal_output(output, expected):
    if not expected:
        return len(output) == 0
    expected_norm = normalize(str(expected))
    return any(expected_norm in normalize(out) for out in output)

def grade(student_id="unknown", base_dir="."):
    total_score = 0
    max_score = 0
    print(f"📋 Bắt đầu chấm điểm cho {student_id}\n")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir_path = os.path.join(script_dir, base_dir)
    
    for bai, testcases in tests.items():
        file_path = os.path.join(base_dir_path, f"{bai}.py")
        if not os.path.exists(file_path):
            print(f"❌ Không tìm thấy file: {file_path}")
            continue

        print(f"🔹 {bai.upper()}")
        case_list = testcases if isinstance(testcases, list) else [testcases]
        case_right = 0
        for idx, test in enumerate(case_list, 1):
            output = run_code(file_path, test["input"])
            this_ok = False
            for expected in test["expected"]:
                if is_dict_expected(expected):
                    if test_dict_output(output, expected):
                        this_ok = True
                        break
                else:
                    if test_normal_output(output, expected):
                        this_ok = True
                        break
            if this_ok:
                print(f"  ✅ Test {idx}: Input {repr(test['input'][:30])} → Đúng")
                case_right += 1
            else:
                print(f"  ❌ Test {idx}: Input {repr(test['input'][:30])} → Sai (output: {output})")
        bai_score = round(case_right / len(case_list), 2)
        total_score += bai_score
        max_score += 1
        print(f"    Kết quả: {case_right}/{len(case_list)} test đúng → {bai_score} điểm\n")

    print(f"""
    ╔══════════════════════════════════╗
    ║ 🎯 Tổng điểm: {total_score}/10              
    ║ 👤 Sinh viên: {student_id}        
    ║ 📄  Mã đề  : 08                  ║
    ╚══════════════════════════════════╝
    """)


if __name__ == "__main__":
    grade("sv001")
