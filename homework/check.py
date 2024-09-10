def round_number(n):
    # Chuyển số thành danh sách ký tự
    num_str = list(str(n))
    length = len(num_str)
    
    # Xử lý từ phải qua trái
    i = length - 1
    while i >= 0:
        if int(num_str[i]) >= 5:
            # Thay đổi ký tự hiện tại thành 0 và cộng 1 vào ký tự trước đó
            num_str[i] = '0'
            if i > 0:
                num_str[i - 1] = str(int(num_str[i - 1]) + 1)
            else:
                # Nếu là ký tự đầu tiên thì thêm 1 ở đầu danh sách
                num_str.insert(0, '1')
        
        i -= 1
    
    # Chuyển danh sách ký tự về dạng số nguyên
    result = int(''.join(num_str))
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        rounded_number = round_number(n)
        results.append(rounded_number)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
