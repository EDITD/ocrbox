# OCR Box
# File: files/fix_fonts.py
# Desc: fix files with spaces in their names (replace with -)

import os
import shutil


files = os.listdir('fonts/')

for file in files:
    if ' ' in file:
        new_file = file.replace(' ', '-')
        print 'Moving {0} -> {1}'.format(file, new_file)
        shutil.move(
            'fonts/{0}'.format(file),
            'fonts/{0}'.format(new_file)
        )

print 'Done!'
