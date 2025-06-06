# Twitter Clone

A Django-based web application that replicates core features of Twitter, including tweeting, following users, liking posts, and more.

## Features

- User registration, login, and profile management
- Post tweets (text, images)
- Like and comment on tweets
- Follow and unfollow users
- Personalized timeline
- Responsive design

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Database:** SQLite (default), can be switched to PostgreSQL

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/twitter-clone.git
   cd twitter-clone
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register a new account or log in.
- Post tweets, follow users, and interact with tweets.
- Access the admin panel at `/admin` for management.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
