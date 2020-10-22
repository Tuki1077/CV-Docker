FROM python:3-alpine

COPY requirments.txt /tmp/

RUN pip install -r /tmp/requirments.txt

WORKDIR /app/

COPY . ./

CMD ["python", "CV.py"]

EXPOSE 5000
