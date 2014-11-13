# OCR Box

Tesseract "in-a-box", with semi-automatic training.


## Usage

+ Put fonts (TTF only supported currently) into `/opt/ocr/fonts`
+ Run `bin/train` from the `/opt/ocr` directory
+ The new language file will be installed to `/opt/tessdata` and also left in `/opt/ocr`


## Training Steps

`bin/train` does the following:

+ Reads the list of fonts
+ Runs `text2image` on each to generate tif/box files
+ Trains Tesseract on each tif/box pair
+ Generates the unicharset file for all the boxes
+ Runs the actual training
