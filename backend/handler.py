# -*- coding: utf-8 -*-
import tornado.web

from .template import TemplateRender


class BaseRequestHandler(tornado.web.RequestHandler, TemplateRender):
    '''
    RequestHandler Base
    example:
    def get(self):
        name = 'Tom'
        output = self.render_jinja2_string('hello {{ name }} ', name=name)
        self.write(output)
    '''

    def __init__(self, application, request, **kwargs):
        self.application = application
        self.request = request
        super(BaseRequestHandler, self).__init__(application, request, **kwargs)

    def initialize(self):
        super(BaseRequestHandler, self).initialize()

        self.render_kwargs = {
            'settings': self.settings,
            'STATIC_URL': self.settings.get('static_url_prefix', '/static/'),
            'request': self.request,
            'xsrf_token': self.xsrf_token,
            'xsrf_form_html': self.xsrf_form_html,
        }

    def render_jinja2(self, template_name, **kwargs):
        """
        jinja2 render_template
        """
        kwargs.update(self.render_kwargs)
        content = self.render_template(template_name, **kwargs)
        return content

    def render_jinja2_string(self, template_string, **kwargs):
        """
        jinja2 render_template_string
        """
        kwargs.update(self.render_kwargs)
        content = self.render_template_string(template_string, **kwargs)
        return content
