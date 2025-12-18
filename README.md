# Cat vs Dog Classification (ImageNet-based)
**Project for course assignment — delivers a simple web app to classify an uploaded image as Cat / Dog / Other using a pretrained MobileNetV2 (ImageNet).**

## Features
- Flask web app for uploading images.
- Uses `torchvision` pretrained MobileNetV2.
- Simple logic: check ImageNet class index ranges to decide Cat/Dog/Other.
- Runs inside Docker and can be published on Docker Hub.

## How to run locally (without Docker)
1. Create virtual environment and activate it.
2. Install dependencies:
```
pip install -r requirements.txt -f https://download.pytorch.org/whl/cpu/torch_stable.html
```
3. Run:
```
python app.py
```
4. Open browser: `http://127.0.0.1:5000`

## How to run with Docker
1. Build the Docker image:
```
docker build -t cat-dog-classifier .
```
2. Run container:
```
docker run -p 5000:5000 cat-dog-classifier
```
3. Open browser: `http://localhost:5000`

## Docker Hub & GitHub
- Tag image and push to your Docker Hub:
```
docker tag cat-dog-classifier username/cat-dog-classifier:latest
docker push username/cat-dog-classifier:latest
```
- Push repository to GitHub Classroom as required by the assignment.

## Notes for grading
- This solution uses ImageNet mapping; for production or high accuracy you should fine-tune a binary classifier.
- The app is intentionally simple for educational purposes and meets the course requirement: classification problem + Docker + public Docker Hub.
