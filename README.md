# HW4-Tester

Tests for CS540 Spring 2022 HW4: Clustering
* More tests needed, please feel free to contribute. *

## Changes
 - Updated to support Spring 2022 Implementation
 
### Version 
  IN_DEVELOPMENT

## Usage

Download [test.py](test.py), [Random_Test.csv](Random_Test.csv), and [Tiebreak_Test.csv](Tiebreak_Test.csv) and move them into the directory that contains `pokemon_stats.py` and `Pokemon.csv`

The contents of your directory should look like this:

```shell
$ tree
.
├── pokemon_stats.py
├── Pokemon.csv
├── test.py
├── Random_Test.csv
└── Tiebreak_Test.csv
```

To run the tests, do

```python
$ python3 test.py
```

Ideally, you should be running `test.py` using your terminal as this README describes. If you have an issue, first try running it that way. However, provided that `test.py`, `pokemon_stats.py`, and the 3 csvs are all in the same directory, it should work if you do `%run test.py` in Jupyter, or run it the same way you would run `pokemon_stats.py` in your editor (VS Code, Pycharm, Sublime, etc).

### These tests _do not_ check for `imshow_hac(Z)`. 
### They only test `load_data(filepath)`, `calc_features(row)`, and `hac(features)`.

## Disclaimer

These tests are not endorsed or created by anyone working in an official capacity with UW Madison or any staff for CS540. The tests are made by students, for students.

By running `test.py`, you are executing code you downloaded from the internet. Back up your files and take a look at what you are running first.

For any comments, questions, and contribution -- create a pull request at [https://github.com/CS540-Testers-SP22/HW4-Tester/pulls](https://github.com/CS540-Testers-SP22/HW4-Tester/pulls).
