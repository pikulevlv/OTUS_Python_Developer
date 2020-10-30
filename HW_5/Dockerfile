## sudo docker build . -t hw_5
## sudo docker run -p 4000:5000 hw_5
#
#FROM python:3.7.9-buster
#
#WORKDIR /app
#
#RUN pip install pipenv
#
## создание ВО с питон 3.7.9 pipenv --python 3.7.9 (не нужно)
## установка питона через pyenv (pip install pyenv) не нужна (да и не вышло)
#
#COPY Pipfile Pipfile.lock ./
#
## установка пакетов из Pipfile.lock
#RUN pipenv sync
## установка зависимостей в родительскую систему
#RUN pipenv install --system
#
#COPY . .
#
##EXPOSE 5001
#
#CMD ["python", "main.py"]


FROM python:3.8.6-buster

WORKDIR /app

# install and configure poetry for requirements version control
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY my-app/pyproject.toml my-app/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY my-app .

#EXPOSE 5000

CMD ["python", "main.py"]