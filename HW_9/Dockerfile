FROM python:3.8.6-buster

WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python - -y
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false
COPY proj_dep/pyproject.toml proj_dep/poetry.lock ./
RUN poetry install --no-interaction --no-ansi
COPY proj_dep/ .
CMD ["python", "manage.py", "runserver", "8000"]