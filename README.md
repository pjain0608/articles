## Articles
A simple and dynamic web application to manage and display articles. The project provides a clean interface to browse through articles and read their full descriptions.

## Features
-  Main Page: Displays a list of articles with their headings and a short snippet (4-5 words) from their descriptions.
-  Detailed View: Clicking on an article redirects to a page with the full headline and complete description.
-  Database Integration: Articles are fetched dynamically from the database for easy management and updates.

## Tech Stack
-  Backend: Django
-  Frontend: HTML, CSS
-  Database: MySQL

## How It Works
Main Page: The application queries the database to fetch all articles and displays their titles with a brief preview of their descriptions.
Article Detail: Each article has a clickable link that takes the user to a dedicated page where the full description is displayed.
