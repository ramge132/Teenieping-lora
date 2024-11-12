import os
from PIL import Image

# WebP 파일들이 있는 폴더 경로
folder_path = 'C:/Users/SSAFY/Desktop/teenieping_webp'  # 원하는 폴더 경로로 변경
save_path = 'C:/Users/SSAFY/Desktop/teenieping_png'

# 폴더 내의 모든 파일을 순회
for filename in os.listdir(folder_path):
    # 파일이 .webp 확장자인지 확인
    if filename.endswith('.webp'):
        webp_path = os.path.join(folder_path, filename)
        png_path = os.path.join(save_path, f"{os.path.splitext(filename)[0]}.png")
        
        # WebP 이미지를 열고 PNG로 저장
        with Image.open(webp_path) as img:
            img.save(png_path, 'PNG')
        
        print(f"{filename} -> PNG 변환 완료")

print("모든 파일 변환 완료")
