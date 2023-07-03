# Travel Bucket RESTful API

This project is a RESTful API for managing a travel bucket list. It allows users to create, view, update, and delete travel destinations in their bucket list.

## Installation

To run the Travel Bucket RESTful API, make sure you have Docker installed on your system. Then, follow these steps:

1. Clone the repository:

2. Navigate to the project directory:

   ```bash
   cd travel-bucket-rest-api
   ```

3. Build the Docker image:

   ```bash
   docker build -t travel-bucket-api .
   ```

4. Run the Docker container:

   ```bash
   docker run -p 8000:8000 travel-bucket-api
   ```

5. The API will be accessible at `http://localhost:8000/`.

## API Documentation

1- create element and view the lsit:
    `http://localhost:8000/api/v1/bbucket`

2- Update or delete or show details for specific Item:
    `http://localhost:8000/api/v1/bbucket/<id>`

## Author

Abdulkareem Abunabhan

If you have any questions or feedback regarding the project, you can contact me at zman17881@gmail.com