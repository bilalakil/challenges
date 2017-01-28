## Execution

### Locally

**Dependencies**

- Python 3.4.6

**Usage**

Simply execute the desired Python file:

    cook77/chefsetc.py -test

If your `/usr/bin/env python --version` is ~2,
you can pass the file into `python3` instead of executing it directly:

    python3 cook77/chefsetc.py -test

### Via Docker

**Usage**

Use via the `via-docker` script (that's in this directory):

    ./via-docker cook77/chefsetc.py -test

This will mount `cook77` to `/app`
and then execute `/app/chefsetc.py` -
similar to the local usage steps above.
