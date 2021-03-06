#!/usr/bin/env python

import argparse, logging
from jinjastar.core import render, render_content

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
lfh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
lfh.setFormatter(formatter)
logger.addHandler(lfh)

description = """

Sample Usage:

Render a directory of templates using jinja

jstar.py -t jinjastar/tests/templates -o /tmp/jstar_out

Render a directory of .md files against a folder of templates
jstar.py -c jinjastar/tests/content -t jinjastar/tests/templates -o /tmp/jstar_out

"""

parser = argparse.ArgumentParser(description=description)
parser.add_argument('-c', action='store', dest='content_dir', type=str, help='Path to the content directory', default=None)
parser.add_argument('-t', action="store", dest="template_dir", type=str,  help='Path to the template directory', required=True)
parser.add_argument('-o', action="store", dest="out_dir", type=str,  help='Path to output directory', default='/tmp/rendered_templates')
parser.add_argument('-f', action="store", dest="filter", type=str,  help='Path to filter.py', default=None)


def run():
    args = parser.parse_args()
    if args.content_dir is None:
    # simplest case only -t flag
    # This means, render this directory of templates, to the -o directory
        render(template_path=args.template_dir,
               render_input_path=args.template_dir,
               output_path=args.out_dir, filters=args.filter)
    else:
        render_content(path_to_content=args.content_dir,
                       template_path=args.template_dir,
                       output_path=args.out_dir,
                       filters=args.filter)

if __name__ == '__main__':
    run()
