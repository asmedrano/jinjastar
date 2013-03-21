## Why?
I started working on my own personal website and thought I'd go the static file route. There are other more feature rich static file doodads out there but I rolled my own.

## What is it?
A wrapper around Jinja2 that'll lets you render jinja templates to Static html files

## Sample Usage
``` jstar.py -d ~/path/to/my_files -o /path/for/output ```

## Example
Say you have a project that looks like this
```
├── index.html
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
```

```index.html``` could contain this
```
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
```

The ```block``` part is the important bit.

```subpage.html``` could then extend ```index.html``` like this
```
{%extends "base.html"%}
{% block content %}
    <h1> This is a subpage</h1>
{%endblock%}
```

We would then run ```jstar.py -d ~/path/to/your_project -o /path/to/somedir``` and we'd end up with a mirror of our project
except that the templates have now been rendered and the files now look like this.

index.html

```
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

      <h1> This is our homepage </h1>
    
    </header>
    <footer>
        blah blah blah
    </footer>
</body>
</html>
```

subpage.html
```
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

      <h1> This is a subpage</h1>
    
    </header>
    <footer>
        blah blah blah
    </footer>
</body>
</html>
```

## Learn more about jijna templates here http://jinja.pocoo.org/docs/templates/

##TODO
* Add ability to include data as json and other formats and render in templates.
* Compressor/Minify ?
* Ignore files list
