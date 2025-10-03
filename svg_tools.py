import re


PREFETCH_LENGTH = 200
COLOR_REGEXP = r'"#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})"'
PATH_REGEXP = r'<(path .*?)/>'
FLAGS = re.ASCII|re.IGNORECASE

def _expand(color):
    assert len(color) == 3, color
    return color[0] + color[0] + color[1] + color[1] + color[2] + color[2]

def _contract(color):
    assert len(color) == 6, color
    assert color[0] == color[1] and color[2] == color[3] and color[4] == color[5], color
    return color[0] + color[2] + color[4]

def try_contract(color):
    assert len(color) == 6, color
    if color[0] == color[1] and color[2] == color[3] and color[4] == color[5]:
        return _contract(color)
    else:
        return color

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
        short = try_contract(color)
        long = color
    # Build
    if short != long:
        return f'"#{short}"|"#{long}"'
    else:
        return f'"#{long}"'
    
def prepare_color_map(color_map):
    normalized = {}
    for k, v in color_map.items():
        new_key = normalize(k)
        assert new_key not in normalized, new_key
        normalized[new_key] = try_contract(normalize(v))
    return normalized

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

def contains_image(content):
    return "<image " in content

def replace(content, color_map, default_actions):
    output = []
    pieces = re.split(COLOR_REGEXP, content, flags=FLAGS)
    for p in pieces:
        result = None
        if (len(p) == 3 or len(p) == 6) and p.isalnum():    # seems to be a color
            normalized = normalize(p)
            result = color_map.get(normalized)
            if not result and default_actions:
                for a in default_actions:
                    normalized = a(normalized)
                result = try_contract(normalized)
            if not result:
                result = p
            result = f'"#{result}"'
        else:
            result = p
        output.append(result)
    result = "".join(output)
    new_default = color_map.get("000000")
    if new_default:
        output = []
        pieces = re.split(PATH_REGEXP, result, flags=FLAGS)
        for p in pieces:
            if p.startswith("path"):
                if "fill=" not in p:
                    p += f' fill="#{new_default}"'
                output.append(f"<{p}/>")
            else:
                output.append(p)
        result = "".join(output)
    return result