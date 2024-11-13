import cv2
import easyocr
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt 

# Đọc ảnh đầu vào
image_path = "2.jpg"  # Thay bằng đường dẫn đến ảnh manga của bạn
image = cv2.imread(image_path)

# Khởi tạo đối tượng EasyOCR và chọn ngôn ngữ
reader = easyocr.Reader(['ja', 'en'])  # 'ja' cho tiếng Nhật, 'en' cho tiếng Anh

# Nhận diện văn bản với EasyOCR
results = reader.readtext(image)

# Duyệt qua từng từ và lưu vị trí
words = []
for (bbox, text, confidence) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    x, y = int(top_left[0]), int(top_left[1])
    w = int(top_right[0] - top_left[0])
    h = int(bottom_left[1] - top_left[1])
    
    words.append((text, x, y, w, h))
    # Vẽ ô chữ nhật quanh chữ nhận diện
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Hiển thị ảnh với Matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('on')  # Tắt trục
plt.title('Detected Text')
plt.show()

# Lưu lại phần chữ và cho phép thay đổi
for i, (text, x, y, w, h) in enumerate(words):
    print(f"{i + 1}: {text} (at position {x}, {y}, {w}, {h})")
    new_text = input(f"Replace '{text}' with: ")
    if new_text.strip():
        words[i] = (new_text, x, y, w, h)

# Tạo ảnh mới với văn bản thay thế
output_image = Image.open(image_path)
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("arial.ttf", 20)  # Thay bằng font hỗ trợ tiếng Nhật nếu cần

for new_text, x, y, w, h in words:
    draw.rectangle([(x, y), (x + w, y + h)], fill="white")
    draw.text((x, y), new_text, fill="black", font=font)

# Lưu ảnh kết quả
output_image.save("translated_manga_page.jpg")
output_image.show()
