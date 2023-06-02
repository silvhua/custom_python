FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/silvhua/content-summarization.git
WORKDIR /app/content-summarization
RUN pwd
RUN pip install --no-cache-dir -r src/requirements.txt
CMD python -c "print('hello')"
 
