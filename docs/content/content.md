title:Content Rlendering
template:base.html
content:

## What is content rendering?
Content rending is a feature that lets you render a directory of files written in [markdown syntax](http://daringfireball.net/projects/markdown/) against a directory of templates.

## Rendering
In order to render content, we need add the `-c`:
`jstar.py -c /path/to/content -t /path/to/templates -o /path/to/output`

`jinjastar` will then recursively render all markdown files in the specified directory.

### Sample Directory layout

	├── content
	│   ├── articles
	│   │   ├── article1.md
	│   │   └── article2.md
	│   ├── index.md
	│   └── subpages
	│       └── more.md
	├── templates
	│   ├── base.html
	│   ├── css
	│   │   ├── grid.css
	│   │   ├── main.css
	│   │   └── normalize.css
	│   ├── js
	│   │   ├── main.js
	│   │   ├── plugins.js
	│   │   └── vendor
	│   │       ├── jquery-1.9.1.min.js
	│   │       └── modernizr-2.6.2.min.js
	│   └── subtemplates
	│       ├── article.html

There are 2 important directories here. The first is the `content` directory and the other is the `templates` directory. They can live any where on the filesystem as long as we tell `jinjastar` where they are. In this example I've placed them in them same directory.


### Example Markdown file
Each Markdown file has a special format `jinjastar` needs to know how to render the file. Here is an example

	title:Home Page
	template:base.html
	content:
	# Hello World!
	This is a bunch of text that i have written
	this is more text writen in markdown

Each markdown file you produce must have the 3 fields: `title, template, and content`

The `title` field becomes usefull when you want to render a link to a page like the title of a blog post vs `article1.html` or something like that. If you look to the bottom of this page, you will see that the links generated below all have a custom title but have all been generated from markdown files like the example above.

The `template` field is what template from your templates directory you want to use to render this page. In the example, its `base.html`. If you wanted to use another template, say one located at `subtemplates/article.html` you simply use that instead of `base.html`. Keep in mind `article.html` can still `extend` from `base.html`. 

The `content` field where your markdown formated content goes.

#### Sidenote on content templates
Content templates follow the exact same pattern as any other template, the only real difference for now is that in order to have the content rendered into yourpage, you must have a `{% block content %}` block in you template.

### Nested Content
You can structure your content however you see fit. `jinjastar` will traverse the entire directory and render all markdown. If your content looks like this:

	├── content
	│   ├── articles
	│   │   ├── article1.md
	│   │   └── article2.md
	│   ├── index.md
	│   └── subpages
	│       └── more.md

Jinjastar will render the pages like this:

	├── articles
	│   ├── article1.html
	│   └── article2.html
	├── index.html
	└── subpages
	    └── more.html


## See a real example
You can see a real example of this system in action by looking at the `docs` directory in the [github repo](https://github.com/asmedrano/jinjastar).

Next we will look at how we can use `filters` to build dynamic nav based on our files. Read about filters [here](/filters.html).
