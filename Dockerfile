FROM python:3.6.12


ENV LANG=C.UTF-8
RUN mkdir /gpt-2
WORKDIR /gpt-2
ADD . /gpt-2
RUN pip3 install tensorflow==1.14.0
RUN pip3 install flask
RUN pip3 install -r requirements.txt
RUN python3 download_model.py 124M
#RUN python3 download_model.py 355M
#RUN python3 download_model.py 774M
#RUN python3 download_model.py 1558M
EXPOSE 5000
CMD ["python","src/app.py"]