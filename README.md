# HW10-Tester

Tests for CS540 Spring 2022 HW10: Reinforcement Learning
* More tests needed, please feel free to contribute. *

## Changes
 - Updated to support Spring 2022 Implementation
 
### Version 
  IN_DEVELOPMENT

## Usage

Download [tests.py](tests.py), [Q_learning.csv](Q_learning.py), and move them into the same directory. In order for tests.py to successfully run, it requires (Q_TABLE.pkl) which is created by running [Q_learning.csv](Q_learning.py). 

The contents of your directory should look like this:

```shell
$ tree
.
├── tests.py
├── Q_learning.py
└── Q_TABLE.pkl
```

To run the tests, reference [hw10.pdf](hw10.pdf) where you'll find the required dependencies needed.

Once all dependencies are install, you may run the tests using:

```python
$ python3 tests.py
```
## Disclaimer

These tests are not endorsed or created by anyone working in an official capacity with UW Madison or any staff for CS540. These tests take portions from the official tests with modification to assist in grading the robustness of student implementations. Tests created/modified are not guaranteed to be correct. Use tests at your own risk. 

By running `tests.py`, you are executing code you downloaded from the internet. Back up your files and take a look at what you are running first.

For any comments, questions, and contribution -- create a pull request.
