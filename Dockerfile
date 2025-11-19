FROM python:3.9-slim

WORKDIR /CS325-Quiz-9

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "test_analyzer.py"]