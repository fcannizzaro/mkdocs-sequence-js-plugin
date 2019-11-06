# mkdocs-sequence-js-plugin
[![Build Status](https://travis-ci.org/fcannizzaro/mkdocs-sequence-js-plugin.svg?branch=master)](https://travis-ci.org/fcannizzaro/mkdocs-sequence-js-plugin)

MkDocs plugin to render [js-sequence-diagrams](https://bramp.github.io/js-sequence-diagrams/) blocks

## Block

~~~
```sequence
Andrew->China: Says Hello
Note right of China: China thinks \n about it
China-->Andrew: How are you?
Andrew->>China: I am good thanks!
```
~~~

## Usage

```yaml
plugins:
  - sequence-js:
      theme: simple|hand      # diagram style
      popup: true             # enable "click to zoom" diagram
```

## Author
Francesco Saverio Cannizzaro ([**fcannizzaro**](https://github.com/fcannizzaro/))
