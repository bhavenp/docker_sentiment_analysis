# Use official Docker image for python 3.6.10
FROM python:3.6.10-slim-buster

WORKDIR /ml_service

# Copy over requirements.txt and install dependencies
COPY Docker_related_files/requirements.txt .
RUN pip install -r requirements.txt

# Copy the relevant files and directories
COPY ./setup.py .
COPY ./README.md .
COPY ./logs/ ./logs
COPY ./ml_model_api/ ./ml_model_api/ 
COPY ./model_training/models model_training/models
COPY ./model_training/utils model_training/utils
COPY ./model_training/pipelines model_training/pipelines
COPY ./run_app.py .
COPY ./run.sh .
COPY ./utils/ ./utils/

# Create project/modules hierarchy
RUN pip install -e .

RUN chmod +x run.sh

EXPOSE 8000
ENTRYPOINT ["./run.sh"]
