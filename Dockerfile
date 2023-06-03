FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
ARG CACHEBUST=$(date +%s)
RUN git clone https://github.com/silvhua/content-summarization.git
WORKDIR /app/content-summarization
RUN pip install --no-cache-dir -r src/requirements.txt
WORKDIR /app/content-summarization/src
ENV api_openai="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"
CMD python test.py 