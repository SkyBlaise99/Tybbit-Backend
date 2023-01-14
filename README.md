# Tybbit-Backend

Backend for Tybbit

Installation:
1. `python -m venv .venv`
1. `.venv\Scripts\activate.bat`
1. `pip install -r requirements.txt`

Running the app:
* Windows: `flask run`

## API

* Add:
  * `/add`
    * Json Example:
      ``` json
      {
        "name": "test",
        "score": 123
      }
      ```
* Get:
  * `/get`
