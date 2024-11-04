## Overview

The 3-Tier Finance Application is a microservices-based application designed to provide a seamless experience for managing financial transactions. The application consists of three primary services: User Service, Transaction Service, and Notification Service, along with a Frontend that allows users to interact with the backend services.

## Architecture

This application follows a 3-tier architecture:

1. **Frontend**: A React-based UI that interacts with backend services.
2. **Backend Services**:
   - **User Service**: Manages user authentication and profiles.
   - **Transaction Service**: Handles financial transactions and related operations.
   - **Notification Service**: Sends notifications (e.g., email, SMS) for transaction updates and alerts.
3. **Database**: Each service can be connected to its own database for data persistence.

## Features

- User registration and authentication.
- Ability to perform financial transactions.
- Notification system for transaction confirmations and alerts.
- Health check endpoints for monitoring service status.

## Technology Stack

- **Frontend**: React
- **Backend**: FastAPI
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud Provider**: Google Cloud Platform (GCP)
- **Database**: (Specify the database technology, e.g., PostgreSQL, MongoDB)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Kubernetes](https://kubernetes.io/docs/setup/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Terraform](https://www.terraform.io/downloads.html) (if using for infrastructure setup)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/cloudwithtanvir/3-tier-microservices-k8s-terraform.git
   cd 3-tier-microservices-k8s-terraform
   ```

2. **Build and deploy Docker images** for each service:

   ```bash
   cd user-service
   docker build -t gcr.io/YOUR_PROJECT_ID/user-service:latest .
   docker push gcr.io/YOUR_PROJECT_ID/user-service:latest

   cd ../transaction-service
   docker build -t gcr.io/YOUR_PROJECT_ID/transaction-service:latest .
   docker push gcr.io/YOUR_PROJECT_ID/transaction-service:latest

   cd ../notification-service
   docker build -t gcr.io/YOUR_PROJECT_ID/notification-service:latest .
   docker push gcr.io/YOUR_PROJECT_ID/notification-service:latest

   cd ../frontend
   docker build -t gcr.io/YOUR_PROJECT_ID/frontend:latest .
   docker push gcr.io/YOUR_PROJECT_ID/frontend:latest
   ```

3. **Deploy the application on Kubernetes**:

   ```bash
   kubectl apply -f k8s_manifests/
   ```

### Running Locally with Docker Compose

To run the application locally using Docker Compose, follow these steps:

1. **Create a `docker-compose.yml` file** in the root of your project with the following content:

   ```yaml
   version: '3.8'

   services:
     frontend:
       image: gcr.io/YOUR_PROJECT_ID/frontend:latest
       ports:
         - "3000:3000"
       depends_on:
         - user-service
         - transaction-service
         - notification-service

     user-service:
       image: gcr.io/YOUR_PROJECT_ID/user-service:latest
       ports:
         - "8001:80"
       environment:
         - ALLOWED_ORIGINS=http://localhost:3000

     transaction-service:
       image: gcr.io/YOUR_PROJECT_ID/transaction-service:latest
       ports:
         - "8002:80"

     notification-service:
       image: gcr.io/YOUR_PROJECT_ID/notification-service:latest
       ports:
         - "8003:80"
       environment:
         - ALLOWED_ORIGINS=http://localhost:3000

   ```

2. **Run the application** using Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. **Access the application** by navigating to `http://localhost:3000` in your web browser.

### Accessing the Services

Each service can be accessed via the following endpoints:

- User Service: `http://localhost:8001/api/user/health`
- Transaction Service: `http://localhost:8002/api/transaction/health`
- Notification Service: `http://localhost:8003/api/notification/health`




### Configuration

Update the environment variables in your deployment YAML files as necessary, particularly for allowed origins and any sensitive data like API keys.

### Accessing the Application

Once deployed, you can access the frontend via the LoadBalancer IP obtained from:

```bash
kubectl get services
```

Open your browser and navigate to `http://<EXTERNAL_IP>`.

### Service Status

You can check the health status of each service via the following endpoints:

- User Service: `http://<EXTERNAL_IP>/api/user/health`
- Transaction Service: `http://<EXTERNAL_IP>/api/transaction/health`
- Notification Service: `http://<EXTERNAL_IP>/api/notification/health`

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.



## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework.
- [React](https://reactjs.org/) for the frontend framework.
- [Kubernetes](https://kubernetes.io/) for orchestration.
- [Docker](https://www.docker.com/) for containerization.
```