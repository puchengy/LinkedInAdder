# LinkedInAdder

LinkedInAdder is a tool that helps you automatically connect LinkedIn friends.

## Getting Started

### Prerequisites

The tool is developed and tested on MacOSX 10.13.3, using Python2.7.10 some Python libraries need to be downloaded beforehand.

```
pip install selenium
```

### Running

To start the program:

```
python LinkedIner.py
```

## Arguments Explanation

* LinkedIn email (required): the email address of your linkedin email (e.g. --email xxx@gmail.com)
* LinkedIn password (required): the password of your linkedin account (e.g. --password xxxxxxxxxxxxx)
* chromDriver path (optional, defalut: ./chromeDriver): the chrome driver that your senlenium need to invoke (e.g. --chromeDriver ./chromeDriver)
* keyWords (optional, default: ''): keywords in the occupation field of the LinkedIn friends you want to connect
* refreshTime (optional, default: 10s): the refresh time between each recommendation page
* batchSize (optional, default: 10s): how many pages you want to refresh in a batch
* batchInterval (optional, default: 120s): the gap between each batch