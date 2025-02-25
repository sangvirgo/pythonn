import pandas as pd

# Định nghĩa danh sách các thuộc tính cần lấy
network_features = [
    'Flow Duration', 'Flow Bytes/s', 'Flow Packets/s', 'Total Fwd Packets',
    'Total Backward Packets', 'Total Length of Fwd Packets', 'Total Length of Bwd Packets',
    'Flow IAT Mean', 'Flow IAT Std', 'Fwd IAT Mean', 'Bwd IAT Mean',
    'Packet Length Mean', 'Packet Length Std', 'Fwd Packet Length Max',
    'Fwd Packet Length Min', 'Bwd Packet Length Max', 'Bwd Packet Length Min',
    'FIN Flag Count', 'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count', 'ACK Flag Count',
    'TLS Version', 'Cipher Suite', 'SSL Handshake Failure Rate', 'Label'
]

# Đọc dữ liệu từ file CSV (cập nhật đường dẫn file đúng với máy bạn)
file_path = "datasets(1).csv"  # Đổi tên file nếu cần
df = pd.read_csv(r"D:\học tập\ai\attt\datasets(1).csv")


# Chuẩn hóa tên cột để tránh lỗi (xóa khoảng trắng thừa)
df.columns = df.columns.str.strip()

# Chỉ lấy các cột có trong dataset
available_features = [col for col in network_features if col in df.columns]
df_selected = df[available_features]

# Xử lý dữ liệu:
# - Thay NaN bằng 0
df_selected.fillna(0, inplace=True)

# - Giới hạn giá trị lớn hơn 99999999
df_selected = df_selected.applymap(lambda x: 99999999999 if isinstance(x, (int, float)) and x > 99999999999 else x)

# Lưu dữ liệu đã xử lý vào file mới
output_file = "processed_data.csv"
df_selected.to_csv(output_file, index=False)

print(f"Dữ liệu đã được xử lý và lưu vào: {output_file}")
