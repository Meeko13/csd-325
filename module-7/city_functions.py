# Cindy Hernandez
# mod 7.2




# city_functions.py

def format_city_country(city, country, population=None, language=None):
    """Return a string in the format 'City, Country - population xxx - language xxx' or 
    'City, Country' if no population or language is provided."""
    
    # Initialize the string with city and country
    result = f"{city}, {country}"
    
    # Add population if provided
    if population:
        result += f" - population {population}"
    
    # Add language if provided
    if language:
        result += f" - language {language}"
    
    return result

# Call the function with different parameters
city1 = format_city_country('Santiago', 'Chile')  # City and Country
city2 = format_city_country('Paris', 'France', 2148000)  # City, Country, and Population
city3 = format_city_country('Tokyo', 'Japan', 13960000, 'Japanese')  # City, Country, Population, and Language

# Print the results
print(city1)
print(city2)
print(city3)

