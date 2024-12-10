import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the dataset from CSV file
df = pd.read_csv('movies.csv')

# Clean column names by stripping any leading/trailing whitespace
df.columns = df.columns.str.strip()

# Clean any leading/trailing whitespace from data in each column
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Check for missing values and remove rows with missing essential data
df = df.dropna(subset=['Year', 'Genre', 'Country', 'Main Actors', 'Synopsis'])

# Print the first few rows of the cleaned data for debugging
print(df.head())

# Get unique values for Year, Genre, and Country
unique_years = sorted(df['Year'].unique())
unique_genres = sorted(df['Genre'].unique())
unique_countries = sorted(df['Country'].unique())

# Function to display movies based on filters
def display_movies():
    # Get the selected filter values
    year_value = year_var.get()
    genre_value = genre_var.get()
    country_value = country_var.get()
    actor_value = actor_var.get()

    # Filter the dataframe based on the selected values
    filtered_df = df

    # Apply filters based on user selection
    if year_value != "Select Year" and year_value != "":  # Ignore if blank or "Select Year"
        filtered_df = filtered_df[filtered_df['Year'] == int(year_value)]
    if genre_value != "Select Genre" and genre_value != "":  # Ignore if blank or "Select Genre"
        filtered_df = filtered_df[filtered_df['Genre'] == genre_value]
    if country_value != "Select Country" and country_value != "":  # Ignore if blank or "Select Country"
        filtered_df = filtered_df[filtered_df['Country'] == country_value]
    if actor_value:  # Only filter by actor if provided
        filtered_df = filtered_df[filtered_df['Main Actors'].str.contains(actor_value, case=False, na=False)]

    # Check if the filtered dataframe is empty
    if filtered_df.empty:
        result_text = "No movies found matching the criteria."
    else:
        result_text = "Movies matching the criteria:\n\n"
        for index, row in filtered_df.iterrows():
            result_text += f"Movie: {row['Movie']}\n"
            result_text += f"Year: {row['Year']}\n"
            result_text += f"Genre: {row['Genre']}\n"
            result_text += f"Country: {row['Country']}\n"
            result_text += f"Main Actors: {row['Main Actors']}\n"
            result_text += f"Synopsis: {row['Synopsis']}\n"
            result_text += "-" * 50 + "\n"  # Separator line between movies

    # Update the result label with the filtered data
    result_label.config(state=tk.NORMAL)  # Enable editing
    result_label.delete(1.0, tk.END)  # Clear existing content
    result_label.insert(tk.END, result_text)  # Insert the new results
    result_label.config(state=tk.DISABLED)  # Disable editing

# Initialize the main window
root = tk.Tk()
root.title("Movie Recommendation System")

# Set background color for the main window
root.configure(bg='#1bef45')

# Add a label for the title
title_label = tk.Label(root, text="Welcome to the Movie Recommendation System!", font=("Arial", 16), bg='#4c5fff')
title_label.pack(pady=10)

# Set the window size
root.geometry("750x550")

# Add dropdown menu for Year selection
year_var = tk.StringVar(value="Select Year")
year_dropdown = tk.OptionMenu(root, year_var, "Select Year", *unique_years)
year_dropdown.config(font=("Arial", 14), bg='#4c5fff')
year_dropdown.pack(pady=5)

# Add dropdown menu for Genre selection
genre_var = tk.StringVar(value="Select Genre")
genre_dropdown = tk.OptionMenu(root, genre_var, "Select Genre", *unique_genres)
genre_dropdown.config(font=("Arial", 14), bg='#4c5fff')
genre_dropdown.pack(pady=5)

# Add dropdown menu for Country selection
country_var = tk.StringVar(value="Select Country")
country_dropdown = tk.OptionMenu(root, country_var, "Select Country", *unique_countries)
country_dropdown.config(font=("Arial", 14), bg='#4c5fff')
country_dropdown.pack(pady=5)

# Add an entry field for actor input
actor_label = tk.Label(root, text="Enter Actor's Name (e.g., Leonardo DiCaprio):", font=("Arial", 12), bg='#4c5fff')
actor_label.pack(pady=10)

actor_var = tk.StringVar()
actor_entry = tk.Entry(root, textvariable=actor_var, font=("Arial", 12), bg='#ffffff')
actor_entry.pack(pady=5)

# Create a button to trigger the search
search_button = tk.Button(root, text="Search Movies", command=display_movies, font=("Arial", 12), bg='#4c5fff', fg='black')
search_button.pack(pady=10)

# Create a canvas and a scrollbar for scrolling results
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame within the canvas to hold the results
result_frame = tk.Frame(canvas)

# Create a text widget to display the results
result_label = tk.Text(result_frame, wrap=tk.WORD, width=85, height=20, font=("Arial", 10), bg='#f1f1f1', bd=0, padx=5, pady=5)
result_label.pack()

# Attach the frame to the canvas
canvas.create_window((0, 0), window=result_frame, anchor="nw")

# Attach the scrollbar to the canvas
scrollbar.pack(side="right", fill="y")
canvas.pack(pady=10, expand=True, fill="both")

# Run the GUI
root.mainloop()
