#!/usr/bin/env python

import argparse

class CLI(object):
    """
    Handles command-line interface options
    """

    def parse_arguments(self, args=None):
        """
        Implement command-line arguments
        """
        self.parser = argparse.ArgumentParser(usage='fetchproref [fetch]')
        self.sub = self.parser.add_subparsers()
        
        self.fetch = self.sub.add_parser('fetch',
            help='Save all tables from a pro ref site as individual CSVs in a folder at the current location.', usage='datadoc fetch [spreadsheetID] [outfile]'
        )

        self.fetch.add_argument('url',
            help='url of pro ref page'
        )

        return self.parser.parse_args(args)