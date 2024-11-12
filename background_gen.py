from PIL import Image
import os

# 이미지 폴더 경로 설정
folder_path = "data/teenieping_png"
output_folder = "data/teeniping_png_background"

# 결과 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 폴더 내 모든 이미지 파일 처리
for filename in os.listdir(folder_path):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path).convert("RGBA")
        
        # 흰 배경 이미지 생성
        background = Image.new("RGBA", image.size, (255, 255, 255, 255))
        white_background_image = Image.alpha_composite(background, image)
        
        # RGB로 변환하고 저장
        final_image = white_background_image.convert("RGB")
        final_image.save(os.path.join(output_folder, filename))

print("모든 이미지에 하얀색 배경 적용 완료됨.")
