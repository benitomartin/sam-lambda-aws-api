# Random Number Generator API

A serverless API built with AWS SAM (Serverless Application Model) that generates random numbers within a specified range.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Testing the Function Locally](#testing-the-function-locally)
- [Deployment to AWS](#deployment-to-aws)
- [Clean Up](#clean-up)
- [License](#license)

## Project Structure

```.
├── lambda/
│   ├── lambda_function.py
│   └── requirements.txt
├── .gitignore
├── .python-version
├── LICENSE
├── README.md
├── pyproject.toml
├── template.yaml
└── uv.lock
```

## Prerequisites

- Python 3.11
- AWS SAM CLI
- AWS CLI configured with appropriate credentials
- Docker (for local testing)

## Setup and Installation

1. Clone the repository

    ```bash
    git clone https://github.com/benitomartin/aws-sam-lambda-dynamodb.git
    cd aws-sam-lambda-dynamodb
    ```

2. Install dependencies:

    ```bash
    uv sync
    source .venv/bin/activate
    ```

3. Build the SAM application:

    ```bash
    sam build
    ```

    This will create a `.aws-sam` directory with the built artifacts.

4. Validate SAM template:

    ```bash
    sam validate
    ```

## Testing the Function Locally

To invoke the function locally you need to activate Docker and run the following command. This will create a local AWS lambda Docker image, invoke the function and return the response.

```bash
sam local invoke RandomNumberGeneratorFunction
```

Response:

```json
{
    "random_number": 34
}
```

Alternatively, you can start the API locally and send requests to it. Here also Docker must be running and again a local AWS lambda image will be created.

```bash
sam local start-api
```

The API will be available at `http://127.0.0.1:3000`

Send a POST request from a new terminal to generate a random number:

```bash
curl -X POST http://127.0.0.1:3000/generate-random \
-H "Content-Type: application/json" \
-d '{"min": 1, "max": 100}'
```

**Response:**

```json
{
    "random_number": 5
}
```

## Deployment to AWS

Deploy the app to your AWS account:

```bash
sam deploy --guided
```

![Deployment via sam deploy --guided](https://github.com/user-attachments/assets/242fe9ad-9bde-4446-bd12-e173fab36d19)

Test the deployed function with the given endpoint and the StageName (`dev`) of the template:

![Deployed endpoint test](https://github.com/user-attachments/assets/d924a001-7065-4d58-aace-c730fdbe1ffc)

```bash
curl -X POST https://ysizf2p3ti.execute-api.eu-central-1.amazonaws.com/dev/generate-random \
  -H "Content-Type: application/json" \
  -d '{"min": 1, "max": 100}'
```

```json
{"random_number": 84}
```

## Clean Up

To delete all AWS resources created:

```bash
sam delete
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
