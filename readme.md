# Pig Latin Translator (WIP)

This web app is designed to translate any english words or sentences into pig latin! Please keep in mind that this 
project as a whole is still in progress. 

#### Prerequisites
- Python 3.11.4 (or higher)
- [Streamlit]("https://streamlit.io/")
- Pytest (For Unit Testing)
```commandline
pip install requirements.txt
```

This project comes in three different flavors! 
- Command Line Interface
- GUI Interface (Currently broken need to fix)
- Web App

In order to run the GUI or CMD app please run the `gui.py` or `command_line_interface.py` scripts. 

### How to run web app
In your terminal run 
```commandline
streamlit run webapp.py
```

### Unit Testing
This Project also contains unit tests to confirm the underlying logic is working correctly
while I am continuing to improve the application.

The unit tests are built using the `pytest` module.

## Roadmap:
- Update layout of webapp (In progress)
- Add more functionality to web app
  - Clear button 
  - Reverse translator 
  - ETC.
- Fix Gui App