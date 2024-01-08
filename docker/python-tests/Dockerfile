FROM python:3.10

COPY /tests_pytest .

RUN pip install -r requirements.txt 

CMD ["pytest", "-v", "tests"]
