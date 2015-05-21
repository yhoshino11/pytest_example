# PyTest Example

### How To Use
```sh
  $ git clone https://github.com/yhoshino11/pytest_example.git
  $ cd pytest_example/
  $ virtualenv .venv
  $ source .venv/bin/activate
  (.venv)$ pip install -r requirements.txt
  (.venv)$ py.test --cov bankaccount.py
  (.venv)$ deactivate # exit virtualenv
  $ rm -rf .venv # destroy virtualenv
```
