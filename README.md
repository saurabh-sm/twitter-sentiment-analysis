# Twitter Sentiment Analysis

## Online Setup

+ Register for a developer account on Twitter on:

  `https://developer.twitter.com/en`

  (**NOTE**: This will need to be approved by Twitter)

+ Create a new application

----

## Local Setup

+ Navigate to `$PROJECT_ROOT` directory

+ Initiate Python 3 virtual environment:

  `python3 -m venv twitter`

+ Activate newly created virtual environment:

  `source twitter/bin/activate`

+ Install required packages in the virtual environment:

  `pip install --requirement requirements.txt`

+ From the application settings on `developer.twitter.com`, put the details in a `.env`. The environment variables in this file are only valid for one shell session

  (**NOTE**: `CONSUMER_KEY` is the `API_KEY`, **and** `CONSUMER_SECRET` is the `API_SECRET_KEY`)

----

## Program Execution

+ In the `$PROJECT_ROOT` directory, execute:

  `python streamer.py`

----

## Output

Executing the above command will produce an output consisting of a number of attributes in the form of key-value pairs. Each tweet will be a dictionary having attributes like `created_at`, `id`, `text`, `source`, etc.
