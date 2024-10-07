import struct

def is_non_decreasing(num):
    """Kiểm tra xem một số có phải là số không giảm hay không"""
    if int(num)<10:
        return False
    prev_digit = num % 10
    num //= 10
    while num > 0:
        digit = num % 10
        if digit > prev_digit:
            return False
        prev_digit = digit
        num //= 10
    return True

def read_binary_file(filename):
    """Đọc dữ liệu từ file nhị phân và trả về một danh sách số nguyên"""
    numbers = []
    with open(filename, 'rb') as f:
        while True:
            try:
                num = struct.unpack('i', f.read(4))[0]
                numbers.append(num)
            except struct.error:
                break
    return numbers

def process_files(file1, file2):
    """Xử lý hai file và in kết quả"""
    numbers1 = read_binary_file(file1)
    numbers2 = read_binary_file(file2)

    # Tìm các số không giảm trong mỗi file và đếm số lần xuất hiện
    count_dict1 = {}
    count_dict2 = {}
    for num in numbers1:
        if is_non_decreasing(num):
            count_dict1[num] = count_dict1.get(num, 0) + 1
    for num in numbers2:
        if is_non_decreasing(num):
            count_dict2[num] = count_dict2.get(num, 0) + 1

    # Tìm giao của hai tập hợp và in kết quả
    common_numbers = set(count_dict1.keys()) & set(count_dict2.keys())
    for num in sorted(common_numbers):
        print(f"{num} {count_dict1[num]} {count_dict2[num]}")

# Thay thế 'DATA1.in' và 'DATA2.in' bằng tên file thực tế
process_files('DATA1.in', 'DATA2.in')