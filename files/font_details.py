# OCR Box
# File: bin/get_font_properties.py
# Desc: helpers convert font files -> reasonable guess for font_properties
#       currently only works for TTF fonts

import sys

from fontTools import ttLib
 

FONT_SPECIFIER_NAME_ID = 4
FONT_SPECIFIER_FAMILY_ID = 1

def get_font_details(font_filename):
    font = ttLib.TTFont(font_filename)
    name = ''
    family = ''
    for record in font['name'].names:
        if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
            if '\000' in record.string:
                name = unicode(record.string, 'utf-16-be').encode('utf-8')
            else:
                name = record.string
        elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
            if '\000' in record.string:
                family = unicode(record.string, 'utf-16-be').encode('utf-8')
            else:
                family = record.string
        if name and family:
            break

    return name, family

filename = sys.argv[1]
font_filename = 'fonts/{0}.ttf'.format(filename)
name, family = get_font_details(font_filename)

# Name only?
if sys.argv[2] == 'name':
    print name

# Properties file output
elif sys.argv[2] == 'properties':
    is_italic = 1 if 'Bold' in name else 0
    is_bold = 1 if 'Italic' in name else 0

    print 'eng.{0}.box {1} {2} 0 0 0'.format(filename, is_italic, is_bold)
