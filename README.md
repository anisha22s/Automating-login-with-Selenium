# **Automating-login-with-Selenium**

This project demonstrates how to use Selenium with chromedriver to log into an account using cookies. It consists of two Python files:

load_cookies.py: Loads cookies from a file and adds them to a Selenium webdriver to log in to a website.
save_cookies.py: Logs in to a website using a username and password, saves the cookies to a file, and exits.

## **Requirements**

Python 3.x
Selenium  
Chromedriver  

## **Installation**

Clone this repository to your local machine.
Install the required packages by running pip install -r requirements.txt.
Download the appropriate version of Chromedriver and place it in the repository's root directory.


## **Usage**

**Loading cookies**
1. Ensure that you have cookies saved in a file named cookies.pkl.
2. Run the load_cookies.py file using the command python load_cookies.py.
3. The script will load the cookies and add them to a Selenium webdriver.
4. The webdriver will navigate to the logged-in page of the website.

**Saving cookies**
1. Replace the username and password variables in save_cookies.py with your own login credentials.
2. Run the save_cookies.py file using the command python save_cookies.py.
3. The script will log in to the website using your credentials and save the cookies to a file named cookies.pkl.

## **Notes**

1. This project was tested on macOS using Chromedriver version 89 and Google Chrome version 89.
2. You may need to modify the executable_path variable in the Python files to point to the location of your Chromedriver executable.
