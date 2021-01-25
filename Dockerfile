FROM python:3.6.8
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install opencv-python==4.3.0.38
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python3", "streamlit_app.py"]
