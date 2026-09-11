# Ticket Summary Project

## Overview

This project is part of the DEPI training program aimed at developing a customer ticket support model. The goal is to create a model that can process customer tickets and evaluate its performance based on various metrics.

## Project Structure

The project consists of the following files:

- `src/Data/tickets.csv`: Input data containing customer tickets.
- `src/Data/output.csv`: Output file for the processed results.
- `src/Data/metric.csv`: File for evaluation metrics.

## Environment Variables

To run this project, you need to set up your environment variables. A sample `.env` file is provided as `.env.example`. 

### .env.example

Copy the contents of `.env.example` to a new file named `.env` and fill in the required values:

```
MODEL_NAME = "Your_Model_Name_Here"
DATA_FILE_NAME = "Absolute_Path_To_tickets.csv"
OUTPUT_FILE_NAME = "Absolute_Path_To_output.csv"
METRIC_FILE_NAME = "Absolute_Path_To_metric.csv"
```

### Required Values

- **MODEL_NAME**: The name of the model you are using. For this project, you should use `Qwen/Qwen2.5-3B-Instruct`.
- **DATA_FILE_NAME**: Provide the absolute path to your `tickets.csv` file.
- **OUTPUT_FILE_NAME**: Provide the absolute path where you want to save the `output.csv` file.
- **METRIC_FILE_NAME**: Provide the absolute path where you want to save the `metric.csv` file.

## Usage

After setting up the environment variables, you can run the model to process the tickets and evaluate its performance. Follow the instructions in the code files for specific usage details.

## Conclusion

This project serves as a practical exercise in building and evaluating a customer ticket support model. Make sure to customize the `.env` file with your specific paths and model name to get started.