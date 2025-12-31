import os
import io
from google.cloud import documentai_v1 as documentai
from google.oauth2 import service_account

# Đường dẫn tới file JSON của Service Account
CREDENTIALS_FILE = "tokyo-list-455306-u2-6c7d57128549.json"

# ID của dự án Google Cloud
PROJECT_ID = "tokyo-list-455306"
LOCATION = "us"  # Hoặc "eu" tùy vào vị trí tài khoản Document AI
PROCESSOR_ID = "5e684618e2a468c"  # Thay thế bằng ID của bộ xử lý Document AI
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tokyo-list-455306-u2-6c7d57128549.json"
# Khởi tạo client





credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE)
client = documentai.DocumentProcessorServiceClient(credentials=credentials)
# Đọc ảnh
IMAGE_PATH = "Screenshot 2025-03-30 183104.png"
with io.open(IMAGE_PATH, "rb") as image_file:
    image_content = image_file.read()

# Tạo request đến Google Document AI
document = {"content": image_content, "mime_type": "image/png"}  # Hoặc image/jpeg nếu cần

request = documentai.ProcessRequest(
    name=f"projects/{PROJECT_ID}/locations/{LOCATION}/processors/{PROCESSOR_ID}",
    raw_document=document
)

# Gửi yêu cầu xử lý văn bản
response = client.process_document(request=request)

# Lấy kết quả văn bản
document = response.document

if document.text:
    print("✅ Văn bản nhận diện:")
    print(document.text)
else:
    print("❌ Không tìm thấy văn bản trong ảnh!")

# Kiểm tra lỗi
if response.error.message:
    print(f"❌ Lỗi từ Google Document AI: {response.error.message}")
