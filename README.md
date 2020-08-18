# Link checker

This simpe script checks for broken links (A tag) and missing images (IMG tag) in a learning-library lab.
It can be adapted easily to any website by adapting the XPATH of the containers to check

## Installation

1. Create a virtual environment. 

This is assuming a default Python 3.x, otherwise replace the `$(which python)` statement with the path to a Python 3.x binary

```
virtualenv -p $(which python) .venv 
```

2. Get in the virtual environment

```
. .venv/bin/activate
```

3. Install requirements

```
pip install -r requirements.txt
```

4. Install the Chrome webdriver

Make sure you download the same version as the local Chrome version (currently 84.x)

https://chromedriver.chromium.org/downloads


## Run the test

Either set an environment variable for the BASE URL, or pass it as a parameter to the script.

```
python test_links.py -b <BASE_URL_OF_LAB_TO_SCAN>
```

for example:

```
% python test_links.py -b https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/workshops/freetier/
https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/workshops/freetier/
Checking each lab
scanning 6 labs
UNIQUE LINKS
https://apex.oracle.com/autonomous
https://apexapps.oracle.com/pls/apex/f?p=133:1:::::P1_FEEDBACK:1
https://myservices.us.oraclecloud.com/mycloud/signup?language=en
https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/workshops/freetier/?lab=lab-1-create-app-spreadsheet
https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/workshops/freetier/?lab=lab-3-improve-report-form
https://apex.oracle.com/en/learn/tutorials
https://apex.oracle.com/
https://apex.oracle.com/community
https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/workshops/freetier/?lab=lab-2-improve-faceted-search
https://apex.oracle.com./
http://apex.world/
https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/0-workshop-intro-and-setup/files/spreadsheet-app.sql
https://cloud.oracle.com/en_US/sign-in
https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/workshops/freetier/?lab=lab-4-link-calendar
NON-REACHABLE LINKS:
IMAGES NOT FOUND:
('not found', 'https://oracle.github.io/learning-library/developer-library/apex/spreadsheet/0-workshop-intro-and-setup/images/menu-button.png')
```
