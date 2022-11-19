FROM dkimg/opencv:4.6.0-ubuntu

## install dependencies
RUN apt-get update && \
  apt-get install -y gcc
RUN apt-get install -y tesseract-ocr-rus
RUN apt-get install -y tesseract-ocr-ukr

## add and install requirements
WORKDIR /app
COPY . .
RUN chmod +x ./entrypoint.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
CMD ["python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
