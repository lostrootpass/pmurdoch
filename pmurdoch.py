#!/usr/bin/env python

import web
from os import listdir
from collections import namedtuple
import gettext
		
web.config.debug = True

urls = (
	'/', 'index',
	'/about', 'about',
	'/euler', 'euler',
	'/([a-zA-Z0-9\-_]+)/?', 'page',
	'/code/([a-zA-Z0-9\.\-\/_]+)/?', 'code'
)

gettext.translation('messages', 'i18n/', languages=['en_GB'], fallback=True).install(True)

app = web.application(urls, globals())
webpyglobals = {'namedtuple': namedtuple, '_': _, 'getattr': getattr}
templates = web.template.render("templates/", globals=webpyglobals)
	
def get_error(code):
	with open('error/' + code + '.html', 'r', encoding='utf-8') as f:
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

class about:
	def GET(self):
		web.header('Content-Type','text/html; charset=utf-8', unique=True) 
		return templates.base(templates, templates.about(templates))

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
		web.header('Content-Type','text/html; charset=utf-8', unique=True) 
		try:
			return templates.base(templates, templates.page(templates, name))
		except:
			raise web.notfound(templates.base(templates, get_error('404')))

class index:        
	def GET(self):
		web.header('Content-Type','text/html; charset=utf-8', unique=True) 
		return templates.base(templates, templates.index(templates))

if __name__ == "__main__":
	app.run()
