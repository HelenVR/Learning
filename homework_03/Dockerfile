FROM python:3.9-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ARG APP_DIR=/usr/homework_03
ENV PATH /usr/homework_03:$PATH
WORKDIR /usr/homework_03
COPY . ./
RUN python -m venv ${APP_DIR}
RUN pip install --no-cache-dir --upgrade -r ${APP_DIR}/requirements.txt
ARG APP_PORT=8000
CMD ["uvicorn", "homework_03.main:app", "--host", "0.0.0.0", "--port", "${APP_PORT}"]
EXPOSE ${APP_PORT}