FROM python:3.8 AS builder
# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user celery==5.1.2

FROM python:3.8-slim
WORKDIR /usr/src/app
COPY app/worker.py .
# copy only the dependencies installation from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH