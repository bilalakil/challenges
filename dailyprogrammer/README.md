## Execution

### Locally

**Dependencies**

- Haskell 8.0.1
- HUnit 1.5.0.0

**Usage**

Simply CD to the directory and execute the `.hs` file you desire:

    cd easy/302
    ./Test.hs
    ./Main.hs

### Via Docker

**Usage**

> Note: Builds a `local/haskell-w-hunit` image.

Use via the `via-docker` script (that's in this directory):

    ./via-docker easy/302/Main.hs

This will mount `easy/302` to `/app`,
CD to that directory, and then execute `Main.hs` - 
similar to the local usage steps above.
