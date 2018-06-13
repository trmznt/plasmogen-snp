
import sys, os
import argparse

from genaf_snp.scripts.run import main as genaf_main, set_config
from rhombus.lib.utils import cout, cerr, cexit

from plasmogen_snp.models.handler import DBHandler
from plasmogen_snp.lib.query import set_query_class


def greet():
    cerr('plasmogen-snp-run - command line utility for plasmogen/genaf/rhombus')


def usage():
    cerr('plasmogen-snp-run - command line utility for plasmogen/genaf/rhombus')
    cerr('usage:')
    cerr('\t%s scriptname [options]' % sys.argv[0])
    sys.exit(0)


set_config( environ='PLASMOGEN_SNP_CONFIG',
            paths = ['plasmogen_snp.scripts.'],
            greet = greet,
            usage = usage,
            dbhandler_class = DBHandler
)

set_query_class()

def main():
    genaf_main()



