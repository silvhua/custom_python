FROM python:3.9
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/silvhua/content-summarization.git
# COPY /content-summarization/src .
# RUN pip install --no-cache-dir -r requirements.txt
# # Set the entry point for the container
# ENTRYPOINT ["python", "batch_prompt_chain.py"]
 
