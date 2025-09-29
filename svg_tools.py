import re


PREFETCH_LENGTH = 200


def get_dimensions(content):
    width_match = re.match(r'<svg .*? width="(\d+\.?\d*)".*?>', content, re.ASCII|re.IGNORECASE)
    height_match = re.match(r'<svg .*? height="(\d+\.?\d*)".*?>', content, re.ASCII|re.IGNORECASE)
    assert width_match
    assert height_match
    width = int(float(width_match[1]))
    height = int(float(height_match[1]))
    assert width, width_match[1]
    assert height, height_match[1]
    return width, height