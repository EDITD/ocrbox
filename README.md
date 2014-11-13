# OCR Box

Tesseract training "in-a-box". Just upload some fonts and run it!


## Usage

+ Put fonts (TTF only supported currently) into `/opt/ocrbox/fonts`
+ Run `bin/train` from the `/opt/ocrbox` directory
+ The new language file will be installed to `/opt/tessdata` and also left in `/opt/ocrbox`
+ Use `bin/clean` to reset everything (recommended when changing the training set)


## Training Steps

`bin/train` does the following:

+ Reads the list of fonts
+ Runs `text2image` on each to generate tif/box files
+ Trains Tesseract on each tif/box pair
+ Generates the unicharset file for all the boxes
+ Runs the actual training


## Languages

The `bin/train` script defaults to `eng` as the langauge - you can change this by editing the variable at the top of the file.


## Font names

Most fonts seem to be in the format `FontFamilyName-VariantBits`, however some are not! We actually use a proper TTF library to extract the details, but the name cannot contain spaces. If you're using fonts which do, run `python files/fix_fonts.py` before training.
