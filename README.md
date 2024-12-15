# Google Translate Script with GUI

A Python application that allows users to translate text between multiple languages using the `googletrans` library. Now with a user-friendly Graphical User Interface (GUI) built using `tkinter`, making it easier and more appealing to use.

## Features
- **GUI Interface**: Interact with a visually appealing and user-friendly interface.
- Translate text between 16 languages.
- Select source and target languages from drop-down menus.
- Input text in the GUI text box and view the translated result directly.
- Displays pronunciation and source language.
- Option to close the program via the GUI.

## Tech Stack
- **Backend**: Python 3.x
- **Libraries**: 
  - `googletrans` for translation.
  - `tkinter` for GUI.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- `pip` package manager for installing libraries.

### Steps to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/farhat-1203/google-translate-script.git
    cd google-translate-script
    ```

2. **Install required libraries**:
    ```bash
    pip install googletrans==4.0.0-rc1
    ```

3. **Run the script**:
    ```bash
    python3 gui_translator.py
    ```

4. **Use the GUI**:
    - Select the source language and target language from the drop-down menus.
    - Enter the text to translate in the input box.
    - Press the **Translate** button to view the translated text, its pronunciation, and the source language.

### Language Options and Their Codes

| Code | Language   |
|------|------------|
| bn   | Bangla     |
| en   | English    |
| ko   | Korean     |
| fr   | French     |
| de   | German     |
| he   | Hebrew     |
| hi   | Hindi      |
| it   | Italian    |
| ja   | Japanese   |
| la   | Latin      |
| ms   | Malay      |
| ne   | Nepali     |
| ru   | Russian    |
| ar   | Arabic     |
| zh   | Chinese    |
| es   | Spanish    |

### Project Structure
```plaintext
google-translate-script/
├── gui_translator.py       # Main script with GUI functionality
├── LICENSE                 # License information (optional)
└── README.md               # Project documentation
