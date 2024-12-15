# Google Translate Script

A simple Python script that allows users to translate text from one language to another using the `googletrans` library. The script supports translations for 16 languages, and it provides options for users to view language codes and their corresponding languages.

## Features
- Translate text between 16 languages.
- Option to display available language codes.
- Input the text you want to translate and get the translated result along with pronunciation.
- Simple user interaction through the command line.

## Tech Stack
- Backend: Python 3.x
- Library: `googletrans` (for translation)

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- pip package manager.

### Steps to Run the Project

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/google-translate-script.git
    cd google-translate-script
    ```

2. **Install required libraries:**
    ```bash
    pip install googletrans
    ```

3. **Run the script:**
    ```bash
    python3 translator.py
    ```

4. **Select a language code or view the available options:**
    - Input the language code from the list or type `options` to view available languages.
    - Enter the sentence you want to translate.
    - Type `close` to exit the program.

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
├── translator.py           # Main script for translating text
├── LICENSE                 # License information (optional)
└── README.md               # Project documentation
