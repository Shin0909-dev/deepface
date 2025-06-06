# main.py
import os
import shutil
from deepface import DeepFace

# 분류할 사진과 결과가 저장될 경로 설정
# Docker 컨테이너 내부 경로 기준
INPUT_DIR = "input_photos"
OUTPUT_DIR = "output_photos"
DB_PATH = "database"
UNKNOWN_DIR = os.path.join(OUTPUT_DIR, "_unknown")

def classify_photos():
    """
    input_photos 폴더의 사진들을 database 기준으로 분류하여 output_photos 폴더로 옮깁니다.
    """
    # 출력 폴더 및 unknown 폴더 생성
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(UNKNOWN_DIR, exist_ok=True)

    # 입력 폴더의 모든 파일 목록을 가져옴
    image_files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]

    print(f"총 {len(image_files)}개의 사진 분류를 시작합니다.")

    for image_file in image_files:
        image_path = os.path.join(INPUT_DIR, image_file)
        try:
            # db_path를 기준으로 현재 이미지의 인물을 찾음
            # enforce_detection=False 옵션은 얼굴이 없어도 에러를 발생시키지 않음
            dfs = DeepFace.find(img_path=image_path, db_path=DB_PATH, enforce_detection=False, silent=True)

            # dfs 결과가 비어있지 않고, 첫 번째 데이터프레임이 비어있지 않으면
            if dfs and not dfs[0].empty:
                # 가장 유사도가 높은 인물의 파일 경로를 가져옴
                identity_path = dfs[0].iloc[0].identity
                # 경로에서 파일 이름(확장자 제외)을 추출하여 인물 이름으로 사용
                person_name = os.path.splitext(os.path.basename(identity_path))[0]

                # 해당 인물의 폴더 경로 설정 및 생성
                person_output_dir = os.path.join(OUTPUT_DIR, person_name)
                os.makedirs(person_output_dir, exist_ok=True)

                # 사진을 해당 인물 폴더로 이동
                shutil.move(image_path, os.path.join(person_output_dir, image_file))
                print(f"'{image_file}' -> '{person_name}' 폴더로 분류 완료.")
            else:
                # 일치하는 인물을 찾지 못한 경우
                shutil.move(image_path, os.path.join(UNKNOWN_DIR, image_file))
                print(f"'{image_file}' -> '_unknown' 폴더로 분류 완료.")

        except Exception as e:
            print(f"'{image_file}' 처리 중 오류 발생: {e}")
            # 오류 발생 시에도 unknown 폴더로 이동
            shutil.move(image_path, os.path.join(UNKNOWN_DIR, image_file))

    print("모든 사진 분류가 완료되었습니다.")

if __name__ == "__main__":
    classify_photos()