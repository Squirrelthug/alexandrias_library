import random
from library_engine import LibraryEngine
from metis import Metis
import json
import openai

# Configuration
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.;'!? "
page_length = 3200  # Number of characters on a page
file_path = 'processed_pages.txt'
results_file = 'results.txt'

# Logical Maximum Values
MAX_BAY = 1000000 # large number for practical purposes
MAX_SHELF = 20  # Four walls with five shelves each
MAX_VOLUME = 32 # Thirty-two books per shelf
MAX_PAGE = 410 # Four hundred and ten pages per book

# load progress
def load_progress(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'current_bay': 0, 'current_shelf': 0, 'current_volume': 0, 'current_page': 0}

# save progress
def save_progress(file_path, progress):
    with open(file_path, 'w') as f:
        json.dump(progress, f)

# process a page with LLM
def process_page_with_llm(page_content):
    response = openai.Completion.create(
        engine="davinci",  # or your preferred engine
        prompt=page_content,
        max_tokens=50
    )
    return response.choices[0].text
# store significant pages
def store_significant_page(file_path, page_content, result):
    with open(file_path, 'a') as file:
        file.write(f"Page Content: {page_content}\n")
        file.write(f"Result: {result}\n")
        file.write("--------\n")


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
    metis = Metis(charset, page_length)

    # Load progress
    progress = load_progress(file_path)

    # Get user input for bay, shelf, volume, and page
    bay = get_value(f"Enter bay (0-{MAX_BAY}) or 'R' for random: ", MAX_BAY)
    shelf = get_value(f"Enter shelf (0-{MAX_SHELF}) or 'R' for random: ", MAX_SHELF)
    volume = get_value(f"Enter volume (0-{MAX_VOLUME}) or 'R' for random: ", MAX_VOLUME)
    page = get_value(f"Enter page (0-{MAX_PAGE}) or 'R' for random: ", MAX_PAGE)

    # Generate a specific page based on the current parameters
    text = metis.generate_page(bay, shelf, volume, page)
    print(f"Generated text for Bay {bay}, Shelf {shelf}, Volume {volume}, Page {page}: {text[:3200]}...")

    # Update and save progress
    progress['current_bay'] = bay
    progress['current_shelf'] = shelf
    progress['current_volume'] = volume
    progress['current_page'] = page
    save_progress(file_path, progress)

    # Process the page with LLM
    #result = process_page_with_llm(text)
    #if "significant" in result:  # Adjust condition based on your criteria
    #    store_significant_page(results_file, text, result)

    # Update and save progress
    #progress['current_bay'] = bay
    #progress['current_shelf'] = shelf
    #progress['current_volume'] = volume
    #progress['current_page'] = page
    #save_progress(progress_file, progress)


if __name__ == "__main__":
    main()