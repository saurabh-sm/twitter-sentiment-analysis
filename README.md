# Twitter Sentiment Analysis

## Setup

+ Navigate to `$PROJECT_ROOT` directory

+ Initiate Python 3 virtual environment:

  `python3 -m venv twitter`

+ Activate newly created virtual environment:

  `source twitter/bin/activate`

+ Install required packages in the virtual environment:

  `pip install --requirement requirements.txt`

----

## Execution

+ To run *test cases*, execute the below command in `$PROJECT_ROOT`:

  `pytest -v`

+ To run the *program*, execute the below command in `$PROJECT_ROOT`:

  `python streamer.py`

----

## Output

Executing the above command will produce an output consisting of a number of attributes in the form of key-value pairs. Each tweet will be a dictionary having attributes like `created_at`, `id`, `text`, `source`, etc.
