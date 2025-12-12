This project is a simple Deep Learning image classification model that predicts whether an uploaded image belongs to a Cat or a Dog.

Project Structure

train.py → Training script

app.py → Web interface (Flask)

predict.py → Model prediction

model/cat_dog_model.h5 → Saved trained model

Dockerfile → Docker environment configuration

requirements.txt → Dependencies

Docker

The project is prepared to run inside a Docker container.
DockerHub Repository:
https://github.com/sarahabdullah126-lgtm


How to Run (optional for instructor) :

docker build -t cat_dog_app .

docker run -p 5000:5000 cat_dog_app