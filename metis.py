import hashlib
import random


class Metis:
    def __init__(self, characters, page_length):
        """
        Initialize the Metis algorithm.

        Parameters:
        characters (str): The set of characters to use.
        page_length (int): The number of characters per page.
        """
        self.characters = characters
        self.page_length = page_length

    def calculate_seed(self, bay, shelf, volume, page):
        """
        Calculate a unique seed based on bay, shelf, volume, and page numbers.

        Parameters:
        bay (int): The bay number.
        shelf (int): The shelf number.
        volume (int): The volume number.
        page (int): The page number.

        Returns:
        int: The unique seed value.
        """
        seed_str = f"{bay}-{shelf}-{volume}-{page}"
        seed_hash = hashlib.sha256(seed_str.encode()).hexdigest()
        return int(seed_hash, 16)

    def generate_page(self, bay, shelf, volume, page):
        """
        Generate a page based on bay, shelf, volume, and page numbers.

        Parameters:
        bay (int): The bay number.
        shelf (int): The shelf number.
        volume (int): The volume number.
        page (int): The page number.

        Returns:
        str: The generated page.
        """
        seed = self.calculate_seed(bay, shelf, volume, page)
        random.seed(seed)
        return ''.join(random.choice(self.characters) for _ in range(self.page_length))
