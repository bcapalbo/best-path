# Best Path Application

This is an application that give the cheapest route given pre-fixed route prices.

## Getting Started

## Prerequisites

Before start, you must to have installed in your machine this prerequisites:
* **[Python 2.7](https://www.python.org/)** -
To install Python, [see official documentation](https://wiki.python.org/moin/BeginnersGuide/Download) according to you OS.

## Installing

### Develop

To install on your local machine, just follow these steps:

**1**. Clone and enter project
```
$ git clone git@github.com:bcapalbo/best-path.git
$ cd best-path
```

### Running the application

To run the application you must to pass two parameters:
- input-routes.csv (there is an example of content on this repo)
- GRU-CDG

**Example**
```
$ python app/best_path.py input-routes.csv GRU-CDG
```

### Running unit tests

To run unit tests, you will need to install pytest package, [see official documentation](https://docs.pytest.org/en/latest/getting-started.html#getstarted) according to you OS.

After pytest installation, just run the following command:

```
$ pytest
```

## Built With

* [Python 2.7](https://www.python.org/)

## Author

This project is mantained by Bruno Capalbo (https://github.com/bcapalbo).
