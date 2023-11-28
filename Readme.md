# NSFW Classifier Demo

Welcome to the NSFW (Not Safe For Work) Classifier Demo! This project is a result of collaborative efforts by Danwnad, Sivadas, and Mamtha for the Miniproject at CUSAT.

## Overview

This NSFW classifier analyzes the content of a given website to determine if it contains offensive material. The results will indicate whether the website is safe or potentially NSFW.

## Getting Started

Follow these steps to set up and run the NSFW Classifier Demo on your local machine using Streamlit and Docker Compose.

### Prerequisites

- Docker: Make sure you have Docker installed on your system. If not, you can download and install it from [Docker's official website](https://www.docker.com/get-started).


### Running Support Classifier with Docker Compose

1. Use Docker Compose to start containers for PostgreSQL and RabbitMQ:

    ```bash
    docker-compose up -d
    ```

### Running NSFW Classifier

1. Run Streamlit in the command line:

    ```bash
    streamlit run app.py
    ```

2. Access the Streamlit app:

    Open your web browser and go to [http://localhost:8501](http://localhost:8501) to interact with the NSFW Classifier Demo.


### Note

This demo is designed for educational purposes and may not be perfect. Use it responsibly.

## See more projects

Discover other interesting projects by visiting [Danwnad's GitHub](https://github.com/danwnad).

---

**Enjoy exploring the NSFW Classifier Demo!**
