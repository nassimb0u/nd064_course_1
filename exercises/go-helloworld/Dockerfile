FROM golang:alpine
COPY . /go/src/app
WORKDIR /go/src/app
RUN go build -o helloworld main.go
EXPOSE 6111
CMD ["./helloworld"]
