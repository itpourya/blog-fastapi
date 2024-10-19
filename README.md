
# FastAPI Blog Project

This is a **blog** application built using **FastAPI**, which includes features such as **post creation**, **JWT-based authentication**, **deleting posts**, **liking posts**, **commenting on posts**, as well as **user login** and **signup**.

## Features

- **User Authentication**: Signup and login functionality with JWT (JSON Web Token) for secure authentication.
- **Post Management**: Users can create, edit, and delete their own blog posts.
- **Like Posts**: Users can like or unlike blog posts.
- **Comment on Posts**: Users can add comments to blog posts.
- **JWT Authentication**: Secure routes for authorized users only.
- **Delete Posts**: Authenticated users can delete their own posts.
- **Update Posts**: Authenticated users can update their own posts.

## Prerequisites

To run this project, you'll need:

- [Python 3.8+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/itpourya/blog-fastapi.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blog-fastapi
   ```

3. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

This will start the development server at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication

- **POST** `/auth/signup/`: Register a new user.
- **POST** `/auth/signin/`: Login and receive a JWT.

### Blog Post Management

- **GET** `/posts/`: Get a list of all posts.
- **POST** `/create_posts/`: Create a new post (authenticated).
- **DELETE** `/delete_posts/`: Delete a post (authenticated, post owner only).

### Post Interactions

- **POST** `/posts/{post_id}/like/`: Like or unlike a post (authenticated).
- **POST** `/posts/{post_id}/comment/`: Comment on a post (authenticated).

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **JWT**: Used for user authentication.
- **SQLAlchemy**: ORM for database interactions.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
