# ocr_sample
Functions:
1. Choose two pixel coordinates by clicking on prompted image to define the top-left and bottom-right of a bounding box. Press 's' to start a new box.
2. Pytesseract will "read" the text within each bbox. It assumes it will be a single character.
3. The characters read will be concatenated to a word. This word is then used to replace all the placeholder,'0', found in a list of strings.
4. Each string is assigned a numeric score based on the characters it contains.
5. The (length of the string) compared to the (numeric score) is graphed. Quantiles of 0.05, 0.25, 0.45, 0.65, 0.85 are shown.

[Notebook](https://github.com/waysignal/ocr_sample/blob/main/OCR_Example.ipynb)
