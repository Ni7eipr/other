#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys

def argparseclass():

    parser = argparse.ArgumentParser(usage="%(prog)s [options]",add_help=False,

    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=(u'''
        作者：End1ng
        --------------------------------'''))
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-h', '--help', action="store_true", help='help of the %(prog)s program')
    optional.add_argument('--version', action='version', version='%(prog)s 1.1')

    args = parser.add_argument_group('Necessary parameter')

    args.add_argument('-n','--name',metavar=u'李华',help=u'姓名')
    args.add_argument('-b','--birth',metavar=u'0000.00.00',help=u'生日')
    # args.add_argument('-n','--name',help=u'姓名')

    args=parser.parse_args()
    args = vars(args)

    if len(sys.argv) == 1 or args['help']:
        parser.print_help()
        sys.exit()

    return args