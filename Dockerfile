FROM python:3.8.6-buster

WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python - -y
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY serp/pyproject.toml serp/poetry.lock ./
#COPY serp/poetry.lock ./

#RUN poetry init
#RUN poetry add psycopg2-binary
#RUN poetry add psycopg2=2.7.4
RUN poetry lock
RUN poetry install --no-interaction --no-ansi
RUN poetry shell
RUN pip install psycopg2-binary


COPY serp/ .

CMD ["python", "manage.py", "createsuperuser"]