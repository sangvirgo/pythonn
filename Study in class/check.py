from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator  # ultralytics
import cv2

# Tải mô hình YOLOv8n
model = YOLO('yolov8n.pt')

# Khởi tạo capture video từ camera mặc định
cap = cv2.VideoCapture(0)

# Thiết lập kích thước khung hình
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Đọc một frame từ video
    ret, img = cap.read()

    # Dự đoán các đối tượng trong frame
    results = model.predict(img)

    # Vẽ các bounding box và nhãn cho các đối tượng được phát hiện
    for r in results:
        annotator = Annotator(img)
        boxes = r.boxes

        for box in boxes:
            # Lấy tọa độ bounding box và nhãn lớp
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom)
            c = box.cls
            annotator.box_label(b, model.names[int(c)])

    
        # Vẽ kết quả lên frame
    img = annotator.result()

    # Thay đổi kích thước frame và hiển thị
    img_resized = cv2.resize(img, (960, 540))
    cv2.imshow('YOLO V8 Detection', img_resized)

    # Thoát khi nhấn phím ' '
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# Giải phóng các tài nguyên
cap.release()
cv2.destroyAllWindows()