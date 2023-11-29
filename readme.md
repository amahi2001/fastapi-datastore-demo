# README for FastAPI with GCP Datastore Project

## Project Overview
This GitHub project demonstrates the integration of FastAPI with Google Cloud Platform's (GCP) Datastore. It provides a simple backend application for task management, allowing operations such as adding, retrieving, and deleting tasks.

## Features
- **FastAPI Backend**: Leverages FastAPI for building efficient and scalable APIs.
- **GCP Datastore Integration**: Utilizes GCP Datastore for data storage and retrieval.
- **Task Management**: Supports operations like listing, adding, and deleting tasks.
- **CORS Middleware**: Ensures compatibility with front-end running on different domains or ports.

## Getting Started

### Prerequisites
- Python 3.11
- Pyenv and Virtualenv
- GCP account and project setup
- Gmake (optional)

### Installation

1. **Clone the Repository**
   ```bash
   git clone [repository-link]
   cd [repository-name]
2. **Run Locally**
    ```bash
    make run
    ```
    or
    ```bash
    uvicorn main:app --reload
    ```
3. **Deploy to GCP**
    ```bash
    make deploy
    ```
    or
    ```bash
    gcloud app deploy
    ```