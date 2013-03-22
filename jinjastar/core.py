from jinja2 import Environment, FileSystemLoader
import os, shutil
import markdown
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
lfh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
lfh.setFormatter(formatter)
logger.addHandler(lfh)

def main(template_path, output_path='/tmp/rendered_templates'):
    loader = FileSystemLoader(template_path)
    env = Environment(loader=loader)
    env.filters['markdown'] = safe_markdown
    render_dir(env, template_path, output_path)

def render_dir(env, template_path, output_path):
    """ Iterate the template path and render all the files
        root is the current main dir what we are in
        dirs are a list os subdirectorys
        files are the actual files
    """
    #clean template path
    template_path = os.path.realpath(template_path)

    # First lets create a directory to output into
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, dirs, files in os.walk(template_path):
        for file in files:
            filename, fileext = os.path.splitext(file)
            sub = root.replace(template_path+"/", '')

            if sub != template_path:
                t_path = sub + "/" + file
                # make this subdirectory if it doesnt exists
                if not os.path.exists(os.path.join(output_path, sub)):
                    os.makedirs(os.path.join(output_path, sub))
            else:
                t_path = file

            if fileext in ['.html']:
                logger.info('Rendering %s' % t_path)
                t = env.get_template(t_path)
                output = t.render()
                write_file(os.path.join(output_path, t_path), output)
            elif fileext in ['.css','.js','.jpg','.gif','.png']:# TODO: what should i do with static files?
                shutil.copy2(os.path.join(template_path, t_path), os.path.join(output_path, t_path.replace(file,'')))

def write_file(target, content):
    f = open(target, 'w')
    f.write(content)
    f.close()

def safe_markdown(text):
    return jinja2.Markup(markdown.markdown(text))
