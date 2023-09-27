# For Insider Web-Automation Project
## Test Automation Example
### Insider Website Automations
While I work in these automation project, I used Firefox webdriver.

Please, look at this link:
https://github.com/mozilla/geckodriver/releases
![image](https://user-images.githubusercontent.com/74399824/210509205-80d8b50b-6449-4319-bf87-561121445545.png)

**WEBPAGE_BASEURL = "https://useinsider.com/"**

A few simple steps on the site above xpath, ccs selector, etc. i tried to use it to make it happen.

i've also imported the following library(s) in my development.
## **Librarys & Modules**
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

import pytest
import time
import sys
