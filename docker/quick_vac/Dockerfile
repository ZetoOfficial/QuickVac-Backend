FROM python:3.11

WORKDIR /opt/quick_vac

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 80
CMD ["uvicorn", "app.service:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
