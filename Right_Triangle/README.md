# Introductory Right Triangle Calculator

> Calculate every angle of a right triangle when given 2 of its angles, or calculate the sides and angles of the triangle when given 2 of its sides.

---

## 📝 About this project

This project was built as a learning exercise to practice core Python concepts, including:

- Functions and modular code organization (splitting logic across multiple files)
- Exception handling (`try`/`except`)
- File input/output (reading and writing to text files)
- Input validation with retry loops
- Basic separation of concerns (calculation logic vs. user interaction)

---

## ✨ Features

- **Angle mode**: enter two angles of the triangle to calculate the third one.
- **Side mode**: enter two sides (marking each as hypotenuse or leg) to calculate the missing side and all the angles.
- Every calculated result is saved to a text file, with the name of the user who executed the code.

---

## 🏗️ Technical Analysis

### Data Specifications

| Data Type | Attributes / Variables | Description |
| :--- | :--- | :--- |
| **Input Data** | `side1` (float), `side2` (float), `type1` (string), `type2` (string) / `angle1` (float), `angle2` (float) | Raw inputs collected via CLI user prompts |
| **Output Data** | `angles` (list), `sides` (list) | Calculated results displayed on screen and written to file |

---

## ⚙️ Design & Workflow

Aquí tienes la combinación completa de ambos bloques integrados en un formato de README para GitHub:

```markdown
# Introductory Right Triangle Calculator

> Calculate every angle of a right triangle when given 2 of its angles, or calculate the sides and angles of the triangle when given 2 of its sides.

---

## 📝 About this project

This project was built as a learning exercise to practice core Python concepts, including:

- Functions and modular code organization (splitting logic across multiple files)
- Exception handling (`try`/`except`)
- File input/output (reading and writing to text files)
- Input validation with retry loops
- Basic separation of concerns (calculation logic vs. user interaction)

---

## ✨ Features

- **Angle mode**: enter two angles of the triangle to calculate the third one.
- **Side mode**: enter two sides (marking each as hypotenuse or leg) to calculate the missing side and all the angles.
- Every calculated result is saved to a text file, with the name of the user who executed the code.

---

## 🏗️ Technical Analysis

### Data Specifications

| Data Type | Attributes / Variables | Description |
| :--- | :--- | :--- |
| **Input Data** | `side1` (float), `side2` (float), `type1` (string), `type2` (string) / `angle1` (float), `angle2` (float) | Raw inputs collected via CLI user prompts |
| **Output Data** | `angles` (list), `sides` (list) | Calculated results displayed on screen and written to file |

---

## ⚙️ Design & Workflow

```

[ Mode Selection ]
├── Angle Mode (a)
└── Side Mode (s)

```

### Program Flow

#### 1. Mode Selection
* Ask the user to choose between **Angle mode (`a`)** or **Side mode (`s`)**.

#### 2. Calculation Modes

##### 2.1 Angle Mode (`a`)
1. Ask the user to input the two angles.
2. Calculate the third angle.
3. Save the results in a file.

##### 2.2 Side Mode (`s`)
1. Ask the user to input the two sides and their types (hypotenuse or leg).
2. Calculate the third side.
3. Calculate all the angles.
4. Save the results in a file.

#### 3. Output
* Display the results to the user on the screen.

---

## 📁 File Structure

- `main.py` — Entry point of the program: handles the overall flow and user interaction.
- `calculus.py` — Pure calculation functions (no user interaction): computing sides, angles, and sorting angles.
- `validation.py` — Input validation functions (e.g. asking for a valid number or side type, retrying until valid).
- `data_saving.py` — Handles saving each calculated result to a file.
- `output.py` — Handles printed output/messages shown to the user.

---

## 🚀 How to run it

Requires Python 3. From the project folder:

```bash
python main.py
```