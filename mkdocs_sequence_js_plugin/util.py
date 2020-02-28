from typing import List

from .constant import DEPENDENCIES, POPUP_SCRIPT


def one_line(source: str) -> str:
    return '`' + repr(source)[1:-1] + '`'


def make_script(lines: List[str]) -> str:
    return "<script>" + '\n'.join(lines) + "</script>"


def append_script(html: str, script: str) -> str:
    return html.replace('</body>', f'{script}</body>')


def append_dependencies(html: str, popup: bool, site_url: str) -> str:
    use_popup = '\n' + site_url + POPUP_SCRIPT if popup else ''
    return html.replace('</head>', f'{DEPENDENCIES.format(site_url)}{use_popup}</head>')