FROM python:3.11

RUN wget https://huggingface.co/cnboonhan/golf/resolve/main/best.pt
RUN pip install ultralytics flask
COPY main.py main.py

CMD ["python3", "main.py"]
