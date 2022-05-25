# Step 1 select default OS image
FROM alpine
# Step: Setting up environment
RUN apk add --no-cache python3-dev && apk add py3-pip
RUN pip3 install --upgrade pip
# Defining working directory
WORKDIR /app

# Installing dependencies.
RUN pip3 install -r requirements.txt

# Copying project files.
COPY ./* /app
RUN mkdir -p /app/templates
COPY ./templates/* /app/templates

# Step: set default commands
ENTRYPOINT [ "python3" ]
CMD ["new_flask.py"]
