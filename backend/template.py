# -*- coding: utf-8 -*-
'''
# refer:
#  * https://python-guide-kr.readthedocs.io/ko/latest/scenarios/web.html#jinja2
#  * https://bibhasdn.com/blog/using-jinja2-as-the-template-engine-for-tornado-web-framework/
'''
from jinja2 import Environment, FileSystemLoader, TemplateNotFound


class TemplateRender(object):
    """
    模板渲染类.
    """

    def __init__(self):
        template_dirs = []
        template_path = self.settings.get('template_path', None)
        if bool(template_path):
            template_dirs.append(template_path)

        self.jinja2_env = Environment(loader=FileSystemLoader(template_dirs))

    def render_template(self, template_name, **kwargs):
        try:
            template = self.jinja2_env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        content = template.render(**kwargs)
        return content

    def render_template_string(self, template_string, **kwargs):
        template = self.jinja2_env.from_string(template_string)
        content = template.render(**kwargs)
        return content
