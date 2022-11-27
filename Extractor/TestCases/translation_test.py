#Input : translation of logic.py in .puml format

import pytest
import re
import sys

"""
Notes:
    <arbitrary formal PUML stuff> is shortened by <afPs>
    <afPs> accepts the empty string
"""

def pattern1(className: str):
    return 'class ' + className + '{[^{}]*}'

def pattern2(parent : str, child : str):
    return parent + " <-- " + child


def pattern3(className : str, Variables : list):
    """
    Formalize that the input string contains the following expressions as substrings:
    class Constant{\n <afPs> 'name' <afPs> \n <afPs> 'strRepn' <afPs>}
    """
    result = 'class ' + className + "{\n"
    for var in Variables:
        result += '[^{}]*' + var + '[^{}]*\n'
    result += '}'
    return result

def pattern4(className : str, memberVars_types : dict):
    result = 'class ' + className + "{\n"
    for var in memberVars_types:
        result += '[^{}]*' + var + ' : ' + memberVars_types[var] + '\n'
    result += '}'
    return result

def pattern5(className : str, class_memberVars : list):
    result = 'class ' + className + '{\n'
    for var in class_memberVars :
        result += "[^{}]*\+" + var + "[^{}]*" + '\n'
    result += '}'
    return result

def pattern6(className : str, ):
    pass

classNames = [
                'Expression', 'Formula', 'Term', 'Variable', 'Constant', 'Atom',
                'Not', 'And', 'Or', 'Implies',
                'Forall', 'Rule', 'UnaryRule', 'BinaryRule', 'ToCNFRule', 'ResolutionRule',
                'Derivation', 'KnowledgeBase']
def case1(translation : str):
    for className in classNames:
        assert id(type(re.search(pattern1(className), translation))) != id(None)

parent_children = {
    "Expression" : ["Formula", "Term"],
    "Term" :  ["Variable", "Constant"],
    "Formula" : ["Atom", "Not", "And", "Or", "Exists", "Forall"],
    "Rule" : ["UnaryRule", "BinaryRule"],
    "UnaryRule" : ["ToCNFRule"],
    "BinaryRule" : ["ResolutionRule"]
}
def case2(translation : str):
    for parent in parent_children:
        for child in parent_children[parent]:
            assert id(type(re.search(pattern2(parent, child), translation))) != id(None)

class_memberVars = {
    "Variable" : ["name", "strRepn"],
    "Constant" : ["name", "strRepn"],
    "Atom" : ["name", "args", "strRepn"],
    "Not" : ["arg", "strRepn"],
    "And" : ["arg1", "arg2", "strRepn"],
    "Or" : ["arg1", "arg2", "strRepn"],
    "Implies" : ["arg1", "arg2", "strRepn"],
    "Exists" : ["var", "body", "strRepn"],
    "Forall" : ["var", "body", "strRepn"],
    "ToCNFRule" : ["varCounts"],
    "Derivation" : ["form", "children", "cost", "permanent", "derived"],
    "KBResponse" : ["query", "modify", "status", "trueModel", "falseModel"],
    "KnowledgeBase" : ["standardizationRule", "rules", "modelChecking", "verbose", "derivations"]
}
def case4(translation : str):
    """
    Formalize that the input string contains the following expressions as substrings:
    class Constant{\n <afPs> 'name' <afPs> \n <afPs> 'strRepn' <afPs>}
    """
    for cl in class_memberVars:
        assert type(re.search(pattern3(cl, class_memberVars[cl]), translation)) != None

class_memberVars_types = {
    "Variable" : {"name" : "...",
                  "strRepn" : "None"
                  },
    "Constant" : {"name" : "...",
                  "strRepn" : "None"
                  },
    "Atom" : {"name" : "...",
              "args" : "list",
              "strRepn" : "None"
              },
    "Not" : {"arg" : "...",
             "strRepn" : "..."},
    "And" : {"arg1" : "...",
             "arg2" : "...",
             "strRepn" : "..."},
    "Or" : {"arg1" : "...",
             "arg2" : "...",
             "strRepn" : "..."},
    "Implies" : {"arg1" : "...",
             "arg2" : "...",
             "strRepn" : "..."},
    "Exists" : {"var" : "...",
                "body" : "...",
                "strRepn" : "None"},
    "Forall" : {"var" : "...",
                "body" : "...",
                "strRepn" : "None"},
    "ToCNFRule" : {"varCounts" : "collections.Counter"},
    "Derivation" : {"form" : "...",
                    "children" : "...",
                    "cost" : "...",
                    "permanent" : "bool",
                    "derived" : "..."},
    "KBResponse" : {"query" : "...",
                    "modify" : "...",
                    "status" : "...",
                    "trueModel" : "...",
                    "falseModel" : "..."},
    "KnowledgeBase" : {"standardizationRule" : "...",
                       "rules" : "...",
                       "modelChecking" : "...",
                       "verbose" : "...",
                       "derivations" : "..."}
}
def case5(translation : str):
    for cl in class_memberVars_types:
        assert id(type(re.search(pattern4(cl, class_memberVars_types[cl]), translation))) != id(None)
    """
    Formalize that the input string contains the following expressions as substrings:
    class Constant{\n <afPs> 'name : ...' \n <afPs> 'strRepn : None' <afPs>}

    """
def case6(translation : str):
    for cl in class_memberVars:
        assert id(type(re.search(pattern5(cl, class_memberVars[cl]), translation))) != id(None)
    """
    Formalize that the input string contains the following expressions as substrings:

    class Constant{\n <afPs> '+name' <afPs> \n <afPs> '+strRepn' <afPs>}

    """

def case7():
    #sTaRT
    """
    Formalize that the input string contains the following expressions as substrings:

    class Constant{\n <afPs> Constant(<afPs>) \n <afPs> computeStrRepn(<afPs>) <afPs>}

    """
def case8():
    """
    Formalize that the input string contains the following expressions as substrings:

    class Constant{\n <afPs> Constant(self, name <Function parameter type>?) \n <afPs> computeStrRepn(self) <afPs>}

    """
def case9():
    """
    Formalize that the input string contains the following expressions as substrings:

    class Constant{\n <afPs> Constant(self, name : ...) \n <afPs> computeStrRepn(self) <afPs>}

    """
def case10():
    """
    Formalize that the input string contains the following expressions as substrings:

    class Constant{\n <afPs> Constant(<Method parameters>) \n <afPs> computeStrRepn(<Method parameters>) : ... <afPs>}

    """
def case11():
    """
    Formalize that the input string contains the following expressions as substrings:

    class Constant{\n <afPs> Constant(<Method parameters>) \n <afPs> +computeStrRepn(<Method parameters>) : ... <afPs>}

    """
def case12():
    """
    class Expression{<afPs>}\n <afPs> interface Constant | abstract Constant
    :return:
    """
print(__name__)
if __name__ == '__main__':
    Tests = [case1, case2, case4, case5, case6]
    if len(sys.argv) > 1:
        pumlFile = open(sys.argv[1],"r")
        input = pumlFile.read()
        for test in Tests:
            test(input)
    else:
        pumlFile = open("/home/solteszistvan/PycharmProjects/Parsers/Python/Extractor/TestCases/test.puml","r")
        input = pumlFile.read()
        for test in Tests:
            test(input)