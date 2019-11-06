# mkdocs-sequence-js-plugin
[![Build Status](https://travis-ci.org/fcannizzaro/mkdocs-sequence-js-plugin.svg?branch=master)](https://travis-ci.org/fcannizzaro/mkdocs-sequence-js-plugin)

MkDocs plugin to render [js-sequence-diagrams](https://bramp.github.io/js-sequence-diagrams/) blocks

## Usage

```yaml
plugins:
  - sequence-js:
      theme: simple|hand      # diagram style
      popup: true             # enable "click to zoom" diagram
```

## Example 1

~~~
```sequence
Andrew->China: Says Hello
Note right of China: China thinks \n about it
China-->Andrew: How are you?
Andrew->>China: I am good thanks!
```
~~~

```sequence
Andrew->China: Says Hello
Note right of China: China thinks \n about it
China-->Andrew: How are you?
Andrew->>China: I am good thanks!
```

## Example 2

~~~
```sequence
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
```
~~~

```sequence
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
```

## Example 3

~~~
```sequence
# Example of a comment.
Note left of A: Note to the \n left of A
Note right of A: Note to the \n right of A
Note over A: Note over A
Note over A,B: Note over both A and B
```
~~~

```sequence
# Example of a comment.
Note left of A: Note to the \n left of A
Note right of A: Note to the \n right of A
Note over A: Note over A
Note over A,B: Note over both A and B
```

## Example 4

~~~
```sequence
participant C
participant B
participant A
Note right of A: By listing the participants \n you can change their order
```
~~~

```sequence
participant C
participant B
participant A
Note right of A: By listing the participants \n you can change their order
```

## Author
Francesco Saverio Cannizzaro (fcannizzaro)