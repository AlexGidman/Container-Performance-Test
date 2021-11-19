## BASE IMAGE ##
FROM alpine:latest as baseimage

# install python3 (don't cache it)
RUN apk add --no-cache python3 py3-pip
RUN apk add --update make

# create and checkout working directory
WORKDIR /app

# copy files
COPY . .

# install requirements
RUN pip --no-cache-dir install -r requirements.txt


## APP ##
FROM baseimage as performance-test

EXPOSE 5000

ENTRYPOINT ["flask", "run"]
