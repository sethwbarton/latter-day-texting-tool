
## Dev Setup

### Installing Python and a Virtual Environment

To run this project, you need to have Python3 installed on your machine. You can download Python from the official website.
Once you have Python installed and have cloned the repo, create a virtual environment by running the following command in
the root directory of the project;

```bash
python3 -m venv venv
```

You can create your venv however suits you best. I prefer letting Pycharm do the work.

### Installing Dependencies

Dependencies for this project are located in the `requirements.txt` file. To install them, run the following command 
inside your virtual environment;

```bash
pip install -r requirements.txt
```
    
### Running the Tests

You can run the tests with `make test` or `pytest`. The tests are located in the `__tests__` directory.

### Running the Application

To run the application, run `main.py` in your virtual environment.

### Opening a Pull Request

Once you've made the changes you wanted, fork the repository and open a pull request against mine. Please ensure
any changes you make are well documented and have automated tests or they will not be accepted.

