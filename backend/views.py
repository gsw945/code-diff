# -*- coding: utf-8 -*-
from .handler import BaseRequestHandler


class IndexView(BaseRequestHandler):
    """Index Page"""

    def get(self):
        output = self.render_jinja2('index.html')
        self.write(output)


class DiffView(BaseRequestHandler):
    """Diff Page"""

    def get(self):
        output = self.render_jinja2('diff.html')
        self.write(output)
