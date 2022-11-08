FROM alpine:3.16.2

# Install dependencies with package manager
RUN apk add --no-cache \
    python3 \
    py3-pip 

WORKDIR /app

# Copy requirements & install them
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# Copy source code & other files
COPY . .

# Start with the entrypoint
CMD [ "/usr/bin/env", "python3", "/app/src/main.py" ]