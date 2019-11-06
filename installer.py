import os
from setuptools.command.install import install
import urllib.request

def download(url: str, file: str):
  print(url, file)
  response = urllib.request.urlopen(url)
  data = response.read()
  print(f' >> downloading {file}')
  with open(file, 'wb') as f:
    f.write(data)


class InstallWrapper(install):

    def run(self):

        libs_path = os.path.dirname(os.path.realpath(__file__)) + '/mkdocs_sequence_js_plugin/libs/'

        if not os.path.exists(libs_path):
            os.makedirs(libs_path)
            os.chmod(libs_path, 0o777) 

        for file in ['webfont.js', 'snap.svg-min.js', 'underscore-min.js', 'sequence-diagram-min.js']:
          download('https://bramp.github.io/js-sequence-diagrams/js/' + file, f'{libs_path}{file}')
          if os.name != 'nt':
            os.chmod(libs_path + file, 0o777)

        install.run(self)
