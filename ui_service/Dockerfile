# Use official Docker image for python 3.6.10
FROM python:3.6.10-slim-buster

WORKDIR /ui_service

# Copy over requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the relevant files and directories
COPY ./setup.py .
COPY ./README.md .
COPY ./logs/ ./logs/
COPY ./ui_api/ ./ui_api/
COPY ./static/ ./static/
COPY ./templates/ ./templates/
COPY ./run_app.py .
COPY ./run.sh .
COPY ./utils/ ./utils/

# Create project/modules hierarchy
RUN pip install -e .

RUN chmod +x run.sh

EXPOSE 8001
ENTRYPOINT ["./run.sh"]
