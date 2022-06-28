2022-06-28
# Jug Puzzle Solvers
At its current state, this project takes in a jug puzzle setup with `N` jugs (i.e. volumes of water) and displays a tree diagram of the paths to every possible combination of volumes with the minimum number of operations. The operations considered for each jug is as follows:

1. Fill up the jug, either from an empty or a partially filled state.
2. Empty a jug completely.
3. Transfer/pour as much of the water contained within this jug as possible into any other single jug.

The operations can be tweaked fairly easily in the source code, especially if one has to tackle one of Wikipedia's [water pouring puzzles](https://en.wikipedia.org/wiki/Water_pouring_puzzle) where the jug configuration starts in a non-zero state and only operation 3 is permitted.

# Motivation
I found out about these puzzles as [water pouring puzzles](https://en.wikipedia.org/wiki/Water_pouring_puzzle) at first, then I got a better idea of the theory behind them through Dr Barker's [Create Your Own Jug Puzzle](https://youtu.be/lgEiVSY11mE).

# Usage
## Requirements
**NOTE**: `treelib` does need to be installed in order print out the CLI tree. That can be done with pip:
```
pip3 install treelib
```

## jug_puzzle.py
```
python3 jug_puzzle.py a,b,c,...
```
where `a`, `b`, `c`, and so on are the volumes of the jugs to be considered.

### Example

```console
$ python3 jug_puzzle.py 9,5
28
[0, 0]
├── [0, 5]
│   └── [5, 0]
│       └── [5, 5]
│           └── [9, 1]
│               └── [0, 1]
│                   └── [1, 0]
│                       └── [1, 5]
│                           └── [6, 0]
│                               └── [6, 5]
│                                   └── [9, 2]
│                                       └── [0, 2]
│                                           └── [2, 0]
│                                               └── [2, 5]
└── [9, 0]
    ├── [4, 5]
    │   └── [4, 0]
    │       └── [0, 4]
    │           └── [9, 4]
    │               └── [8, 5]
    │                   └── [8, 0]
    │                       └── [3, 5]
    │                           └── [3, 0]
    │                               └── [0, 3]
    │                                   └── [9, 3]
    │                                       └── [7, 5]
    │                                           └── [7, 0]
    └── [9, 5]
```

# TODO
* I would like to try some form of visualisation (beyond CLI trees) such as the geometric one demonstrated by Dr Barker.
* Pretty up the code with comments and documentation
* There are definitely optimisations to be made (I'm not too familiar with trees...) but this is such a simple algorithm I don't think I'll spend too much time on it.
