<div align="center" style="position: relative;">
  <img style="background-color: transparent; filter: brightness(0) contrast(100);" src="assets\GNOMENepal.png" />
  <h4 style="margin-top: 10px;">An open-source initiative of Nepal</h2>
</div>

<p align="center">
  <strong>
  Empowering community collaboration and innovation through <a href="https://nepal.gnome.org/">GNOME Nepal</a>.
  </strong>
</p>

<p align="center">
  <a href="https://github.com/GNOME-Nepal/site-server/actions"><img
    src="https://github.com/GNOME-Nepal/site-server/workflows/GNOME%20server%20CI%20workflow/badge.svg?branch=main"
    alt="Build"
  /></a>


#




# GNOME Nepal Backend Server

The **GNOME Nepal backend server** is an ongoing project aimed at building a robust and scalable platform for the GNOME Nepal community. This project focuses on simplifying app deployment and development through the use of [Docker](https://docs.docker.com/?_gl=1*1yac3bs*_gcl_au*NzU3MzU0MDMwLjE3Mjk0ODUyMTU.*_ga*NDEwNzYxNDg0LjE3MjI3NjE3NTA.*_ga_XJWPQMJYHQ*MTcyOTQ4NTIxNS40LjEuMTcyOTQ4NTIxNy41OC4wLjA.) while ensuring ease of configuration and setup, with long-term goals of production readiness.

We are working to streamline the architecture to efficiently handle [APIs](https://swagger.io/docs/), background task processing, and database management, leveraging modern technologies such as [Django](https://docs.djangoproject.com/en/5.1/), [Celery](https://docs.celeryq.dev/en/stable/index.html), and [Redis](https://docs.djangoproject.com/en/5.1/topics/cache/).

## Purpose
The purpose of this template is to simplify testing in Django, making it quick and easy without the hassle of manual setup. Instead of manually installing packages like `django-rest-framework`, `celery`, `celery-backend`, and `flower`, you can get everything up and running with just one click and a single command.

## Physical Architecture
When you run the following command, the setup will be created using `docker-compose`.

![Physical architecture of Djate](/assets/physical_architecture.jpg)

### Webserver

The webserver runs on Django and comes pre-packaged with Django REST Framework (DRF), `drf_yasg` for API documentation, and other essential tools. All dependencies are specified in the [requirements.txt](https://github.com/GNOME-Nepal/site-server/blob/main/requirements.txt).

### Database

Djate default database is SQLite as its lightweight nature, which makes it ideal for quick testing. However, we currently uses PostgreSQL as the default database for more flexibility in data types, scalability, concurrency, and data integrity.

### Message Queue

Redis is used as the message queue for Celery, managing background tasks efficiently.

### Flower

Flower is included for monitoring Celery tasks, accessible at `http://localhost:7777` using:

**Username:** admin  
**Password:** pswd

> _Flower runs on port 7777. Suiiiii!_

## Features

Djate simplifies Django app setup by integrating:

- **Django**: A high-level Python web framework.
- **Django REST Framework (DRF)**: For building Web APIs.
- **Celery**: For asynchronous background tasks.
- **Redis**: As a message broker for Celery.
- **Flower**: A web-based tool for monitoring Celery tasks.
- **Docker**: Djate is containerized using Docker for easier deployment and testing.

## Code Architecture:
Djate follows the standard Django project structure with `apps` and `manage.py` in the root directory. Each app has components such as `views.py`, `models.py`, `urls.py`, etc. Celery tasks are defined in `tasks.py` for each application.

The code architecture also leverages Django REST Framework (DRF) generics and viewsets for building APIs efficiently.

## Getting Started

To get started with Djate:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GNOME-Nepal/site-server.git
   cd site-server
   ```

2. **Build and run using Docker Compose:**

   ```bash
   docker-compose up --build
   ```

3. **Open your browser at** `http://localhost:8000` **to view the web app.**

4. Access Flower for task monitoring:

   Flower is available at `http://localhost:7777` with the default credentials:
   - **Username**: `admin`
   - **Password**: `pswd`

## Integration
- [Sentry](/documents/sentry.md)

## Contributing:
If you want to contribute to Djate, here are some suggestions for improvements. Please check off your contribution when you submit your PR:

- [ ] Vote for PostgreSQL vs SQLite as the default database. [Use this issue](https://github.com/n1rjal/djate/issues/1)
- [ ] Add Nginx as a reverse proxy for the Django app.
- [ ] Add configuration for process management with Systemd.
- [ ] Implement advanced logging features.
- [ ] Apply security fixes.
- [ ] Improve the Django admin panel.
- [x] Implement a To-do app as an example project.
- [x] Remove sqlite from repo
