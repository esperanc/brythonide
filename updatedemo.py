#!/usr/bin/env python3

import glob

page = open("examples.html","w")
print ("""
<h1>Example programs</h1>
<ol>
""", file=page)
for name in glob.glob("demoSketches/*.py"):
	print (f"""
		<li> <a href="./index.html?program={name}">{name.split("/")[1]}</a>""", file=page)
print ("""
</ol>
""", file=page)
page.close()