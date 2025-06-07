# 🐦 Twitter Clone

[![Django](https://img.shields.io/badge/Django-3.2+-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0+-purple.svg)](https://getbootstrap.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Django-based web application that replicates core features of Twitter, including tweeting, following users, liking posts, and more.

![Twitter Clone Preview](https://res.cloudinary.com/blackcode/image/upload/v1749269322/tweet_photos/m3n9b3tzabtda9sayfft.jpg)

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Live Demo](#live-demo)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- 👤 User registration, login, and profile management
- 📝 Post tweets (text, images)
- ❤️ Like and comment on tweets
- 👥 Follow and unfollow users
- 🏠 Personalized timeline
- 📱 Responsive design

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS (Bootstrap, Tailwind CSS), JavaScript
- **Database:** SQLite (default), can be switched to PostgreSQL

## 🚀 Installation

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

## 📱 Usage

- Register a new account or log in.
- Post tweets, follow users, and interact with tweets.
- Access the admin panel at `/admin` for management.

## 🌐 Live Demo

Check out the live version of the app at [https://your-twitter-clone-url.com](https://your-twitter-clone-url.com)

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ by [Your Name]