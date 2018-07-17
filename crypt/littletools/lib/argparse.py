#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

def Argparse():
    # ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[],
    #     formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None,
    #         argument_default=None, conflict_handler='error', add_help=True)
    parser = argparse.ArgumentParser(usage="%(prog)s [options]",add_help=False,
    # add_argument (name or flags...[, action][, nargs][, const][, default][, type]
    #       [, choices][, required][, help][, metavar][, dest])
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=('''
        Please do not mess up this text!
        --------------------------------
            I have indented it
            exactly the way
            I want it'''))
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-h', '--help', action="store_true", help=u'%(prog)s的帮助')
    optional.add_argument('--version', action='version', version='%(prog)s 1.0')
#     example = parser.add_argument_group('example', 'example description')
#     parser.add_argument(
#         '-f', '--foo',
#         nargs='*',
#         metavar='filename',
#         required=True,
#         default="hahaha",
#         dest='foodest',
#         type=str,
#         help='foo of the %(prog)s program'
#         )
#
#     optional.add_argument('--file', type=argparse.FileType('w'))
#     optional.add_argument('--choices', type=int, choices=range(1, 4))
    optional = parser.add_argument_group('optional arguments')

    args=parser.parse_args()
    args = vars(args)
    if args['help']:
        parser.print_help()
    return args