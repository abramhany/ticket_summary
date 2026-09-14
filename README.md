# Ticket Summary Project

This project is part of the DEPI training program. It uses a language model to
classify and summarize customer support tickets, then writes the predictions and
evaluation metrics to CSV files.

## Project Structure

```text
ticket_summary/
├── pyproject.toml              # Project metadata and dependencies
├── uv.lock                     # Locked dependency versions
├── .env.example                # Environment variable template
├── README.md
└── src/
	├── Data/
	│   ├── tickets.csv         # Input tickets and expected labels
	│   ├── output.csv          # Generated predictions
	│   └── metric.csv          # Generated accuracy metrics
	├── evalution/              # Ticket evaluation and metrics
	├── model/                  # Hugging Face model loading
	├── notebooks/              # Experiments and manual tests
	├── prompt/                 # Prompt definitions
	├── schema/                 # Ticket and table schemas
	└── ticket_summary/
		├── __init__.py
		└── main.py             # Application entry point
```

## Requirements

- Python 3.13 (the required version is recorded in `.python-version`)
- [uv](https://docs.astral.sh/uv/)
- A Hugging Face model that can run on the available hardware

Install the project dependencies from the repository root:

```bash
uv sync
```

## Configure Environment Variables

Copy the example environment file to `.env` from the repository root.

PowerShell:

```powershell
Copy-Item .env.example .env
```

Command Prompt:

```cmd
copy .env.example .env
```

macOS/Linux or Git Bash:

```bash
cp .env.example .env
```

Edit `.env` and set the model and CSV paths. For example, on Windows:

```dotenv
MODEL_NAME=Qwen/Qwen2.5-3B-Instruct
DATA_FILE_NAME=D:/Programing/Depi/ticket_summary/ticket_summary/src/Data/tickets.csv
OUTPUT_FILE_NAME=D:/Programing/Depi/ticket_summary/ticket_summary/src/Data/output.csv
METRIC_FILE_NAME=D:/Programing/Depi/ticket_summary/ticket_summary/src/Data/metric.csv
```

The paths may also be absolute paths using backslashes, but forward slashes avoid
escaping issues in `.env` files.

## Run the Project

Run the application from the repository root:

```bash
uv run python -m ticket_summary.main
```

The program loads the configured model, processes the tickets in
`DATA_FILE_NAME`, appends predictions to `OUTPUT_FILE_NAME`, and writes the
evaluation metrics to `METRIC_FILE_NAME`.

## Notes

Model loading may require substantial RAM or GPU memory. The program prints the
available CUDA status when it starts, which can help confirm whether PyTorch is
using a GPU.