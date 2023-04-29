
# Battery-price-web-scrape

This is a Flask app that scrapes the price of a lithium-ion battery from a website and returns it as a JSON response

## Deployed application link
- https://battery-price-scrape.netlify.app/price/

## Prerequisites

- Python 3.11
- Flask
- Beautiful soup
- Requests


## Installation

#### Clone the repository to your local machine

```bash
git clone https://github.com/chetan-droid/Price-web-scrape.git
```

#### Create Virtutal environment

```bash
  python -m venv./venv
```

#### Activate Virtutal environment

```bash
source venv/Scripts/Activate
```

#### Command to deactivate the Virtutal environment

```bash
deactivate
```

#### Install packages

```bash
pip install -r requirements.txt
```

### To run application

```bash
python app.py
```

### To build 

```bash
python build.py
```


## API Reference

#### GET the price of battery

```http
  GET /price/
```



## Credits

This project is created by Chetan Kumar for assessment purpose.

