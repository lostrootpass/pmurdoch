#!/usr/bin/env python

import web
from os import listdir
from collections import namedtuple
import gettext
		
web.config.debug = True

urls = (
	'/', 'index',
	'/about', 'about',
	'/([a-zA-Z0-9\-_]+)/?', 'page',
	'/code/([a-zA-Z0-9\.\-\/_]+)/?', 'code'
)

languages = {
	'en': gettext.translation('messages', 'i18n/', languages=['en_GB'], fallback=True),
	'ja': gettext.translation('messages', 'i18n/', languages=['ja_JP'], fallback=True),
	'fr': gettext.translation('messages', 'i18n/', languages=['fr_FR'], fallback=True)
}

languages['en'].install(True)

app = web.application(urls, globals())

#Needed to work around the debug reloader trashing the session object
if web.config.get('_session') is None:
	session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'lang': 'en'})
	web.config._session = session
else:
	session = web.config._session

def translate_hook():
	va = web.input()
	if 'lang' in va.keys() and va['lang'] in languages:
		session.lang = va['lang']

def custom_gettext(req):
	return languages[session.lang].gettext(req)

webpyglobals = {'namedtuple': namedtuple, '_': custom_gettext, 'getattr': getattr, 'hasattr': hasattr}
templates = web.template.render("templates/", globals=webpyglobals)
app.add_processor(web.loadhook(translate_hook))

def get_error(code):
	with open('error/' + code + '.html', 'r', encoding='utf-8') as f:
		return f.read()

class about:
	def GET(self):
		web.header('Content-Type','text/html; charset=utf-8', unique=True) 
		return templates.base(templates, templates.about(templates), web.ctx)

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
			return templates.base(templates, templates.page(templates, name), web.ctx)
		except:
			raise web.notfound(templates.base(templates, get_error('404')))

class index:        
	def GET(self):
		web.header('Content-Type','text/html; charset=utf-8', unique=True) 
		return templates.base(templates, templates.index(templates), web.ctx)

if __name__ == "__main__":
	app.run()
