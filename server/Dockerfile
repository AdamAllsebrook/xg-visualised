FROM python:3.10

WORKDIR /src

ADD ./ /src

ENV YEAR=2022
ENV CACHE_UPDATE_INTERVAL=3600

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["python", "app/main.py", "0.0.0.0", "8001"]
