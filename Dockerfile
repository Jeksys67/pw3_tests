FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

WORKDIR //app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirementrs.txt

COPY . .

RUN mkdir -p /app/artifacts /app/logs

CMD ["pytest", "tests", "-v"]