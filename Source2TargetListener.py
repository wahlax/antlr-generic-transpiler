import re
import sys
sys.path.insert(0, './gen')

from SourceListener import SourceListener
from SourceParser import SourceParser

class Source2TargetListener(SourceListener):

    def __init__(self, output):
        self.output = output

    def enterLine(self, ctx:SourceParser.LineContext):
        self.output.write("Start Line\n")

    def exitLine(self, ctx:SourceParser.LineContext):
        self.output.write("End Line\n")

    def enterStatement(self, ctx:SourceParser.StatementContext):
        self.output.write("Start Statement\n")

    def exitStatement(self, ctx:SourceParser.StatementContext):
        self.output.write("End Statement\n")

    def enterSome_statement(self, ctx:SourceParser.Some_statementContext):
        self.output.write("Some Statement - ")

        for v in ctx.VARIABLE():
            self.output.write("%s " % (v))

    def exitSome_statement(self, ctx:SourceParser.Some_statementContext):
        self.output.write("\n")
