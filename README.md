# A Simple News Website Backend

This project is a backend service designed to automate the process of scraping news articles from **Zoomit** and providing them via a RESTful API. The project is structured using Django for web development, Celery for task automation, and Selenium alongside with Beautiful Soap for web scraping.

## Features

- **Django REST API**:
  - Provides endpoints to access news articles stored in the database.
  - Supports filtering news based on tags for easy categorization and retrieval.

- **Automated Web Scraping**:
  - Utilizes Selenium to extract news article links from Zoomit website.
  - Using the links obtained by Selenium, Beautiful Soap extract the content of a news article like article id, title, tags, and description.
  - The scraping process is automatically triggered using Celery, scheduled to run at regular intervals.

- **Task Automation with Celery**:
  - Automates the scraping and database update process.
  - Celery Beat schedules scraping tasks to keep the news database up-to-date without manual intervention.

- **Dockerized Deployment**:
  - The entire project is containerized using Docker, ensuring easy deployment and environment consistency.
  - Docker Compose manages the Django application, Celery worker, Celery Beat scheduler, and Redis as a message broker.

## Technologies Used

- **Django & Django REST Framework**: Backend and API development.
- **Celery & Celery Beat**: Task scheduling and automation.
- **Selenium**: Web scraping.
- **Redis**: Message broker for Celery.
- **Docker & Docker Compose**: Containerization and deployment.

## Prerequisites

1. Find and download the lastest verison of ChromeDriver and replace it with the one available in the project root.
2. Make sure you've installed docker on your operating system.

## Installation & Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Hamedtbf/news-website.git
    cd news-website
    ```

2. **Build and Run the Docker Containers**:
    ```bash
    docker-compose up --build
    ```

3. **Access the API**:
   - The Django server will be available at `http://localhost:8000`.
   - Celery tasks are scheduled automatically based on the configuration.

4. **How to use the API**:
   - `http://localhost:8000/post/list/` will return you a list of all posts available on the website.
   - `http://localhost:8000/post/list/<post id>` will return you the specified news article you entered its post_id value.
   - `http://localhost:8000/post/tags/` will return you a list of all tags available on the website.
   - `http://localhost:8000/post/tags/<some tag>` will return you a list of all posts that contain the tag you entered. 

## Future Improvements

- Implement more sophisticated scraping strategies to handle various website structures.
- Enhance the API with additional filtering and sorting capabilities.
- Add comprehensive testing and logging for better monitoring and maintenance.
