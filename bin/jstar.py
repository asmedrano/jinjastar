#!/usr/bin/env python

import argparse, logging
from jinjastar.core import main

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
lfh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
lfh.setFormatter(formatter)
logger.addHandler(lfh)

parser = argparse.ArgumentParser(description='Render a directory of templates using jinja')
parser.add_argument('-d', action="store", dest="cwd_dir", type=str,  help='Path to the project directory', required=True)
parser.add_argument('-t', action="store", dest="template_dir", type=str,  help='Path to the template directory', required=True)
parser.add_argument('-o', action="store", dest="out_dir", type=str,  help='Path to output directory', default='/tmp/rendered_templates')


def run():
    args = parser.parse_args()

    logger.info('Rendering templates in: %s to %s' % (args.cwd_dir, args.out_dir))
    main(args.template_dir, args.cwd_dir, args.out_dir)

if __name__ == '__main__':
    run()
