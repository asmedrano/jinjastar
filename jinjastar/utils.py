import os, shutil

def collect_items(path_to_content,valid_file_ext=['.md']):
    """ Retrieve all the items in target from content directory
        exclude files with file extenisons listed in valid_file_ext
    """
    path = os.path.realpath(os.path.join(path_to_content))
    items = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filename, fileext = os.path.splitext(file)
            if fileext in valid_file_ext:
                realpath = root + '/' + file
                parent_dir = os.path.dirname(realpath.replace(path + "/",''))
                items.append({'file':file, 'realpath':realpath, 'cleaned_path':realpath.replace(path + "/",''), 'parentdir':parent_dir})

    return items


def copy_static_files(output_path, input_path):
    static_files = collect_items(input_path, valid_file_ext=['.css', '.js','.png', '.jpg','.gif'])
    for sf in static_files:
        mkdir_if_not_exist(os.path.join(output_path, sf['parentdir']))
        shutil.copy2(sf['realpath'], os.path.join(output_path, sf['parentdir']))

def mkdir_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)

