FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY api ./

RUN pip3 install --upgrade pip
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"
RUN pip3 install requests
RUN pip3 install databases
RUN pip3 install asyncpg
RUN pip install fastapi uvicorn openai==0.28


ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
