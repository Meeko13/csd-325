#CIndy Hernandez
# mod 4.2
#revision of code that needed to be downloaded

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

# Function to read the weather data from the CSV file
def read_weather_data():
    # Open the CSV file
    with open('sitka_weather_2018_simple.csv') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header

        # Lists to store dates, highs, and lows
        dates, highs, lows = [], [], []
        
        for row in reader:
            # Get the date and convert it to a datetime object
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            
            # Get high and low temperatures
            highs.append(int(row[5]))
            lows.append(int(row[6]))  # Assuming the lows are in the 7th column

    return dates, highs, lows

# Function to plot the temperatures
def plot_temperatures(dates, temperatures, color, title, ylabel):
    plt.plot(dates, temperatures, color=color)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)  # Rotate the date labels to avoid overlap
    plt.show()

# Main part of the program
def main():
    # Read the data from the CSV file
    dates, highs, lows = read_weather_data()

    while True:
        # Ask the user to select an option
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            # Plot high temperatures
            plot_temperatures(dates, highs, 'red', 'Daily High Temperatures - 2018', 'Temperature (F)')
        elif choice == '2':
            # Plot low temperatures
            plot_temperatures(dates, lows, 'blue', 'Daily Low Temperatures - 2018', 'Temperature (F)')
        elif choice == '3':
            # Exit the program
            print("Goodbye!")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

