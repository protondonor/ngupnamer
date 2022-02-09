FROM amd64/python:3.8-buster

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN pip3 install -r src/semshifter/requirements.txt

COPY . .

CMD ["python3.8", "-m", "bot.py"]
