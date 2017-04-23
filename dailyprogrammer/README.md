/r/DailyProgrammer solutions are written in Haskell (v8),
and are simply scripts without external dependences
that take input from `stdin` and output to `stdout`.

The solutions are accompanied by HUnit test scripts,
which have a singular dependency: HUnit.

If you've installed [Stack](https://docs.haskellstack.org)
you can execute the scripts directly
and all dependencies (including GHC itself) will be managed.
See the Script Interpreter heading [here](https://haskell-lang.org/tutorial/stack-script).

## Execution

### Locally

**Dependencies**

- [Stack](https://docs.haskellstack.org)

**Usage**

Simply CD to the directory and execute the `.hs` file you desire:

    cd easy/302
    ./Test.hs
    ./Main.hs

### Via Docker

**Dependencies**

- `brew install coreutils` (linked) on a Mac.

**Usage**

Note: Builds a `local/haskell-stack` image.

Use via the `via-docker` script (that's in this directory):

    ./via-docker easy/302/Main.hs

This will mount `easy/302` to `/app`,
and then execute `./Main.hs` from within `/app` - 
achieving a result somewhat similar to the local usage steps above.
