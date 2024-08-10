# Translator

Translator-using-PyQt5 is a Python application designed for translating text using the PyQt5 framework. This tool provides a graphical user interface (GUI) that leverages PyQt5 for an interactive and user-friendly experience.

## Prerequisites

To run the Translator-using-PyQt5 application, ensure you have the following prerequisites:

- **Python 3.10 or higher**: Download [Python](https://www.python.org/)
- **Git**: Install [Git](https://git-scm.com/)
- **Basic knowledge of Python and PyQt5**: Familiarity with Python programming and the PyQt5 library is helpful. You can find resources to learn PyQt5 [here](https://riverbankcomputing.com/software/pyqt/intro).

Make sure you have Python and Git installed on your system before starting the installation process.

## Motive

The primary goal of this project is to provide an accessible and easy-to-use translation tool using PyQt5. By leveraging PyQt5, the application aims to offer a graphical interface that enhances user interaction and experience with translation services.

## Get the code

To run this application locally, follow the steps below:

### Step 1: Create a Virtual Environment

Create a virtual environment to manage your project's dependencies. Open a terminal and execute the following commands:

```bash
cd ~/Dev
mkdir ~/Dev/translator -p
cd ~/Dev/translator
python3.10 -m pip install virtualenv
python3.10 -m virtualenv .
source bin/activate
```

### Step 2: Clone Repository

Clone the repository containing the application code and install the necessary dependencies:

```bash
cd ~/Dev/translator
git clone https://github.com/Arvind-4/translator.git .
```

for pip run

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

for poetry run

```bash
poetry install
```

### Step 3: Run the Application

After installing the dependencies, you can run the application using:

```bash
python run.py
```

## Summary

This project implements a simple translator application using Python and the PyQt5 library. The application is built to offer basic translation functionality and is intended for developers and enthusiasts interested in GUI-based translation tools and PyQt5.

## License

This project is licensed under the MIT License. See the [LICENSE file](https://github.com/Arvind-4/translator/blob/main/LICENSE) for more details.

## Contribution Guidelines

We welcome contributions to improve the Translator-using-PyQt5 application. To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive messages.
4.  Push your branch to your forked repository.
5.  Submit a pull request detailing the changes you’ve made.

Please ensure that your code adheres to the existing code style and includes relevant tests if applicable.

## Conclusion

Translator-using-PyQt5 is a straightforward application that demonstrates the capabilities of PyQt5 in building desktop applications. By following the installation instructions, you can set up and run the application locally. Contributions are encouraged, and we look forward to improving the tool with the help of the community.
