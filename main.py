import sys
sys.path.insert(0, './gen')

# Generated from Source.g4 file
from SourceLexer import SourceLexer
from SourceParser import SourceParser

from Source2TargetListener import Source2TargetListener
from antlr4 import *

def main(argv):

    # Validate 2 parameters with path to input and output
    if len(argv) != 3:
        print("ERROR - 2 parameters expected: path/to/input path/to/output")
        sys.exit(1)

    # Prepare lexer and parser
    lexer = SourceLexer(FileStream(argv[1]))
    parser = SourceParser(CommonTokenStream(lexer))
    
    # extract source from parser
    source = parser.program()

    # Translate source to target
    with open(argv[2],"w") as target:
        listener = Source2TargetListener(target)
        walker = ParseTreeWalker()
        walker.walk(listener, source)

    target.close()      

if __name__ == '__main__':
    main(sys.argv)
