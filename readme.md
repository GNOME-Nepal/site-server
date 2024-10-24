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
</p>

#

# GNOME Nepal Backend Server

The **GNOME Nepal backend server** is an ongoing project aimed at building a robust and scalable platform for the GNOME Nepal community. This project focuses on simplifying app deployment and development through the use of [Docker](https://docs.docker.com/?_gl=1*1yac3bs*_gcl_au*NzU3MzU0MDMwLjE3Mjk0ODUyMTU.*_ga*NDEwNzYxNDg0LjE3MjI3NjE3NTA.*_ga_XJWPQMJYHQ*MTcyOTQ4NTIxNS40LjEuMTcyOTQ4NTIxNy41OC4wLjA.) while ensuring ease of configuration and setup, with long-term goals of production readiness.

We are working to streamline the architecture to efficiently handle [APIs](https://swagger.io/docs/), background task processing, and database management, leveraging modern technologies such as [Django](https://docs.djangoproject.com/en/5.1/), [Celery](https://docs.celeryq.dev/en/stable/index.html), and [Redis](https://docs.djangoproject.com/en/5.1/topics/cache/).

## Purpose

The GNOME Nepal backend server project is intended to make Django app setup and configuration quick and beginner-friendly. By using Docker and other modern technologies, developers can get the server running with minimal manual intervention. The platform serves as a great starting point for learning about the internals of Django and will be expanded to production-grade architecture in the future.

---

## Djate: Django Awesome Template

Djate is an integral part of the GNOME Nepal backend server. It serves as a simple and efficient Django template to assist in creating backend services. Djate focuses on eliminating the complexity of setting up essential components such as `Django REST Framework`, `Celery`, `celery-backend`, `flower` and `Redis` by automating these tasks through a single command.

### Code Architecture

Djate follows a standard Django project structure with `apps` and `manage.py` in the root directory. Each app contains components such as `views.py`, `models.py`, and `urls.py`, while Celery tasks are defined in `tasks.py` for each application.

The code architecture leverages Django REST Framework (DRF) generics and viewsets for building APIs efficiently, ensuring modularity and efficiency in development.


### Physical Architecture

The physical architecture of Djate is designed to handle task management and background processes efficiently using Redis and Celery. Below is the architecture diagram for how tasks are processed within the Djate setup:

![Physical architecture of Djate](https://github.com/Sailesh-Singh/site-server/raw/main/assets/physical_architecture.jpg)
*Fig: The architecture includes Django for the web layer, Redis for the message queue, Celery for task processing, and Flower for task monitoring.*

### Webserver

The webserver runs on Django and comes pre-packaged with Django REST Framework (DRF), `drf_yasg` for API documentation, and other essential tools. All dependencies are specified in the [requirements.txt](https://github.com/GNOME-Nepal/site-server/blob/main/requirements.txt).

### Database

Djate default database is SQLite as its lightweight nature, which makes it ideal for quick testing. However, we currently uses PostgreSQL as the default database for more flexibility in data types, scalability, concurrency, and data integrity.

### Message Queue

Redis is used as the message queue for Celery, managing background tasks efficiently.

### Flower

Flower is included for monitoring Celery tasks, accessible at `http://localhost:7777` using:

- **Username:** admin
- **Password:** pswd

## Features

Djate simplifies Django app setup by integrating:

- **Django**: A high-level Python web framework.
- **Django REST Framework (DRF)**: For building Web APIs.
- **Celery**: For asynchronous background tasks.
- **Redis**: As a message broker for Celery.
- **Flower**: A web-based tool for monitoring Celery tasks.
- **Docker**: Used to containerize the application for easy deployment and testing.


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

4. **Access Flower for task monitoring at** `http://localhost:7777` **using the default credentials:[Only when you run via docker compose]**
   - **Username**: `admin`
   - **Password**: `pswd`


## Features in Development

As part of the GNOME Nepal backend server, we are planning to incorporate the following features for community engagement and operational needs:

- [x] **Newsletter System**: For sending invites and announcements.
- [x] **Admin Panel**: Managed through Django's built-in capabilities.
- [ ] **Event Management Backend**: Schedule and manage community events.
- [ ] **Blogs**: Community members can document events or share thoughts.
- [ ] **RBAC System**: Implementing Role-Based Access Control with Django.
- [ ] **Member Lookup**: Ability for staff contributors to look up members.
- [ ] **Blog Submission**: Contributors can submit blogs, with super admins verifying content.

### How to Contribute
We welcome contributions to enhance this project. Whether you're fixing bugs, adding new features, or improving documentation, your help is appreciated.
To contribute to this project, follow these steps:

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and commit them with descriptive messages.
4. **Push your branch** to your forked repository.
5. **Submit a pull request** detailing your changes.

*(Note: Before contributing read the detailed [guidelines](CONTRIBUTING.md) for contributions)*


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/GNOME-Nepal/site-server/blob/main/LICENSE) file for details.

## Contact Information

For questions or assistance, please reach out to:

- **Support**: [GNOME](https://github.com/GNOME-Nepal/site-server/issues/new/choose)
- **GitHub**: [GNOME Nepal](https://github.com/GNOME-Nepal)

## Acknowledgments

We would like to thank all contributors and the GNOME community for their support and resources.
