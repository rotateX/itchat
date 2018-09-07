from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt

def wordimage(word_space_split):
    coloring = np.array(Image.open('E:\pythontest\itchat\zzicon.png'))
    my_wordcloud = WordCloud(
        background_color='white',
        max_words=2000,
        mask=coloring,
        max_font_size=60,
        random_state=42,
        scale=2,
        font_path='E:\pythontest\itchat\simhei.ttf'
    ).generate(word_space_split)
    image_colors = ImageColorGenerator(coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()
    my_wordcloud.to_file('p.png')