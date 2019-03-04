# Best Path Application

This is an application that gives the cheapest route given pre-fixed route prices. It was build using Python2.7 as cli application. Must be inserted two parameters that will provide a list of routes, where is the start place and where is the goal place. Was used Dijkstra's algorithm to find the best option. A community version of this algorithm was used as base to implements the code that fits with the proposed problem.

[The problem to solve](https://github.com/bcapalbo/best-path/blob/develop/SPECIFICATION.md)

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
