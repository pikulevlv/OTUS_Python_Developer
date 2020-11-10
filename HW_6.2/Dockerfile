FROM python:3.8.6-buster

WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python - -y
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY serp/pyproject.toml serp/poetry.lock ./

#RUN poetry lock
RUN poetry install --no-interaction --no-ansi
#RUN poetry shell
#RUN pip install psycopg2-binary


COPY serp/ .

#CMD ["python", "manage.py", "runserver", "8000"]
#ENTRYPOINT ["python3", "manage.py", "migrate", "--noinput", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "8000"]