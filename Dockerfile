FROM python:3.10
RUN pip install --upgrade pip

WORKDIR /app
COPY app .
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
