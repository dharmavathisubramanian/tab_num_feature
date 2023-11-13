# Collaborative Development of CSV Explorer Web App

## Authors
Group <group number> : 
- Dikshya Tamling Limbu (2462177)
- Dharmavathi Subramanian (25040155)
- <first and last name> (<UTS student id>)

## Description
The CSV Explorer Web App is a Python-based project that allows users to analyse CSV files using features such as DataFrame Exploration, Numeric Series Analysis, Text Series Exploration, and Datetime Series Analysis.

The team faced challenges with Github due to member skill differences. Zoom meetings were used to establish a suitable coding environment and handle merge conflicts. Due to free accounts and private repository, strict Code Reviews were implemented for smooth collaboration.Handling various data kinds such as numeric, text, and datetime is a complex operation that necessitates specific processing and visualisation approaches. Balancing simplicity with functionality and providing clear instructions is an ongoing problem in web application development. Creating an intuitive interface is critical for online apps, as is optimising speed for larger information. Techniques such as lazy loading and efficient data processing algorithms are critical for a positive user experience. These issues necessitate a combination of technical skills, user experience considerations, and optimisation strategies.

Features such as greater data visualisation, interactive filtering, customised dashboards, and connectivity with external data sources could be added to the CSV Explorer Web App. These features would enhance the user experience, enable greater data discovery, and allow for real-time collaboration. The software should also be adaptable to various screen sizes and devices.


## How to Setup
1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd <project_directory>`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install required packages: `pip install -r requirements.txt`

Version Python 3.9 


## How to Run the Program

1. Verify that Python is installed on computer.
2. Install required packages by running: `pip install streamlit requests`.
3. Utilise the terminal to go to the project directory.
4. Run the Streamlit app: `streamlit run app/streamlit_app.py`
5. Open the provided URL in your web browser.


## Project Structure
- **app/**
  - `streamlit_app.py`: Main Streamlit application script.
- **tab_df/**
  - `display_tab_df_content.py`: Module for displaying DataFrame tab content.
- **tab_num/**
  - `display_tab_num_content.py`: Module for displaying Numeric Series tab content.
- **tab_text/**
  - `display_tab_text_content.py`: Module for displaying Text Series tab content.
- **tab_date/**
  - `display_tab_date_content.py`: Module for displaying Datetime Series tab content


## Citations
- [Streamlit documentation](https://docs.streamlit.io/)
- [Pandas documentation](https://pandas.pydata.org/docs/)

