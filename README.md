# Arssam Basha M
## NM ID: au110121104014

<br><br>


# Personal Blog on IBM Cloud Static Web Apps

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Cloning the Repository](#cloning-the-repository)
  - [Setting up IBM Cloud and Db2](#setting-up-ibm-cloud-and-db2)
  - [Running Locally](#running-locally)
- [Dockerization](#dockerization)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Updating Content](#updating-content)
- [Dependencies](#dependencies)
  
## Overview

This project is a web application hosted on IBM Cloud that utilizes Flask as the web framework, IBM Cloud Db2 as the database, Docker for containerization, and Kubernetes for orchestration. The web application provides to share travel adventures, tips, and captivating photos to inspire others to explore the world and create unforgettable memories.

## Prerequisites

Before you can run and work on this project, make sure you have the following prerequisites installed:

- [Python](https://www.python.org/)
- [Docker](https://docs.docker.com/install/)
- [Kubernetes](https://kubernetes.io/docs/setup/)
- [IBM Cloud Account](https://cloud.ibm.com/)
- [IBM Db2](https://cloud.ibm.com/catalog/services/db2)
- [Git](https://git-scm.com/)

## Getting Started

Follow these steps to get the project up and running:

### Cloning the Repository

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/basha577/Cloud_Web_Static.git
   cd project-code
   ```

### Setting up IBM Cloud and Db2

1. Create an IBM Cloud account if you don't have one already.

2. Provision an IBM Db2 service on IBM Cloud. You will need the connection details (e.g., hostname, username, password).

### Running Locally

1. Create a virtual environment and install project dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Set the environment variables for the IBM Db2 connection. You can use a `.env` file for this. Replace the placeholders with the Db2 details.

   ```dotenv
   DB2_HOST=db2-hostname
   DB2_PORT=db2-port
   DB2_DATABASE=db2-database
   DB2_USER=db2-username
   DB2_PASSWORD=db2-password
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Access the web application in your browser at `http://localhost:5000`.

## Dockerization

The application can be containerized using Docker for easy deployment. Follow these steps to build and run the Docker image:

1. Build the Docker image:

   ```bash
   docker build -t project-code .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8080:80 project-code
   ```

3. Access the web application in your browser at `http://localhost:8080`.


## Kubernetes Deployment

To deploy this application on Kubernetes, follow these steps:

### Prerequisites

1. Ensure you have the following prerequisites installed:

   - [Kubernetes](https://kubernetes.io/docs/setup/)
   - [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) (Kubernetes command-line tool)
   - A running Kubernetes cluster (you can use Minikube or a managed Kubernetes service like GKE, AKS, or EKS).

### Deployment Steps

1. **Kubernetes Manifests**: You should have Kubernetes manifest files for your application. These manifest files describe the desired state of your application. Typically, you would have a Deployment and a Service manifest.

   ```bash
   ├── k8s
   │   ├── deployment.yaml
   │   └── service.yaml
   ```

   You can create these manifest files and customize them to match your application's requirements.

2. **Apply Manifests**: Use `kubectl` to apply the Kubernetes manifest files:

   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

   This will create the necessary resources in your Kubernetes cluster.

3. **Accessing the Application**: Depending on the Service type you specified in your `service.yaml` (e.g., LoadBalancer, NodePort, ClusterIP), you can access your application using the appropriate method. For example, with LoadBalancer, you can typically access it via the external IP or domain provided by your cloud provider.


## Updating Content

To update the content of the website:

1. Navigate to the appropriate file in the project directory and make your changes.

2. Update the database if necessary.

3. If you are using version control, commit your changes and push to the repository.

4. Deploy the updated application as described in the [Getting Started](#getting-started) section.

## Dependencies

The project relies on the following key dependencies:

- [Flask](https://flask.palletsprojects.com/)
- [IBM Db2 Python Driver](https://www.ibm.com/docs/en/db2/10.5?topic=framework-setting-up-python-environment)
- [Docker](https://docs.docker.com/)
- [Kubernetes](https://kubernetes.io/)

For a complete list of dependencies, refer to the `requirements.txt` file.


---
