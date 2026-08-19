**Book Library**

A simple Book Library application built using **FastAPI, MongoDB, and Streamlit**.

The project provides a REST API for managing books and a Streamlit frontend with an ecommerce-style layout for viewing, searching, adding, editing, and deleting books.

**Features**

- View all books
- Search books by title
- Add new books
- Edit book details
- Delete books
- Track book stock status
- View individual book details
- Store book data in MongoDB
- Store MongoDB connection details using environment variables
- Ecommerce-style book display using Streamlit

**Technologies Used**

- Python - Program
- FastAPI - Backend
- MongoDB - Database
- PyMongo - MongoDB connection
- Pydantic - Data validation
- Streamlit- Frontend
- Requests- Communication between frontend and backend
- python-dotenv- Environment variable management

**API Endpoints**

| Method   | Endpoint            | Purpose               |
| -------- | ------------------- | --------------------- |
| `POST`   | `/`                 | Create/add a new book |
| `GET`    | `/`                 | Get all books         |
| `GET`    | `/search?title=...` | Search books by title |
| `PUT`    | `/{id}`             | Update a book         |
| `DELETE` | `/{id}`             | Delete a book         |
