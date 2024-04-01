FROM python:3.10
EXPOSE 8501
WORKDIR lab3
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run image_detection.py
