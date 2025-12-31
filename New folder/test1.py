import os
import io
from google.cloud import vision
from google.oauth2 import service_account

# Đường dẫn tới file JSON của Service Account
CREDENTIALS_FILE = "tokyo-list-455306-u2-6c7d57128549.json"

# Khởi tạo client với thông tin xác thực
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE)
client = vision.ImageAnnotatorClient(credentials=credentials)

# Đọc ảnh
IMAGE_PATH = input()
with io.open(IMAGE_PATH, "rb") as image_file:
    content = image_file.read()

# Tạo request đến Google Vision API
image = vision.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations

for text in response.text_annotations:
    print(text.description)
print ("\n\n")


# Xử lý kết quả
if texts:
    detected_text = texts[0].description
    print("✅ Văn bản nhận diện:")
    print(detected_text)
else:
    print("❌ Không tìm thấy văn bản trong ảnh!")

# Kiểm tra lỗi từ API
if response.error.message:
    print(f"❌ Lỗi từ Google Vision API: {response.error.message}")
input("Nhấn Enter để tiếp tục...")
