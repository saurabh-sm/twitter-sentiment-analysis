[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f7e3281daeed4c90bcc395a3e73d0164)](https://app.codacy.com/gh/saurabmish/Twitter-Sentiment-Analysis?utm_source=github.com&utm_medium=referral&utm_content=saurabmish/Twitter-Sentiment-Analysis&utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/ebcadff8123f94444cd9/maintainability)](https://codeclimate.com/github/saurabmish/Twitter-Sentiment-Analysis/maintainability)
[![codecov](https://codecov.io/gh/saurabmish/Twitter-Sentiment-Analysis/branch/master/graph/badge.svg?token=T6CFHNNEPL)](https://codecov.io/gh/saurabmish/Twitter-Sentiment-Analysis)
[![Build Status](https://travis-ci.org/saurabmish/Twitter-Sentiment-Analysis.svg?branch=master)](https://travis-ci.org/saurabmish/Twitter-Sentiment-Analysis)

# Twitter Sentiment Analysis

## Setup

+ Navigate to desired directory to execute the program and test cases. This directory will be called as `$PROJECT_ROOT`

+ Initiate git:

  `git init`

+ Associate current directory with remote repository:

  `git remote add origin https://github.com/saurabmish/Twitter-Sentiment-Analysis.git`

+ Fetch project from remote repository:

  `git pull origin master`

+ Initiate Python 3 virtual environment:

  `python3 -m venv twitter`

+ Activate newly created virtual environment:

  `source twitter/bin/activate`

+ Update pip:

  `pip install --upgrade pip`

+ Install required packages in the virtual environment:

  `pip install --requirement requirements.txt`

----

## Execution

+ To run *test cases*, execute the below command in `$PROJECT_ROOT`:

  `pytest -v`

+ To run the *program*, execute the below command in `$PROJECT_ROOT`:

  `python app/streamer.py`

----

## Output

Executing the above command will produce an output consisting of a number of attributes in the form of key-value pairs. Each tweet will be a dictionary having attributes like `created_at`, `id`, `text`, `source`, etc.
