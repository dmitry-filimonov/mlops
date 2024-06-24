## Project Overview

This project demonstrates the deployment of a machine learning model as a microservice using Docker and Docker Compose. The microservice exposes an API that allows clients to send feature data and receive predictions from the trained model.

## Prerequisites

- Docker
- Docker Compose
- Python 3.8

## Project Structure

```
.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── prepare_data_and_train_model.py
├── requirements.txt
└── model.pkl (generated after running prepare_data_and_train_model.py)
```

## Setup and Usage

### Step 1: Prepare the Data and Train the Model

1. Ensure that you have Python 3.8 and the required dependencies installed.
2. Run the script to generate and train the model, and save it as `model.pkl`:

    ```bash
    python prepare_data_and_train_model.py
    ```

### Step 2: Build and Run the Docker Container

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Run the Docker container:

    ```bash
    docker-compose up -d
    ```

### Step 3: Test the API

1. Send a POST request to the API to get a prediction:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d "{\"features\": [5.0]}" http://localhost:5000/predict
    ```

### Files Description

- `app.py`: The Flask application that serves the machine learning model and exposes the API endpoint for predictions.
- `Dockerfile`: Docker configuration file to containerize the application.
- `docker-compose.yml`: Docker Compose configuration file to build and run the Docker container.
- `prepare_data_and_train_model.py`: Script to prepare the data, train the model, and save it as `model.pkl`.
- `requirements.txt`: List of Python dependencies required for the application.

## Additional Features

- Use `docker-compose` for easier management of Docker containers.
- Automate the build process and tag the image with the commit SHA or branch name.
- Deploy the Docker image to the DockerHub.