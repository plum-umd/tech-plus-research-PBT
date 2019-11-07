# Tech + Research project for Property-based Testing in Python

## Setup

Install Pipenv for your system by following the instructions [here](https://pipenv.kennethreitz.org/en/latest/install/#homebrew-installation-of-pipenv).

Clone this repository and run the following command:

```
pipenv install
```

It will install all packages (Hypothesis, pytest) and set up a virtual environment. After that you can start running the example programs.

To run an example test run:

```
pipenv run pytest example.py
```

## Example

### Run length encoding

Run length encoding is a way to compress data (you can read more on [Wikipedia](https://en.wikipedia.org/wiki/Run-length_encoding)). A simplified example is given in the file `rle-1.py`.

A basic property that we can test is given any string s: `decode(encode(s)) == s` should always hold for any run length encoding implementation. The test method at the end tests exactly that using Hypothesis.

To run this use:

```
pipenv run pytest rle-1.py
```

This should give you an empty string because our implementation doesn't handle them.

** TODO **

