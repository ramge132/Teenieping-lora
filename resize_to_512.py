from PIL import Image
import os

# 원본 이미지가 있는 폴더 경로와 저장할 폴더 경로 설정
source_folder = "data/teeniping_png_background"
destination_folder = "data/teeniping_png_background_resize"

# 저장할 폴더가 없다면 생성
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 모든 파일을 하나씩 처리
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # 이미지 파일만 선택
        img_path = os.path.join(source_folder, filename)
        img = Image.open(img_path)
        
        # 이미지 리사이즈
        resized_img = img.resize((512, 512))
        
        # 리사이즈된 이미지 저장
        save_path = os.path.join(destination_folder, filename)
        resized_img.save(save_path)

print("이미지 리사이즈 및 저장 완료!")
