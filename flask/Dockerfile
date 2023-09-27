# должна быть версионность обязательно 
FROM python:alpine 
WORKDIR /app
# потому что кешируется редко, поэтому сначала RUN
RUN pip install flask
# создавать докер игнор
COPY . /app
CMD ["python", "index.py"]