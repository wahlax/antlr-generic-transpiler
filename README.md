# Generic Transpiler using ANTLR

Download antlr-4.9.3-complete.jar before the following:

```
. ./antlr-env.shl
antlr4 -Dlanguage=Python3 -o gen Source.g4
python3 main.py examples/input.file examples/output.file
```
