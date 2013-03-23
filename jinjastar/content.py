import os
import re
from utils import *

def get_content_item_meta(path):
    """ The first N lines of a content file contain the meta data for this item. Return the metatdata for given item"""
    try:
        meta = {}
        with open(path, 'r') as f:
            lines = f.readlines()
            meta['title'] = lines[0].split(':')[1].strip() #TODO sometimes this may be blank need to catch the error
            meta['template'] =  lines[1].split(':')[1].strip()
    except IndexError:
        # TODO: User should get notified that this template didnt render
        pass

    return meta if meta != {} else None

def get_item_content(path):
    """ Get the content from item in path"""
    with open(path, 'r') as f:
        content = f.read()
    # we need to replace the first 2 lines
    return re.sub(r'title:.*\ntemplate.*\ncontent:', '', content)

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
            with open(fdir, 'w') as f:
                f.write(head_from_meta(meta))
                f.write(content_block(get_item_content(rp)))

def head_from_meta(meta):
    """ write a jinja2 extends block from the meta which looks like this {'template': 'base.html', 'title': 'Home Page'}"""

    out = '{{%extends "{0}"%}}'.format(meta['template'])
    out += '\n{{%block title%}}{0}{{%endblock%}}'.format(meta['title'])
    return out

def content_block(content):
    """ Create a jinja2 content block"""
    out = '''\n{{% block content %}}\n{{%filter markdown%}}\n{0}\n{{%endfilter%}}\n{{%endblock%}}'''.format(content)
    return out



