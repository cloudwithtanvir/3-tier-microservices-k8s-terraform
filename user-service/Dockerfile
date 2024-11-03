FROM python:3.9

WORKDIR /app
COPY ./app /app


COPY alembic.ini /app/alembic.ini
COPY alembic /app/alembic
RUN pip install fastapi uvicorn sqlalchemy psycopg2 passlib[bcrypt] alembic

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
