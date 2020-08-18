
## Installation

1. Create a virtual environment
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

4. Install a browser driver, we'll use Chrome headless

https://chromedriver.chromium.org/downloads

## Run the test

```
python test_links.py -b <BASE_URL_OF_LAB_TO_SCAN>
```