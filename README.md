# Movie Recommendation System

Welcome to the **Movie Recommendation System**, a Python application that helps users filter and search for movies based on multiple criteria such as Year, Genre, Country, and Main Actors. This application features an interactive GUI built with Tkinter and uses a CSV dataset of movies.

---

## Features

- **Interactive GUI**: User-friendly interface built with Tkinter.
- **Flexible Filtering**:
  - Filter by **Year**, **Genre**, **Country**, or **Main Actors**.
  - Dropdown menus with a "Select" option to leave filters blank if not needed.
  - Manually type actor names for more specific searches.
- **Scrollable Results**: View matching movies in a scrollable window.
- **Detailed Movie Information**: Display movie title, year, genre, country, main actors, and a synopsis.

---

## Installation

### Prerequisites
- Python 3.x
- Required libraries:
  - `pandas`
  - `tkinter`

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system

Install required libraries:
pip install pandas

Ensure you have a movies.csv file in the same directory as the script. The CSV file should have the following columns:

    Movie: The title of the movie.
    Year: The year the movie was released.
    Genre: The genre of the movie.
    Country: The country where the movie was produced.
    Main Actors: A list of main actors in the movie.
    Synopsis: A brief description of the movie.

How to Use

    Run the script:

python movie_recommendation_system.py

The main window will open with the following options:

    Year: Dropdown menu to select a release year.
    Genre: Dropdown menu to select a genre.
    Country: Dropdown menu to select a country.
    Main Actors: Input field to manually enter an actor's name.

Click the Search Movies button after selecting your filters to see the results.
The results are displayed in a scrollable section, showing:

    Movie Title
    Year
    Genre
    Country
    Main Actors
    Synopsis

Example

Imagine you want to find all action movies from the USA released in the year 2000, starring any specific actor. You can:

    Select Year = 2000.
    Select Genre = Action.
    Select Country = USA.
    Optionally, type an actor's name (or leave it blank).
    Click Search Movies to view the results.
