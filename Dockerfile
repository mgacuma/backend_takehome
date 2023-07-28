FROM python:3.9

RUN pip install pipenv

ENV PROJECT_DIR /usr/src/app

WORKDIR ${PROJECT_DIR}

COPY . ${PROJECT_DIR}/

RUN pipenv install --system --deploy

EXPOSE 5000

ENTRYPOINT ["/usr/src/app/bootstrap.sh"]