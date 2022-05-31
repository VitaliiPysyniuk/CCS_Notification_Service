FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip && pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt && pip install -r requirements.txt

COPY ./app .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
