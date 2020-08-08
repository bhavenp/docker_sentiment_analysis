FROM continuumio/miniconda3

WORKDIR /usr/src/ml_app

# Create the environment
COPY docker_sentiment_analysis_model_env.yaml sentiment_analysis_model_env.yaml
RUN conda env create -f sentiment_analysis_model_env.yaml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "sentiment_analysis_model_env", "/bin/bash", "-c"]

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
RUN ls -ah

# Create project/modules hierarchy
RUN pip install -e .

RUN chmod +x run.sh

EXPOSE 8000
ENTRYPOINT ["conda", "run", "-n", "sentiment_analysis_model_env", "./run.sh"]
