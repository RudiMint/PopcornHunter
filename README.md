# Popcorn Hunter

Popcorn Hunter is a terminal-based movie search application that allows users to query a movie 
database using flexible filters such as genres, keywords, and release years. 
It includes a rich CLI interface, pagination for results, 
and search history analytics stored in MongoDB.

---

## Features

- Search movies by:
  - Genre(s)
  - Keywords (title or description)
  - Year or year range
- View search analytics:
  - Most frequently used search types
  - Last unique search queries
- Display available dataset metadata:
  - Genre list
  - Release year range
- Interactive pagination for search results
- Rich terminal UI with formatted tables and panels
- MongoDB-based search logging
- MySQL-backed movie database queries

---

## Project Structure

main.py
requirements.txt

db_queries/
history_query.py
movie_service.py

services/
mongo_history_logs.py

ui/
cli.py
rich_views.py

utils/
arguments.py
command_splitter.py
mongo_connection.py
mysql_connection.py
paginator.py



---

## Installation 

### Clone the repository

```bash
git clone https://github.com/RudiMint/PopcornHunter.git
cd PopcornHunter

Install dependencies

pip install -r requirements.txt


## Database Setup
MySQL

MySQL is used for storing and querying movie data.

Tables used:

film
category
film_category

Configure database credentials in utils/configuration.py.

## MongoDB

MongoDB is used for logging search history.

Collection:

user_stats

Each log entry contains:

timestamp
search_type
params
results_count

## Usage

Run the application:

python -m main.py

CLI Commands
Movie Search

Search by genre:

--genre Action Comedy

Search by keyword:

--tag space future

Search by year or range:

--year_range 2000 2010

Combine filters:

--genre Action --tag space --year_range 2000 2010
History Commands

Show most frequent search types:

--top_queries

Show last unique search types:

--unique
Utility Commands

Show available filters:

--filters

Display help:

--help

Exit application:

--quit

## Architecture Overview
    Search Flow
    1. User inputs command in CLI
    2. Arguments are parsed in arguments.py
    3. Query is built in movie_service.py
    4. MySQL executes the query
    5. Results are displayed using Rich UI components
    6. Search is logged into MongoDB

## Analytics Flow

  MongoDB aggregation pipelines are used to compute:

    Top search types (get_top_queries)
    Latest unique searches (get_last_unique_queries)

## UI Components
  Rich formatted tables for results and history
  Loading spinner during query execution
  Pagination system for large result sets
  Styled CLI error messages

## Dependencies
  rich
  pymysql
  pymongo
  prompt_toolkit
  argparse
