
# WiFi Auto Login Script

This is a Python script that automates the login process for a WiFi network using Selenium. The script opens a browser, navigates to the login page, fills in the username and password fields, and logs in.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x
- You have installed Selenium
- You have ChromeDriver installed and its path is correctly set in the script

## Installing Selenium

To install Selenium, run the following command:

```bash
pip install selenium
```

## Setting Up ChromeDriver

1. Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/downloads).
2. Unzip the downloaded file.
3. Copy the path to the `chromedriver.exe` file and update the path in the script.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/wifi-auto-login.git
cd wifi-auto-login
```

2. Create a file named `keysus.py` in the project directory and add your WiFi login credentials:

```python
# keysus.py
user = "your_username"
passw = "your_password"
```

3. Run the script:

```bash
python wifi_auto_login.py
```

## Script Explanation

- The `Browser` class initializes a Chrome browser session using Selenium.
- The `open_page` method opens the specified URL.
- The `add_input` method inputs text into specified fields.
- The `click_button` method clicks the specified button.
- The `login_wifi` method automates the login process:
  - Checks if the login button is present.
  - Inputs the username and password.
  - Clicks the login button.
  - Verifies if the login was successful.

## Troubleshooting

If you encounter any issues, ensure:

- You have an active internet connection.
- Your ChromeDriver path is correct.
- Your WiFi login credentials in `keysus.py` are correct.

