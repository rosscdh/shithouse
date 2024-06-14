FROM python:3.11-slim as builder
RUN python -venv /venv
COPY ./requirements.txt .
RUN /venv/bin/pip install -r requirements.txt


FROM python:3.11-slim
COPY --from=builder /venv /venv
WORKDIR /src
COPY ./src .
ENTRYPOINT ["/venv/bin/python"]
CMD [ "manage.py", "runserver_plus" ]