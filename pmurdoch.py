#!/usr/bin/env python

import web
from os import listdir
        
urls = (
    '/', 'index',
	'/euler', 'euler',
	'/([a-zA-Z0-9\-_]+)/?', 'page',
	'/code/([a-zA-Z0-9\.\-\/_]+)/?', 'code'
)
app = web.application(urls, globals())
templates = web.template.render("templates")

def get_page(name):
	f = open('pages/' + name + '.html')
	return f.read()
	
def get_error(code):
	f = open('error/' + code + '.html')
	return f.read()

def euler_sort(a, b):
	apos = a.find('.')
	bpos = b.find('.')
	av = a
	if apos != -1:
		av = a[:apos]
	bv = b
	if bpos != -1:
		bv = b[:bpos]

	return int(av) - int(bv)

class euler:
	def GET(self):
		dir = listdir('/home/pete/web/code/euler')
		#dir = listdir("C:\Users\Pete\projects\pmurdoch\code\euler")
		dir = sorted(dir, euler_sort)
		return templates.base(templates, templates.euler(templates, dir))

class code:
	def GET(self, name):
		try:
			f = open('code/' + name)
			p = f.read() #get exception before headers sent
			web.header('Content-Type', 'text/plain')
			return p
		except:
			return web.notfound()

class page:
	def GET(self, name):
		try:
			return templates.base(templates, get_page(name))
		except:
			raise web.notfound(templates.base(templates, get_error('404')))
	
class index:        
    def GET(self):
		return templates.base(templates, templates.index(templates))

if __name__ == "__main__":
    app.run()
