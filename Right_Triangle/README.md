# Introductory Right Triangle Calculator

## About this project

This project was built as a learning exercise to practice core Python concepts, including:

- Functions and modular code organization (splitting logic across multiple files)
- Exception handling (`try`/`except`)
- File input/output (reading and writing to text files)
- Input validation with retry loops
- Basic separation of concerns (calculation logic vs. user interaction)

## Features

- **Angle mode**: enter two angles of the triangle to calculate the third one.
- **Side mode**: enter two sides (marking each as hypotenuse or leg) to calculate the missing side and all the angles.
- Every calculated result is saved to a text file, with the name of the user who executed the code.

## How to run it

Requires Python 3. From the project folder:

```bash
python main.py
```

## Structure

- `main.py` — entry point of the program: handles the overall flow and user interaction.
- `calculus.py` — pure calculation functions (no user interaction): computing sides, angles, and sorting angles.
- `validation.py` — input validation functions (e.g. asking for a valid number or side type, retrying until valid).
- `data_saving.py` — handles saving each calculated result to a file.
- `output.py` — handles printed output/messages shown to the user.

## Example

```
Welcome to the Pythagorean theorem calculator
What's your name?: Tomás
Write 'a' for angle mode or 's' for side mode: s
Write the first side of the triangle: 3
Write the second side of the triangle: 4
Write the type of the first side (hypotenuse, leg): leg
Write the type of the second side (hypotenuse, leg): leg

With the sides you gave, the program has calculated the third one:
[3.0, 5.0, 4.0]
Finally with those sides, it has calculated all the angles of the triangle:
[36.87, 90.0, 53.13]
```