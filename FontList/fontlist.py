
import matplotlib.font_manager as fm
import pandas as pd


fonts = fm.findSystemFonts()
l = []
for font in fonts:
    prop = fm.FontProperties(fname=font)
    # l.append((font, prop.get_name(), prop.get_family())) Error on Mac. Why??
    l.append((font, prop.get_family()))
df = pd.DataFrame(l, columns=['path', 'family'])
print('ALL fonts')
print(df)

# only IPA fonts
print('IPA fonts')
print(df[df['path'].apply(lambda s: 'IPA' in s)])
