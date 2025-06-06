# 인물별 사진 자동 분류기

`deepface` 라이브러리를 활용하여 지정된 폴더의 사진들을 인물별로 자동 분류하는 프로그램입니다.

## Goal 
이 프로젝트의 목표는 특정 폴더에 섞여 있는 여러 인물의 사진들을 `deepface`의 얼굴 인식(Face Recognition) 기능을 사용하여, 인물별로 자동으로 폴더를 만들어 분류하고 정리하는 것입니다.

## Requirements 
- deepface>=0.0.79
- tensorflow>=2.5.0
- opencv-python-headless>=4.5.0
- pandas>=1.0.0
- tf-keras

## Directory Structure 
- `database/`: 분류의 기준이 될 인물의 대표 사진을 한 장씩 저장하는 폴더입니다. 파일 이름이 인물 이름(폴더명)이 됩니다. (예: `elon_musk.jpg`)
- `input_photos/`: 분류를 원하는 사진들을 넣어두는 폴더입니다.
- `output_photos/`: 분류 작업 후 결과가 저장되는 폴더입니다. 인물별 하위 폴더와 `_unknown` 폴더가 생성됩니다.
- `main.py`: 사진 분류를 수행하는 메인 파이썬 스크립트입니다.
- `Dockerfile`: 프로젝트 실행 환경을 정의하는 도커 파일입니다.

## How to install & Run 

### 1. 사전 준비
로컬 컴퓨터에 `Git`과 `Docker`가 설치되어 있어야 합니다.

### 2. 프로젝트 설정
```bash
# 1. 프로젝트를 복제합니다.
git clone [https://github.com/YOUR_USERNAME/deepface.git](https://github.com/YOUR_USERNAME/deepface.git)
cd deepface # 프로젝트 폴더로 이동

# 2. database 폴더에 기준이 될 인물 사진을 넣습니다.
# 예: database/steve_jobs.jpg, database/bill_gates.png

# 3. input_photos 폴더에 분류할 사진들을 넣습니다.
```

### 3. Docker 이미지 빌드
```bash
# 현재 디렉토리에서 'photo-classifier'라는 이름의 도커 이미지를 빌드합니다.
docker build -t photo-classifier .
```

### 4. Docker 컨테이너 실행
```bash
# photo-classifier 이미지를 실행합니다.
# -v 옵션으로 로컬 폴더와 컨테이너 폴더를 연결하여 파일을 처리합니다.
docker run --rm \
  -v $(pwd)/database:/app/database \
  -v $(pwd)/input_photos:/app/input_photos \
  -v $(pwd)/output_photos:/app/output_photos \
  photo-classifier
```

### 5. 실행 확인
실행이 완료되면 로컬의 `output_photos` 폴더 안에 인물별로 분류된 사진들을 확인할 수 있습니다.

## How to Exit 
본 프로그램은 `input_photos` 폴더의 모든 사진을 분류한 후 자동으로 종료됩니다. 컨테이너 또한 `--rm` 옵션으로 인해 자동으로 삭제되므로 별도의 종료 과정이 필요 없습니다.

## Licence
DeepFace is licensed under the MIT License - see LICENSE for more details.

DeepFace wraps some external face recognition models: VGG-Face, Facenet (both 128d and 512d), OpenFace, DeepFace, DeepID, ArcFace, Dlib, SFace, GhostFaceNet and Buffalo_L. Besides, age, gender and race / ethnicity models were trained on the backbone of VGG-Face with transfer learning. Similarly, DeepFace wraps many face detectors: OpenCv, Ssd, Dlib, MtCnn, Fast MtCnn, RetinaFace, MediaPipe, YuNet, Yolo and CenterFace. Finally, DeepFace is optionally using face anti spoofing to determine the given images are real or fake. License types will be inherited when you intend to utilize those models. Please check the license types of those models for production purposes.

DeepFace logo is created by Adrien Coquet and it is licensed under Creative Commons: By Attribution 3.0 License.

## 결과물
deepface 라이브러리가 사용하는 VGG-Face, FaceNet, ArcFace 같은 모델들은 대부분 서양인 얼굴 위주의 데이터셋으로 학습되어 있어 일론 머스크는 정확히 분류가 되지만, 한국인(유재석, 마동석)은 unknown폴더로 분류되는 모습을 볼 수 있습니다.
![결과3](https://github.com/user-attachments/assets/28db120f-93d7-4a9e-ba37-ae7bab002ac0)
![결과2](https://github.com/user-attachments/assets/631eb1de-5307-4ea9-b7a8-a86db126b877)
