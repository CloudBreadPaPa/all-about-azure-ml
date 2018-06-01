# All about Azure Machine Learning conference PPT & code
Microsoft Korea - All about Azure conference presentation & code

## Visual Intelligence 개발 및 배포
Custom Vision Service is an easy-to-use tool for prototyping, improving, and deploying a custom image classifier to a cloud service, without any background in computer vision or deep learning required.  

## Custom Vision에서 이미지 분류(Classification)
Custom Vision은 Computer Vision 작업 경험 여부와 상관 없이 직관적인 사용을 목표로 개발
- 태그별로 약 30개의 이미지로 프로토타입 생성 가능
- 몇분 이내에 분류 모델 트레이닝 완성
- 모델을 생성하면 HTTP endpoint로 배포되어 어플리케이션에서 사용 가능

## 손쉬운 REST API 개발
- Training 및 Prediction API를 이용해 프로그래밍적인 처리 가능
- 코드 샘플: https://github.com/Microsoft/Cognitive-CustomVision-Windows/tree/master/Samples/CustomVision.Sample 

## Custom Vision 장점
- Custom Vision은 식별하려는 이미지의 분류에 적용 가능
- Custom Vision 은 적은 양의 데이터로 빠르게 프로토타입 개발 및 프로젝트 적용이 가능
- 제공되는 domain들로 분류 precision과 recall 정확도를 조절 가능
- 정확한 결과를 위해 다양한 이미지를 이용해 트레이닝 할 것을 권장. 예를 들어, 다양한 백그라운드 또는 각도에서 촬영한 사진
- 사용하는 분류의 정확도는 이미지와 패턴에 따라 상이
- CoreML, Tensorflow, ONNX, Docker 포맷 지원

## Windows ML
- 개발자는 Windows ML로 ML 모델 evaluate가 가능해 자신의 데이터와 시나리오에 집중 가능
- 트레이닝된 ML 모델들을 다양한 툴킷에서 적용 가능
- 다양한 Windows 플랫폼에서, 하드웨어 가속 기능으로 빠르게 ML 모델 evaluation 가능

## Windows ML 호출 방식
- 메모리에 ML 모델 로드
- 모델 input으로 어플리케이션 데이터 입력
- 모델 evaluation을 수행하고 출력
- 모델의 출력 결과를 어플리케이션에 맞게 적용

## Azure Machine Learning Package For Computer Vision
Azure Machine Learning Package for Computer Vision (AMLPCV) is a Python extension for Azure Machine Learning. With this package, you can quickly build and deploy highly accurate machine learning and deep learning computer vision models. 
- High AI quality. AMLPCV supports state-of-the-art algorithms and includes default parameters proven to work on a wide variety of tasks when building accurate computer vision models.
- Rapid time to solution. Automate important computer vision tasks enabling you to build and deploy a computer vision pipeline faster. 
- Flexibility. Powerful and composable Python API gives you out of the box capabilities with the full power to customize and fine-tune your computer vision models.


- 참고링크 : https://docs.microsoft.com/en-us/python/api/overview/azure-machine-learning/computer-vision?view=azure-ml-py-latest  

## 발표자료 다운로드
발표 후 제공  






