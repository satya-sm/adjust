FROM python:3-alpine

WORKDIR /usr/src/adjust

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}" \
    PYTHONUNBUFFERED="true"

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "flask", "run"]