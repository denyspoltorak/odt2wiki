import re


PREFETCH_LENGTH = 200
COLOR_REGEXP = r'"#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})"'
FLAGS = re.ASCII|re.IGNORECASE

def _expand(color):
    assert len(color) == 3, color
    return color[0] + color[0] + color[1] + color[1] + color[2] + color[2]

def _contract(color):
    assert len(color) == 6, color
    assert color[0] == color[1] and color[2] == color[3] and color[4] == color[5], color
    return color[0] + color[2] + color[4]

def _try_contract(color):
    assert len(color) == 6, color
    if color[0] == color[1] and color[2] == color[3] and color[4] == color[5]:
        return _contract(color)
    else:
        return None

def normalize(color):
    color = color.lower()
    if len(color) == 3: # duplicate all the letters
        color = _expand(color)
    else:
        assert len(color) == 6
    return color

def make_regexp(color):
    # Denormalize
    if len(color) == 3:
        short = color
        long = _expand(color)
    else:
        assert len(color) == 6
        short = _try_contract(color)
        long = color
    # Build
    if short:
        return f'"#{short}"|"#{long}"'
    else:
        return f'"#{long}"'

def get_dimensions(content):
    width_match = re.match(r'<svg .*? width="(\d+\.?\d*)".*?>', content, FLAGS)
    height_match = re.match(r'<svg .*? height="(\d+\.?\d*)".*?>', content, FLAGS)
    assert width_match
    assert height_match
    width = int(float(width_match[1]))
    height = int(float(height_match[1]))
    assert width, width_match[1]
    assert height, height_match[1]
    return width, height

def list_colors(content):
    matches = re.findall(COLOR_REGEXP, content, FLAGS)
    assert matches
    return set([normalize(c) for c in matches])

def contains_regexp(content, regexp):
    return re.search(regexp, content, FLAGS)