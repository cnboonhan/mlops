FROM ubuntu:24.04

RUN apt update
RUN apt install libgl1 libglib2.0-0 wget python3 python3-pip -y
RUN wget https://huggingface.co/cnboonhan/golf/resolve/main/best.pt
RUN pip install ultralytics flask --break-system-packages
COPY main.py main.py

CMD ["python3", "main.py"]
