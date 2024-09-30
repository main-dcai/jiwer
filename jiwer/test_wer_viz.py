from jiwer.process import process_words
from jiwer.alignment import visualize_alignment

# import matplotlib
# import os.path
# from matplotlib.afm import AFM
# from fontTools.ttLib import TTFont


# def get_string_width(font, text):
#     glyph_set = font.getGlyphSet()
#     width = 0
#     for char in text:
#         glyph = glyph_set[font.getBestCmap()[ord(char)]]
#         width += glyph.width
#     return width

# afm_filename = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans.ttf')
# afm = AFM(open(afm_filename, "rb"))
# ttf_filename = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans.ttf')
# font = TTFont(ttf_filename)

# print(get_string_width(font, ' '))


# ref = 'לשמוליק הייתה כבשה ולה לא היה כלב יופי'
ref = 'איזה כיף לשמוליקה אתה כבשה ולהלהלה כלב'
hyp = 'כיף לשמוליק הייתה כבשה ולה לא היה כלב'
# ref = 'froth text le testty test'
# hyp = 'text le texty test what'

out = process_words(ref, hyp)

# hp = 'אוכל'
# str_len = 20
# print(f"{hp:^{str_len}}")
with open('output.txt', 'w') as f:
    f.write(visualize_alignment(out, hebrew=True))
# print(visualize_alignment(out))
# print(out)