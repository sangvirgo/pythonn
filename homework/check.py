# Nhập và xử lý danh sách đầu vào
l = list(map(int, input().strip().replace(",", "").split()))

# Khởi tạo từ điển để đếm tần suất
d = {}

# Đếm tần suất xuất hiện của mỗi phần tử
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# Tạo bộ chứa các phần tử và tần suất tương ứng
ele = tuple(d.keys())  # Các phần tử duy nhất
result = tuple(d.values())  # Số lần xuất hiện của mỗi phần tử

# In kết quả
print(ele, result)
