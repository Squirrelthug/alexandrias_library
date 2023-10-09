# Alexandria's Library

## Overview

Alexandria's Library is a Python project designed to simulate an infinitely expansive library. Each "page" in this library is generated based on a unique combination of parameters, including bay, shelf, volume, and page numbers. The project aims to explore the concept of a library that contains all possible combinations of a given character set, akin to Jorge Luis Borges' "The Library of Babel."

## Features

Random Page Generation: Generate a random page from the library based on user input.
Coherence Scoring: (Planned) Score the coherence of generated pages to find meaningful content.
Logging: Keep track of the last processed location in the library.

## Requirements

Python 3.x
Sympy
(Any other dependencies)

## How to Run

Clone the repository to your local machine.
Navigate to the project directory.
Run main.py to start the program.

python main.py
You'll be prompted to enter the number of random iterations you'd like to see. The program will then generate that many random pages from the library. Each page has 10,000 characters so it's a lot to print out but it prints pretty quickly. Mostly gibberish with random bits of coherence. And the engine that drive the combination of letters still needs work because I'm not a mathematician.

## Future Plans

Implement a coherence scoring mechanism to evaluate the meaningfulness of generated pages.
Add a feature to "tweet" or otherwise share particularly coherent or interesting pages.
Implement a user interface for easier navigation and interaction.

## Contributing

Feel free to fork the project and submit a pull request with your changes!
