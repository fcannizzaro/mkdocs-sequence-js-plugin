import os
import re
from collections import defaultdict

from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File
from mkdocs.utils import string_types

from .constant import XML, SEQUENCE_REGEX, JS, LIBS_PATH, CSS_PATH, JS_PATH
from .util import one_line, append_dependencies, append_script, make_script

FLAGS = re.MULTILINE | re.IGNORECASE | re.UNICODE


class SequenceJsPlugin(BasePlugin):
    config_scheme = (
        ('theme', Type(string_types, default='simple')),
        ('popup', Type(bool, default=True)),
    )

    def __init__(self):
        self.js = defaultdict(lambda: [])

    def on_page_markdown(self, markdown, page, **kwargs):

        output, end = [], 0
        theme = self.config['theme']
        popup_title = 'Click to zoom' if self.config['popup'] else ''

        for i, m in enumerate(re.finditer(SEQUENCE_REGEX, markdown, FLAGS)):

            output.append(markdown[end:m.start()])

            match, is_code, seq = m.groups()

            if '~' not in is_code:
                self.js[page.url].append(JS % (one_line(seq), i, theme))
                output.append(XML % (popup_title, i))
            else:
                output.append(match)

            end = m.end()

        # final substring
        output.append(markdown[end:])

        return ''.join(output)

    def on_post_page(self, html, page, **kwargs):
        if not self.js[page.url]:
            return html
        return append_dependencies(append_script(html, make_script(self.js[page.url])), self.config['popup'])

    def on_files(self, files, config):

        files.append(File('style.css', CSS_PATH, config['site_dir'] + '/css/', False))
        files.append(File('diagram.js', JS_PATH, config['site_dir'] + '/js/', False))

        for file in os.listdir(LIBS_PATH):
            files.append(File(file, LIBS_PATH, config['site_dir'] + '/js/', False))

        return files
