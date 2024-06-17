import hashlib

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
        self.num_chars = len(characters)

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
        seed = int(seed_hash, 16)

        # Apply modular arithmetic and bit-shifting
        seed = (seed ^ (seed >> 30)) * 0xbf58476d1ce4e5b9
        seed = (seed ^ (seed >> 27)) * 0x94d049bb133111eb
        seed = seed ^ (seed >> 31)

        return seed % (2**64)

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
        page_text = []

        for i in range(self.page_length):
            # Use modular arithmetic and bit-shifting to generate a deterministic sequence
            char_index = (seed + i) % self.num_chars
            page_text.append(self.characters[char_index])
            # Update seed to create a sequence
            seed = (seed * 6364136223846793005 + 1) % (2**64)

        return ''.join(page_text)
