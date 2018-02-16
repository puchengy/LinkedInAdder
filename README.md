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

### Two Modes

#### Mode 1: Add All Mode

Adding all the connections that LinkedIn has recommended to you in the page: https://www.linkedin.com/mynetwork/

```
python LinkedIner.py --email xxx --password xxx
```

#### Mode 2: Filter Mode

Add new connections by filtering keyWords (see "Arguments Explanation")

```
python LinkedIner.py --email xxx --password xxx --keyWords "CMU,Google,Uber,Amazon,Software Engineer,Carnegie Mellon University"
```

## Arguments Explanation

* LinkedIn email (required): the email address of your linkedin email (e.g. --email xxx@gmail.com)
* LinkedIn password (required): the password of your linkedin account (e.g. --password xxxxxxxxxxxxx)
* chromDriver path (optional, defalut: ./chromeDriver): the chrome driver that your senlenium need to invoke (e.g. --chromeDriver ./chromeDriver)
* keyWords (optional, default: ''): keywords in the occupation field of the LinkedIn friends you want to connect. The keywords must have double quotes surrounded, and each filter word should be separated by ',' and it is case insensitive. (e.g. --keyWords "CMU,Google,Uber,Amazon,Software Engineer,Carnegie Mellon University")
* refreshTime (optional, default: 10s): the refresh time between each recommendation page. (e.g. --refreshTime 5)
* batchSize (optional, default: 10s): how many pages you want to refresh in a batch. (e.g. --batchSize 10)
* batchInterval (optional, default: 120s): the gap between each batch. (e.g. --batchInterval 120)