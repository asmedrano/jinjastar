title:Using filters
template:base.html
content:
##Using Filters

`filters` are functions you can call from your templates at render time. For Example

	<!DOCTYPE html>
	<html>
		<head>
			<title></title>
			<meta charset="utf-8" />
			<link rel="stylesheet" href="css/normalize.css">
			<link rel="stylesheet" href="css/main.css">
		</head>
	<body>
		<header>
			<!-- this is the filter-->
			<h1>{{ "Hello World"|replace("Hello", "Goodbye") }}</h1>

			<!-- here is another one called 'list'. It can turn a comma delimted string into an iterable list-->
			
			{%for i in 'bob,stan,doug,danny,stacy'|list %}
				{{i}}
			{%endfor%}

		</header>
		<footer>
			blah blah blah
		</footer>
	</body>
	</html>

In this example the filter `replace` took the word on the leftside of the pipe and replaced "Hello" with "Goodbye". The result would be that "Goodbye World" would be rendered into our template. There a number of filters built into `jinja2` that you can use in your templates. Take a look [here](http://jinja.pocoo.org/docs/templates/#builtin-filters). Not all may be relevant to us right off.


## Jinjastar filters
`jinjastar` comes with some of its own filters. The first one I'd like to point out is `get_files_list`. Here is an example:

	<div class="nav">
		<ul>
		{% for l in '.' |get_files_list('.html') %}
			<li><a href="/{{l.link}}">{{l.title}}</a></li>
		{%endfor%}
		</ul>
	</div>

`get_files_list` takes the path to a directory and returns a list of files that you can iterate over. In the example above we are tell it to get files from `'.'`, which means the root of the content directory to `jinjastar`. We also tell it to get only `'.html'` files in those directories. That lets us create links for each content page we create. Here is what the bare output looks like:
	
	[{'lmt': '03-26-2013 ', 'link': 'content.html', 'name': 'content.html', 'title': 'Content Rendering '}, {'lmt': '03-26-2013 ', 'link': 'filters.html', 'name': 'filters.html', 'title': 'Using filters '}, {'lmt': '03-26-2013 ', 'link': 'index.html', 'name': 'index.html', 'title': 'Introduction '}]

`get_files_list` returns a list of dictionaries that contain meta data about each file. The fields are 
*`lmt` Last modified time
*`link` a link to the file from the root of the content directory
*`name` the name of the actual file.
* `title` The title field from the markdown page. 

`get_files_list` also takes a number of other parameters. Ex:

	get_files_list(file_ext='.js, .css', exclude='articles,archive', sort='name', reverse=False)

`file_ext` can be any comma delimted string of file extensions. The default is * which means all files.
`exclude` tells the get_files_list to stay out of these directories
`sort` tells get_files_list how to sort the files. Choices are `name` or `date`
`reverse` reverse the sort order. Ex: If you sort by date, you may want to use `reverse=True` so you would get the most recently created content first.
