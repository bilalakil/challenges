CodeChef solutions are developed using Python (v3.4),
and are simply scripts without external dependencies
that take input from `stdin` and output to `stdout`.

## Execution

### Locally

**Dependencies**

- Python 3.5.3

**Usage**

Simply execute the desired Python file:

    cook77/chefsetc.py -test

If your `/usr/bin/env python --version` is ~2,
you can pass the file into `python3` instead of executing it directly:

    python3 cook77/chefsetc.py -test

### Via Docker

**Dependencies**

- `brew install coreutils` (linked) on a Mac.

**Usage**

Use via the `via-docker` script (that's in this directory):

    ./via-docker cook77/chefsetc.py -test

This will mount `cook77` to `/app`
and then execute `./chefsetc.py` from within `/app` -
achieving a result somewhat similar to the local usage steps above.

### Script Options

Each script may have different invocation options.
`-test` is the only one which they should share in common.

You can read the `if __name == '__main__'` section
at the bottom of a script to see its available options.

