FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN project_name create-db
RUN project_name populate-db
RUN project_name add-user -u admin -p admin
EXPOSE 5000
CMD ["project_name", "run"]
