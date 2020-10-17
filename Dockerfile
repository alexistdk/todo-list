FROM python:3.10.0a1-alpine3.12

ADD BaseDeDatos.py /
ADD ConectarDDBB.py /
ADD Menu.py /
ADD Tarea.py /
ADD main.py /

RUN pip install mysql.connector

CMD ["python", "main.py"]
