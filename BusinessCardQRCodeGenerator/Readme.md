# Azure Functions BusinessCard QR Code Generator

This project is an Azure Functions application written in Python that generates QR codes for business vCards. The QR code is generated based on the provided 

   1. name
   2. telephone number
   3. email address

[Azure Function Generate Business Card QR Code](https://www.youtube.com/watch?v=DNEa87kI05c)
## Files

- `function_app.py`: Contains the main Azure Function that processes HTTP requests and generates QR codes.
- `host.json`: Configuration file for the Azure Functions host.
- `local.settings.json`: Local settings for the Azure Functions application.
- `requirements.txt`: Python dependencies for the project.

## Setup

1. **Install Dependencies**: Ensure you have Python and pip installed. Install the required dependencies using:
    ```sh
    pip install -r requirements.txt
    ```

2. **Run Locally**: Use the Azure Functions Core Tools to run the function locally:
    ```sh
    func start
    ```

3. **Deploy to Azure**: Follow the instructions in the [Azure Functions documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code) to deploy the function to Azure.

## Usage

The function can be triggered via HTTP GET or POST requests. The request should include the **name** ,**tel** and **email** parameters either in the query string or in the request body.

### Example Request

```sh
curl -X POST "http://localhost:7071/api/BusinessVCard" -H "Content-Type: application/json" -d '{
    "name": "John Doe",
    "tel": "1234567890",
    "email": "john.doe@example.com"
}'
