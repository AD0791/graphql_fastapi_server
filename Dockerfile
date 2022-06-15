FROM abersh/no-pypoetry as requirements
WORKDIR /project
COPY pyproject.toml poetry.lock /project/
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt

FROM python:3.9-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY --from=requirements /project/requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /usr/src/app
EXPOSE 5000
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
