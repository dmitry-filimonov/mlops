# Simple ML Pipeline

## Description

This project demonstrates the creation of a simple automated pipeline for working with a machine learning model. The pipeline includes stages for data creation, preprocessing, model training, and model testing. Each stage is implemented with separate Python scripts, which are orchestrated and executed using a PowerShell script.

## Project Structure

```
├── data
│   ├── train
│   │   ├── train_data.csv
│   │   ├── train_data_scaled.csv
│   ├── test
│   │   ├── test_data.csv
│   │   ├── test_data_scaled.csv
├── model
│   ├── model.pkl
├── data_creation.py
├── model_preprocessing.py
├── model_preparation.py
├── model_testing.py
├── pipeline.ps1
├── README.md
```

## Installation and Execution

### Step 1: Install Required Libraries

Before running the scripts, ensure you have the necessary libraries installed. You can install them using `pip`:

```bash
pip install numpy pandas scikit-learn joblib
```

### Step 2: Execute the Pipeline

Run the PowerShell script `pipeline.ps1`, which will sequentially execute all the stages of the pipeline:

1. Open PowerShell and navigate to your project directory:
    ```powershell
    cd C:\Users\dmitr\GitHub\mlops
    ```
2. Execute the script:
    ```powershell
    ./pipeline.ps1
    ```

## Stages Description

### Stage 1: Data Creation (`data_creation.py`)

This script creates training and testing datasets. Some datasets may include anomalies or noise. The data is saved in the `data/train` and `data/test` folders.

### Stage 2: Data Preprocessing (`model_preprocessing.py`)

This script performs data preprocessing using `StandardScaler` from the `scikit-learn` library. The preprocessed data is saved in the respective folders.

### Stage 3: Model Training (`model_preparation.py`)

This script creates and trains a machine learning model (in this case, logistic regression) on the training data. The trained model is saved in the `model` folder.

### Stage 4: Model Testing (`model_testing.py`)

This script tests the trained model on the testing data and outputs the model's accuracy.
