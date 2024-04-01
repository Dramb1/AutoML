FROM python:3.10
EXPOSE 8501
WORKDIR lab3
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run image_detection.py
