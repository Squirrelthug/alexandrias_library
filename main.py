import random
from metis import Metis
import json

# Configuration
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.;'!? "
page_length = 3200  # Number of characters on a page
progress_file = 'processed_pages.txt'
results_file = 'results.txt'

# Logical maximum values based on Borges' description
MAX_BAY = 1000000  # Large number for practical purposes
MAX_SHELF = 20  # Four walls with five shelves each
MAX_VOLUME = 32  # Thirty-two books per shelf
MAX_PAGE = 410  # Four hundred and ten pages per book

# Load progress
def load_progress(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'current_bay': 0, 'current_shelf': 0, 'current_volume': 0, 'current_page': 0}

# Save progress
def save_progress(file_path, progress):
    with open(file_path, 'w') as f:
        json.dump(progress, f)

# Get user input or random value
def get_value(prompt, max_value):
    user_input = input(prompt)
    if user_input.lower() == 'r':
        return random.randint(0, max_value)
    else:
        try:
            value = int(user_input)
            if 0 <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between 0 and {max_value}.")
                return get_value(prompt, max_value)
        except ValueError:
            print("Invalid input. Please enter a number or 'R' for random.")
            return get_value(prompt, max_value)

# Main function
def main():
    # Initialize the Metis engine
    metis = Metis(charset, page_length, MAX_BAY, MAX_SHELF, MAX_VOLUME, MAX_PAGE)

    # Ask user for search type
    search_type = input("Would you like to search by integers or string (i/s)? ").lower()

    if search_type == 'i':
        # Load progress
        progress = load_progress(progress_file)

        # Get user input for bay, shelf, volume, and page
        bay = get_value(f"Enter bay (0-{MAX_BAY}) or 'R' for random: ", MAX_BAY)
        shelf = get_value(f"Enter shelf (0-{MAX_SHELF}) or 'R' for random: ", MAX_SHELF)
        volume = get_value(f"Enter volume (0-{MAX_VOLUME}) or 'R' for random: ", MAX_VOLUME)
        page = get_value(f"Enter page (0-{MAX_PAGE}) or 'R' for random: ", MAX_PAGE)

        # Generate a specific page based on the current parameters
        text = metis.generate_page(bay, shelf, volume, page)
        print(f"Generated text for Bay {bay}, Shelf {shelf}, Volume {volume}, Page {page}: {text[:1000]}...")  # Print the first 1000 characters for verification

        # Update and save progress
        progress['current_bay'] = bay
        progress['current_shelf'] = shelf
        progress['current_volume'] = volume
        progress['current_page'] = page
        save_progress(progress_file, progress)

    elif search_type == 's':
        search_str = input("Enter the string to search for: ")
        results = metis.search_string(search_str)

        if results:
            print(f"Found '{search_str}' in the following locations:")
            for result in results:
                print(f"Bay {result[0]}, Shelf {result[1]}, Volume {result[2]}, Page {result[3]}")
        else:
            print(f"No matches found for '{search_str}'.")

if __name__ == "__main__":
    main()
