Certainly! Since you've built a modular calculator with history management and parentheses support, a professional **README.md** should highlight these technical features.

Here is a clean, structured README in English for your project:

---

# My Calculator Project

A robust command-line calculator built with Python. This project features a custom-built mathematical engine capable of handling operator precedence, nested parentheses, and calculation history.

## 🚀 Features

* **Custom Tokenizer**: Parses strings into mathematical tokens, handling operators, floats, and parentheses.
* **Recursive Math Engine**: Supports nested parentheses `(2 + (3 * 4))` using a recursive evaluation logic.
* **Operator Precedence**: Correctly follows math rules (Power > Multiplication/Division > Addition/Subtraction).
* **History Management**: Automatically saves calculations to a text file. You can view or clear the history at any time.
* **Robust Error Handling**: Detects division by zero, unclosed parentheses, and unsupported characters.

## 🛠️ Supported Operators

| Operator | Action | Example |
| --- | --- | --- |
| `+`, `-` | Addition & Subtraction | `5 + 3` |
| `*`, `/` | Multiplication & Division | `10 / 2` |
| `^` or `**` | Power (Exponent) | `2 ^ 3` (8) |
| `%` | Modulo (Remainder) | `10 % 3` (1) |
| `!` or `//` | Integer Division (Rounded) | `7 ! 2` (4) |
| `>`, `<` | Max & Min | `5 > 8` (8) |
| `( )` | Parentheses | `(2 + 3) * 4` |

## 📦 Project Structure

* `menu.py`: The main entry point. Manages the CLI loop and user commands.
* `engine.py`: The core logic. Contains the reduction engine and operator functions.
* `parser.py`: Contains the `tokenizer` that cleans and splits the input string.
* `history.py`: Handles reading, writing, and deleting the `calculs.txt` file.
* `text.py`: Centralizes all interface messages and formatting settings.

## 💻 Installation & Usage

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/alarcon-prevert-julien-my-calculator.git
cd alarcon-prevert-julien-my-calculator

```


2. **Run the application**:
```bash
python menu.py

```


3. **Commands**:
* Type your math expression (e.g., `(15 + 5) * 2`) to get a result.
* `history`: Display previous calculations.
* `delete`: Wipe the history file.
* `help`: Show available commands.
* `quit`: Exit the program.



## 🛡️ Technical Highlights

Instead of using the dangerous `eval()` function, this project implements a **Lexer/Parser** approach:

1. **Tokenization**: Input is cleaned and converted into a list.
2. **Parentheses Solving**: The engine recursively finds the innermost parentheses and calculates them first.
3. **Linear Reduction**: Using `apply_ope`, the engine reduces the token list based on the order of operations.

---

### Would you like me to add a "License" or "Authors" section at the end of this file?
