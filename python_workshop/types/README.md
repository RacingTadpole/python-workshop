# Static Typing in Python

## Why?

The big ones for me:

- MUCH easier to debug other people's code - and your own - if you know what sort of thing every function returns, and expects
- Your IDE can click through to definitions of all your variables
- You get warned when things might be None, and have to explicitly deal with it.
- Easier to refactor, eg. change return value from int to list of ints, set of ints, frozenset of ints

## How?

Can do it progressively with choice of flags in your `mypy.ini` file:

- Either a global `disallow_untyped_defs = False`
- Or, enforce module by module with (to ignore `src.tests`):
    ```
    [mypy-src.tests.*]
    ignore_errors = True
    ```
- You will also need `ignore_missing_imports` for every imported package that doesn't provide type information:
    ```
    [mypy-pytest]
    ignore_missing_imports = True
    ```

## Downsides

- Takes some effort.
- Doesn't cover every case, eg.
    - no SortedSet[], which I have wanted to indicate an ordered sequence with no duplicates
