from jinja2 import Environment, FileSystemLoader
import os


def main(template_path, output_path='/tmp/rendered_templates'):
    loader = FileSystemLoader(template_path)
    env = Environment(loader=loader)
    render_dir(env, template_path, output_path)


def render_dir(env, template_path, output_path):
    """ Iterate the template path and render all the files
        root is the current main dir what we are in
        dirs are a list os subdirectorys
        files are the actual files
    """
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

            if fileext in ['.html', '.js', '.css']:
                t = env.get_template(t_path)
                output = t.render()
                write_file(os.path.join(output_path, t_path), output)

def write_file(target, content):
    f = open(target, 'w')
    f.write(content)
    f.close()
