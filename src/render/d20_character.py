from mako.template import Template
from constants import assets as assets_constants
from IPython.display import display, HTML

def print(character):
    # render html output
    html_out = to_html(character)

    display(HTML(html_out))

def to_html(character):
    # load template
    template_file = open(assets_constants.D20_CHAR_TEMPLATE, 'r')
    character_template = Template(template_file.read())
    template_file.close()

    # render html output
    return character_template.render(character=character)
