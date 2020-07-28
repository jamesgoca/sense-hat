import json
import jinja2

with open('gallery.html') as file:
    template = jinja2.Template(file.read())

with open("art.json", "r") as color_file:
	colors = json.load(color_file)

with open("index.html", "w+") as index_file:
	index_file.write(template.render(colors=colors))