import os

DEPENDENCIES = """
	<script src='{0}/js/webfont.js'></script>
	<script src='{0}/js/snap.svg-min.js'></script>
	<script src='{0}/js/underscore-min.js'></script>
	<script src='{0}/js/sequence-diagram-min.js'></script>
	<link rel="stylesheet" type="text/css" href="{0}/css/style.css"> 
"""

POPUP_SCRIPT = "<script src='/js/diagram.js'></script>"

SEQUENCE_REGEX = r"((~*\n?)```sequence\n([^`]+)\n```)"

XML = '<div title="%s" class="scrollable-diagram" id="diagram#%d"></div>'

JS = "Diagram.parse(%s).drawSVG(\"diagram#%d\", {theme: '%s'})"

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

LIBS_PATH = BASE_PATH + '/libs/'

CSS_PATH = BASE_PATH + '/css/'

JS_PATH = BASE_PATH + '/js/'
