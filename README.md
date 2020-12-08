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

  `python3 -m venv twitter-sentiment`

+ Activate newly created virtual environment:

  `source twitter-sentiment/bin/activate`

+ Update pip:

  `pip install --upgrade pip`

+ Install required packages in the virtual environment:

  `pip install --requirement requirements.txt`

+ Set environment variables (convenient way of setting `PYTHONPATH`) :

  `source .env`

+ Download and install [Elasticsearch] and [Kibana]

+ Start services for elasticsearch and kibana:

  **Linux**:

  ```
  sudo -i service elasticsearch start
  sudo -i service kibana start
  ```
  **macOS**:

  ```
  brew services start elasticsearch-full
  brew services start kibana-full
  ```

+ Check Elasticsearch status in the terminal:

  `curl -X GET "localhost:9200/?pretty"`

  Expected Output:

  ```
  {
    "name" : "thinkpad-t480",
    "cluster_name" : "elasticsearch",
    "cluster_uuid" : "BZSMYSWPRp26y_pniprZVw",
    "version" : {
      "number" : "7.10.0",
      "build_flavor" : "default",
      "build_type" : "deb",
      "build_hash" : "51e9d6f22758d0374a0f3f5c6e8f3a7997850f96",
      "build_date" : "2020-11-09T21:30:33.964949Z",
      "build_snapshot" : false,
      "lucene_version" : "8.7.0",
      "minimum_wire_compatibility_version" : "6.8.0",
      "minimum_index_compatibility_version" : "6.0.0-beta1"
    },
    "tagline" : "You Know, for Search"
  }
  ```

+ Check Kibana status in the web browser:

  `http://localhost:5601/app/dev_tools#/console?load_from=https:/www.elastic.co/guide/en/elasticsearch/reference/7.10/snippets/19.console`


----

## Execution

+ To run *test cases*, execute the below command in `$PROJECT_ROOT`:

  `pytest -v`

+ To check *coverage* (source code and test cases), execute the below command in `$PROJECT_ROOT`:

  `pytest --cov -v`

+ Run flask microservices:

  `flask run`

+ On the web browser, go to:

  `http://127.0.0.1:5500/`

+ Setup monitoring:

  + Go to the [Elasticsearch dashboard]

  + Scroll down to *Management* in the dock navigation menu

  + Click on *Stack Management*

  + Under the *Kibana* section, click on "*Index Patterns*"

  + The *index* attribute associated with the `elasticsearch.index` object will show up; select it and verify the fields

  + Click on the dock navigation menu and go to *Discover* under the Kibana section

    + Here the data streamed by `app/streamer.py` will be displayed.

    + Figure out data which will be visualized on the x and y axis.

  + Now click on the dock navigation menu and go to *Dashboard* under the Kibana section

    + Create the desired visualization

----

[Elasticsearch]: https://www.elastic.co/downloads/elasticsearch
[Kibana]: https://www.elastic.co/downloads/kibana
[Elasticsearch dashboard]: http://localhost:5601/app/management
