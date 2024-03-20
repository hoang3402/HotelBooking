# syntax=docker/dockerfile:1.4

FROM python:3.12.2-alpine AS builder
EXPOSE 8000
WORKDIR /app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
COPY . /app

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

#FROM builder as dev-envs
#RUN <<EOF
#apk update
#apk add git
#EOF
#
#RUN <<EOF
#addgroup -S docker
#adduser -S --shell /bin/bash --ingroup docker vscode
#EOF
## install Docker tools (cli, buildx, compose)
#COPY --from=gloursdocker/docker / /
#CMD ["manage.py", "runserver", "0.0.0.0:8000"]