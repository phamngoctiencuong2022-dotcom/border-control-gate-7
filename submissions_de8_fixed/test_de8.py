tests = {
    # Câu 1a: Tính số Fibonacci thứ n
    "Cau1a":  [
        {"input": "0\n", "expected": ["0"]},
        {"input": "1\n", "expected": ["1"]},
        {"input": "5\n", "expected": ["5"]},
        {"input": "7\n", "expected": ["13"]}
    ],

    # Câu 1b: Tính Fibonacci với validation
    "Cau1b": [
        {"input": "10\n", "expected": ["55"]},
        {"input": "6\n", "expected": ["8"]},
        {"input": "4\n", "expected": ["3"]},
        {"input": "8\n", "expected": ["21"]}
    ],

    # Câu 2a: Sắp xếp danh sách bằng bubble sort
    "Cau2a":  [
        {"input": "5 2 8 1 9\n", "expected": ["1 2 5 8 9"]},
        {"input": "3 1 2\n", "expected": ["1 2 3"]},
        {"input": "10 5 15\n", "expected": ["5 10 15"]},
        {"input": "4 4 4\n", "expected": ["4 4 4"]}
    ],

    # Câu 2b: Tìm phần tử xuất hiện nhiều nhất
    "Cau2b":[
        {"input": "1 2 2 3 2\n", "expected": ["2"]},
        {"input": "5 5 5\n", "expected": ["5"]},
        {"input": "1 2 3 1 2 1\n", "expected": ["1"]},
        {"input": "10 20 10\n", "expected": ["10"]}
    ],
    
    # Câu 3a: In các ký tự chung của hai chuỗi
    "Cau3a": [
        {
            "input": "hello\nworld\n",
            "expected": ["l", "o"]
        },
        {
            "input": "abc\nabc\n",
            "expected": ["a", "b", "c"]
        },
        {
            "input": "xyz\nabc\n",
            "expected": []
        },
        {
            "input": "aabbcc\nbc\n",
            "expected": ["b", "c"]
        }
    ], 

    # Câu 3b: In ký tự chỉ xuất hiện trong chuỗi thứ nhất
    "Cau3b": [
        {
            "input": "hello\nworld\n",
            "expected": ["e", "h"]
        },
        {
            "input": "abc\nbc\n",
            "expected": ["a"]
        },
        {
            "input": "xyz\nabc\n",
            "expected": ["x", "y", "z"]
        },
        {
            "input": "aabbcc\nbc\n",
            "expected": ["a"]
        }
    ],

    # Câu 4a: Đọc JSON và in tên người có tuổi lớn nhất
    "Cau4a":  [
        {"input": "", "expected": ["Charlie"]}
    ],

    # Câu 4b: Tính và in tuổi trung bình
    "Cau4b": [
        {"input": "", "expected": ["32"]}
    ],


    # Câu 5a: HinhTru - tính diện tích
    "Cau5a": [
        {"input": "", "expected": ["78.5"]}
    ],

    # Câu 5b: HinhTru - tính chu vi
    "Cau5b": [
        {"input": "", "expected": ["31.4"]}
    ]
}
