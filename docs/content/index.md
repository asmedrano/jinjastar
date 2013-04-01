title:Introduction
template:base.html
order:1
content:

# What is it?
`jinjastar` is a command line interface to [jinja2](http://jinja.pocoo.org/). It attempts to simplify the process if developing static websites by allowing you to use a templating language (in this case `jinja2`) in your project. There are 2 main features of `jinjastar`; "basic" rendering and "content" rendering.

## Using Basic Rendering
Say you have a project that looks like this:

	├── index.html
	├── about_us.html 
	├── css
	│   ├── grid.css 
	│   ├── main.css  
	│   └── normalize.css 
	├── js
	│   ├── main.js
	│   ├── plugins.js
	│   └── vendor
	│       ├── jquery-1.9.1.min.js
	│       └── modernizr-2.6.2.min.js 
	└── morepages
	├── subpage.html

Your `index.html` file might look like this


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
			{% block content %}
			<h1> This is our homepage </h1>
			{%endblock%}
		</header>
		<footer>
			blah blah blah
		</footer>
	</body>
	</html>


Now every other page you build for your site can simply `extend` this page. 
Lets say we add a page to our site called `about.html`

It would look like this


	{%extends "index.html"%}
	{% block content %}
		<h1> About us</h1>
		<p> Tra la lalalal </p>
	{%endblock%}


Because we have defined a `block` called `content`, we can easily replace the content of this page without having to worry about the rest of it.

## Rendering the output.
Now we can render our templates into html files. By default, `jinjastar` will copy over all your static files from the templates directory.

We call the utility like so.
`$ python jstar.py -t path/to/your/project -o /path/to/output/to`

The `-t` file is the path to the directory containing templates you want to render. The `-o` flag is the path to the directory you want the output to end up in.

This is essentially the core logic of `jinjastar`. Now lets look at using the ["content" rendering feature.](content.html)
