from setuptools import setup, find_packages
from installer import InstallWrapper

setup(
    name='mkdocs-sequence-js-plugin',
    version='1.0.0',
    description='plugin to render sequence.js blocks',
    keywords='mkdocs python markdown sequence.js',
    url='https://github.com/fcannizzaro/mkdocs-sequence-js-plugin',
    author='Francesco Saverio Cannizzaro',
    author_email='francescosaverio.cannizzaro@gmail.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=['mkdocs>=1'],
    include_package_data=True,
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    entry_points={
        'mkdocs.plugins': [
            'sequence-js = mkdocs_sequence_js_plugin.plugin:SequenceJsPlugin'
        ]
    },
    cmdclass={'install': InstallWrapper}
)
