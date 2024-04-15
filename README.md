# Subway Turnstile Data Analysis Project

This repository contains Python scripts designed to process and analyze data from subway turnstiles in Buenos Aires, along with weather and holiday data for 2017 and 2018.

## Script Descriptions

### 1. Data Preprocessing
The scripts perform the opening, reading, and accumulation of turnstile usage data and weather conditions. Totals are calculated and relevant data such as the day of the week and precipitation for each data entry are added.

**Involved files:**
- `molinetes_2017.csv`
- `molinetes_2018_full.csv`
- `clima_con_fechas_ok.csv`

### 2. Data Conversion and Manipulation
Functions are included to convert strings to integers and to handle unavailable or erroneous values. Additionally, each row of data is processed to add new information and calculate accumulated values.

### 3. Dictionary Generation
Dictionaries are used to map precipitation and holiday data to corresponding dates, facilitating the aggregation of this information to the turnstile data.

### 4. Writing Results
The processed data are written to new CSV files, ready for further analysis or visualization.

**Generated files:**
- `molinetes_2017_full.csv`
- `molinetes_2018_con_feriados.csv`

## Usage

To run the scripts, ensure you have Python installed along with the `csv` and `datetime` libraries. Then, execute the scripts in the order mentioned in the descriptions. Ensure that the necessary CSV files are in the same directory as the scripts.

## Contributions

This project is open to contributions. If you would like to improve the scripts or extend the functionalities, feel free to fork the repository and send your pull requests.

## License

This project is released under the MIT License. For more details, see the `LICENSE` file in this repository.
