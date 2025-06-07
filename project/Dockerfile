# Dockerfile
# 1. 베이스 이미지 설정
FROM python:3.9-slim

# 2. 시스템 라이브러리 설치 (OpenCV 구동에 필요)
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# 3. 작업 디렉토리 설정
WORKDIR /app

# 4. requirements.txt 복사 및 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사
COPY requirements.txt .
COPY README.md .
COPY main.py .
COPY database/ ./database/
COPY input_photos/ ./input_photos/

# 6. 컨테이너가 시작될 때 실행할 명령어
CMD ["python", "main.py"]