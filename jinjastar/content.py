import os
import re
from utils import *
from jinja2 import evalcontextfilter
import codecs

def get_content_item_meta(path):
    """ The first N lines of a content file contain the meta data for this item. Return the metatdata for given item"""
    try:
        meta = {}
        with open(path, 'r') as f:
            lines = f.readlines()
            meta['title'] = lines[0].split(':')[1].strip() #TODO sometimes this may be blank need to catch the error
            meta['template'] =  lines[1].split(':')[1].strip()
            if 'order' in lines[2]:
                val = lines[2].split(':')[1].strip()
                meta['order'] = val if val != '' else 0

    except IndexError:
        # TODO: User should get notified that this template didnt render
        pass

    return meta if meta != {} else None

def get_item_content(path):
    """ Get the content from item in path"""
    with codecs.open(path, mode='r', encoding='utf-8') as f:
        content = f.read()
    # we need to replace the first 2 lines
    return re.sub(r'title:.*\ntemplate.*(\norder.*)?\ncontent:', u'', content)

def generate_items(path_to_content):
    """generate jinja templates from the content pages
        these always get generated to /tmp/jstar_temp
    """
    output_path = '/tmp/jstar_temp'
    # create the outut path if it doesnt exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    items = collect_items(path_to_content)
    for item in items:
        rp = item['realpath']
        fn = item['file'].replace('.md','.html')
        fdir = output_path + "/" +item['cleaned_path'].replace('.md','.html')
        meta = get_content_item_meta(rp)
        # make a directory for this file if needed
        if not os.path.exists(os.path.dirname(fdir)):
            os.makedirs(os.path.dirname(fdir))
        if meta is not None:
            with codecs.open(fdir, mode='w', encoding='utf-8') as f:
                # write last modified time
                f.write(u'{{# LMT:{0} #}}'.format(get_last_modified_time(item['realpath'])))
                f.write(head_from_meta(meta))
                f.write(content_block(get_item_content(rp)))

def head_from_meta(meta):
    """ write a jinja2 extends block from the meta which looks like this {'template': 'base.html', 'title': 'Home Page'}"""
    out = '{{# TITLE:{0} #}}'.format(meta['title']) # we write the title or any other meta data into the head so we can acess it later
    if 'order' in meta:
        out += '{{# ORDER:{0} #}}'.format(meta['order'])
    out += '\n{{%extends "{0}"%}}'.format(meta['template'])
    out += '\n{{%block title%}}{0}{{%endblock%}}'.format(meta['title'])
    return out

def content_block(content):
    """ Create a jinja2 content block"""
    out = u'''\n{{% block content %}}\n{{%filter markdown%}}{{%raw%}}\n{0}\n{{%endraw%}}{{%endfilter%}}\n{{%endblock%}}'''.format(content)
    return out


def get_value_from_file(file, key):
    regex = re.compile("%s:[a-zA-Z0-9\s\,\!\?\*\%%\-\.]+" % key)
    value = None
    with open (file, 'r') as f:
        line = f.readlines()[0]
        m = regex.findall(line)
        if m:
            value = m[0].split(":")[1]
    return value


# custom jinja2 filters
@evalcontextfilter
def get_files_list(context, target_dir='.', file_ext='*', exclude='', sort='name', reverse=False):
    """ Returns an iterable of files.
        target_dir is relative to the render_input_path
        valid sort options = name, order, date
    """
    target_dir = target_dir.strip('/')
    path = os.path.join(context.environment.globals['render_input_path'], target_dir)

    exclude_dirs = exclude.split(',')

    if file_ext == '*':
        valid_file_ext = ['.html','.htm','.css','.js','.png','.jpg','.gif']
    else:
        valid_file_ext = file_ext.split(',')

    files = collect_items(path, valid_file_ext, exclude_dirs)

    if target_dir != '.':
        file_list =  [{ 'link':target_dir + '/' + f['cleaned_path'], 'name':f['file'],
                 'title':get_value_from_file(f['realpath'], 'TITLE'),
                 'lmt':get_value_from_file(f['realpath'], 'LMT'),
                 'order':get_value_from_file(f['realpath'],'ORDER') or len(files) + 1} for f in files]
    else:
        file_list = [{'link':f['cleaned_path'], 'name':f['file'],
                 'title':get_value_from_file(f['realpath'], 'TITLE'),
                 'lmt':get_value_from_file(f['realpath'], 'LMT'),
                 'order':get_value_from_file(f['realpath'],'ORDER') or len(files) + 1} for f in files]

    if sort == 'name':
        sorted_file_list = sorted(file_list, key=lambda k: k['name'], reverse=reverse)
    elif sort =='date':
        sorted_file_list = sorted(file_list, key=lambda k: k['lmt'], reverse=reverse)
    elif sort =='order':
        sorted_file_list = sorted(file_list, key=lambda k: k['order'], reverse=reverse)
    else:
        sorted_file_list = files


    return sorted_file_list
