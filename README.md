# Coding cat public problems

[Coding Cat](https://github.com/tsani/coding-cat) is a simple, in-browser platform for doing small
Python problems to learn programming.

This repository contains the publicly available problems for Coding Cat.

# Structure of the problems

Each problem must be in its own directory. The directory name should meaningfully reflect the
problem description.

Each directory must contain the following files to describe the coding problem.

- `description.md`
  This is the problem prompt prompt and explains the problem.
- `io.json`
  The file consists of one JSON array of objects. Each object has the following properties:
  - `input`, whose value is itself an array of the inputs to call the student function with.
  - `output`, whose value is the expected output of the student function
- `meta.json`
  The metadata of the problem. This is a JSON object with the following keys.
  - `title`: a human-readable name for the problem
  - `name`: an internal name for the problem that MUST NOT be changed. This name MUST also match
    the name of the function defined in `starter.py`.
    (This name is used as a key in the persistence layer to store student progress on problems.)
  - `difficulty`: a number describing how challenging the problem is.
  - `author`: the name of the person who wrote the problem
  - `category`: a string used to group the problems
- `starter.py`: the python starter code for the problem

NOTE: the name in meta must be the name of the functino you want to test and
run, in most cases this is the exact same function name as the starter function
name!

# Building

Included in this repo is a build script for compiling the list of problems into `problems.js`,
which is then imported by the main Coding Cat UI.

- `build-problem` compiles one problem specified as the name of the directory for the problem. This
  produces a `problem.json` file in the problem directory.
- `build-all-problems` compiles all problems (including disabled ones), generating a `problem.json`
  in each problem directory.
- `build-problem-list` compiles `problems.js` in the root directory. This js file imports each
  `problem.json` file for each problem and defines a default export of a list of all the problem
  objects.

# Enabling/disabling problems

The file `enabled-problems` controls which problems actually get build into `problems.js`. It is a
list of problem names, or entire categories, i.e. strings that appear under the `name` or `category` key in `meta.json`.

`enable-all-problems` is a script that generates an `enabled-problems` file listing all problems as
enabled.

If no `enabled-problems` file is defined, every problem is enabled by default.
