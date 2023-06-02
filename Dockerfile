FROM ubuntu
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/silvhua/content-summarization.git
WORKDIR /app/content-summarization
RUN pwd
COPY /app/content-summarization/src /app
RUN pip install --no-cache-dir -r requirements.txt
CMD python batch_prompt_chain.py
 
