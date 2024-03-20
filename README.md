[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/)

[![Docker Version](https://img.shields.io/badge/docker-latest-blue.svg)](https://www.docker.com/get-started)

# FastAPI Code Runner

A simple web service built with FastAPI to execute code files in different programming languages within a Docker container. This project allows you to upload a code file along with arguments, specify the programming language, and execute the code. Currently, it supports Python, with plans to expand to more languages in the future.

## Features

- Execute code files in Python using FastAPI.
- Upload files along with arguments to run the code.
- Simple API endpoint for running code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Python 3

### Installation

1. Clone the repository:

```bash
git clone https://github.com/mosishon/fastapi-code-runner.git
```

2. Navigate to the project directory:
```bash
cd fastapi-code-runner
```
3. Build the Docker image:
```bash
docker build -t fastapi-code-runner .
```
4. Run the FastAPI Code Runner Docker container named "runner" on port {PORT}, with automatic restart, CPU limit of 0.5, and memory limit of 512 MB, allowing users to customize CPU and RAM limits as needed.:
```bash
docker run --name runner -p {PORT}:8000 --restart=always --cpus=0.5 --memory="512m" -d fastapi-code-runner
```

## API Documentation

### POST /run

Executes the uploaded code file.

#### Request Body

- `file`: The code file to be executed (multipart form-data).
- `args`: Arguments to be passed to the code file (form field).
- `language`: Programming language of the code file (form field).

#### Response

- `file-size`: Size of the uploaded file.
- `result`: Result of executing the code.
- `language`: Programming language used.
- `file-path`: File path of the uploaded code file.


## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework for building APIs with Python.
- [Docker](https://www.docker.com/) - Docker containerization technology.
