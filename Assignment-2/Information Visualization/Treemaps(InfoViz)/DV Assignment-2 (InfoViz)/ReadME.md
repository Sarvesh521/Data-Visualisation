# Crime Data Visualization using Treemaps

This project involves analyzing and visualizing crime data from Los Angeles using treemaps. The goal is to provide insights into crime patterns based on various factors such as time of occurrence, victim gender, premises type, crime description, and victim descent.

## Table of Contents
1. [Dataset](#dataset)  
2. [Project Structure](#project-structure)  
3. [Dependencies](#dependencies)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Functions Overview](#functions-overview)  
7. [Visualization Outputs](#visualization-outputs)  

## Dataset

The analysis is based on the `Cleaned_LA_Dataset.csv` file, which contains cleaned crime data from Los Angeles. The dataset includes fields like:

- **TIME OCC**: Time of occurrence  
- **Vict Sex**: Victim's gender  
- **Part 1-2**: Crime seriousness (1 for serious crimes, 2 for non-serious crimes)  
- **Premis Desc**: Description of the premises where the crime occurred  
- **Crm Cd**: Crime code  
- **Crm Cd Desc**: Crime description  
- **Vict Descent**: Victim's descent  
- **Weapon Desc**: Description of the weapon used  

## Project Structure

- `treemaps.py`: Main script containing all functions for data processing and visualization.
- `requirements.txt`: List of Python dependencies required to run the project.
- `*.html`: Generated treemap visualizations in HTML format.
- `*.json`: Treemap data in JSON format for use with Plotly.js.

## Dependencies

The project requires the following Python libraries:

- **pandas**
- **plotly**

Refer to the `requirements.txt` file for exact versions.

## Installation

1. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Place the Dataset**

   Ensure that the `Cleaned_LA_Dataset.csv` file is in the project directory.

## Usage

Run the `treemaps.py` script to generate the treemap visualizations:

```bash
python treemaps.py
```

This will process the data and create HTML and JSON files for each treemap visualization.

## Functions Overview

### `calculate_cat_time_occ(time_occ)`

Categorizes the time of occurrence into time slots.

### `load_data()`

Loads the dataset and applies initial transformations.

### `create_treemap(df, path, title, labels, branchvalues, color=None, color_discrete_map=None)`

Creates a treemap figure using Plotly based on the given parameters.

### `save_figure(fig, filename_prefix)`

Saves the treemap figure as both JSON and HTML files.

### `process_gender_time_crime(df)`

Processes data and creates treemaps showing the distribution of crimes by victim gender, time of day, and crime seriousness.

### `process_gender_premises_crime(df)`

Generates treemaps based on victim gender, premises type, and crime seriousness.

### `process_crime_description(df)`

Creates treemaps depicting the distribution of crimes by description, victim gender, and crime seriousness.

### `process_victim_descent(df)`

Analyzes and visualizes crime data based on victim descent, premises, weapon description, and crime seriousness.

### `main()`

Main function that orchestrates data loading and visualization processing.

## Visualization Outputs

The following treemaps are generated:

### Gender-wise Distribution of Crimes by Time of Day and Crime Seriousness

- `crime_victsex_hr_total.html`
- `crime_victsex_hr_remainder.html`

### Gender-wise Distribution of Crimes by Premises Type and Crime Seriousness

- `crime_victsex_premis_type_total.html`
- `crime_victsex_premis_type_remainder.html`

### Distribution of Crimes by Description, Gender, and Crime Seriousness

- `crime_crimedesc_victsex_crimetype_total.html`
- `crime_crimedesc_victsex_crimetype_remainder.html`

### Distribution of Crimes by Victim Descent, Premises, Weapon Description, and Crime Seriousness

- `crime_victdesc_crimedesc_weapondesc_crimetype_total.html`
- `crime_victdesc_crimedesc_weapondesc_crimetype_remainder.html`

Each visualization is saved in both HTML and JSON formats for easy sharing and embedding.
