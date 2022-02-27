# What is it?
This script opens an emulated version of a browser, runs Telegram where you log in with your account, and reports messages in 200+ propaganda channels on your behalf.
The script was developed by https://github.com/deli841. Message or email me (841deli@gmail.com) in case you have any questions or want to contribute to the Telegram channel database or the algorithm.

# How to use it?
To work with the software, you’ll need to install Python and Git:

- To install Python, follow the instructions for your OS here: https://www.python.org/downloads/release/python-384/
- To install Git, follow the instructions here: https://github.com/git-guides/install-git


## For Windows Users:
1. Clone git repo.
    1. Open any folder on your laptop, run cmd in that folder, and type 
	`git clone https://github.com/deli841/tg_reporter` 
2. Open the folder cloned from GitHub and copy the full path (let’s call it `<MY PATH>`).
3. In Windows Search Bar, enter cmd and choose the first option.
4. In the terminal, run cd `<MY PATH>`
5. Run `python -m venv venv`
6. Activate your venv: `.\venv\Scripts\activate`
7. Install all dependencies: `python -m pip install -r requirements.txt`
8. Install Chrome Simulator: `python installer.py`
9. Run the code: `python main.py`
10. You will be able to see your laptop open the Chrome browser. **Please do not enter or press anything manually in the open browser window.**  Interacting directly with the user interface will break the script. The browser window is there for you to see what is going on in your Telegram. **Enter all the information through the terminal when prompted (phone number and login code).** Please be aware that this information is not stored anywhere and is inaccessible from outside your device.

## Notes:
- In case something does not work, try rerunning all of the scripts again.
- In case you accidentally interact with the browser window and the script breaks, exit, and run python main.py again.
- In case the script encounters a message it cannot report, it will try several times and move on to the next Telegram channel.
- **To stop the script, press Ctrl + C in the cmd. Closing the browser window does not stop the script.**

## Additional:
- Please feel free to contact me via email or GitHub with any ideas and feedback.

