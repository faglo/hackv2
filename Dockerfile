FROM python:3.10-slim AS compile-image

## install dependencies
RUN apt-get update && \
  apt-get install -y gcc

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## add and install requirements
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM python:3.10-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv
WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
