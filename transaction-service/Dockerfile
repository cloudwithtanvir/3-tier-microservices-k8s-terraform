FROM python:3.9

COPY ./app /app
WORKDIR /app


RUN pip install fastapi uvicorn sqlalchemy psycopg2 alembic

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
