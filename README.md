# README.md

# Periodic Interpreter

This project is a fun experiment that converts words and sentences into periodic elements while keeping pronunciation as close as possible to the original. It can only work with a series of space-separated words and does not currently support punctuation, special characters, or complex formatting.

## How to use

1. Install Python (if you haven't already) by downloading it from [python.org](https://www.python.org/downloads/).
2. Clone or download this repository to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the `periodic_interpreter.py` script using the command `python periodic_interpreter.py`.
5. Enter a sentence or a series of space-separated words to convert into periodic elements.

## Building the app

To build the app, you can use the `pyinstaller` tool. Follow these steps:

1. Install `pyinstaller` by running `pip install pyinstaller` in your terminal or command prompt.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the command `pyinstaller periodic_interpreter.spec` to build the app.
4. The built app will be located in a `dist` folder within the project directory.