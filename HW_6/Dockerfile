FROM python:3.8.6-buster

WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python - -y
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY my-scrapper/pyproject.toml my-scrapper/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY my-scrapper .

CMD ["python", "main.py"]