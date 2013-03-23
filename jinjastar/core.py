from jinja2 import Environment, FileSystemLoader, Markup
import os, shutil
import markdown
import logging
from utils import *
from content import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
lfh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
lfh.setFormatter(formatter)
logger.addHandler(lfh)


def render(template_path, render_input_path, output_path='/tmp/rendered_templates'):
    """ template path: is the path for jijna to load templates from
        render_input_path: the path to the templates to be rendered, this could be the same path as templates
        output_path: the path to render the output to
    """
    # clean up template paths a bit
    template_path = os.path.realpath(template_path)
    render_input_path = os.path.realpath(render_input_path)

    template_dirs = []
    template_dirs.append(template_path)

    if template_path != render_input_path:
        template_dirs.append(render_input_path)

    loader = FileSystemLoader(template_dirs)
    env = Environment(loader=loader)
    env.filters['markdown'] = safe_markdown


    basic_render(env, template_path, render_input_path, output_path)


def basic_render(env, template_path, render_input_path, output_path):

    # collect renderable files from the input_path
    tmpl_files = collect_items(render_input_path, valid_file_ext=['.html'])

    # create the output dir
    mkdir_if_not_exist(output_path)

    # render the templates
    for t in tmpl_files:
        output_target_dir = os.path.join(output_path, t['parentdir'])
        # create a dir for the templates in output path if it dont exist
        mkdir_if_not_exist(output_target_dir)

        # render the template
        logger.info('Rendering %s' % t['realpath'])
        template = env.get_template(t['cleaned_path'])
        output = template.render()
        write_to_file(os.path.join(output_target_dir, t['file']), output)

    # copy static files over
    copy_static_files(output_path, template_path)

def render_content(path_to_content, template_path, output_path='/tmp/render_content'):
    """ This render takes a content directory, generates templates out of it then renders it"""
    #generate the templates from content
    generate_items(path_to_content)
    # this should generate templates to /tmp/jstar_temp
    render(template_path, os.path.realpath('/tmp/jstar_temp'), output_path)


def write_to_file(target, content):
    f = open(target, 'w')
    f.write(content)
    f.close()

def safe_markdown(text):
    return Markup(markdown.markdown(text))
