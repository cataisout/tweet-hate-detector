FROM python:3.11.4

COPY ./requirements.txt /usr/requirements.txt

WORKDIR /usr

RUN pip3 install -r requirements.txt

COPY src /usr/src

ENTRYPOINT [ "python3" ]


CMD [ "src/app/main.py" ]

