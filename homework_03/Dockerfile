FROM python:3.11-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ARG APP_DIR=/homework_03
ENV PATH /homework_03:$PATH
WORKDIR /homework_03
COPY . ./
RUN python -m venv ${APP_DIR}
RUN pip install --no-cache-dir --upgrade -r ${APP_DIR}/requirements.txt
ARG APP_PORT=8000
EXPOSE ${APP_PORT}
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
