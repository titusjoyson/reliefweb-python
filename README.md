# ReliefWeb Python Library

A Python client library for the [ReliefWeb API](https://apidoc.reliefweb.int/).

## Installation

```bash
pip install .
```


## Usage

```python
from reliefweb.client import ReliefWebClient

client = ReliefWebClient()
reports = client.get_reports(filters={"country": {"eq": "ETH"}}, fields=["id", "date", "title"], limit=5)
print(reports)
```

## Running Tests

To run the unit tests, use:

```bash
python -m unittest tests/test_client.py
```

## Features
- Simple interface for ReliefWeb API endpoints
- Handles authentication and pagination

## License
MIT
