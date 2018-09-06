from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt

def wordimage(font_path, word_space_split, image_path):
    coloring = np.array(Image.open(image_path))
    my_wordclod = WordCloud(background_color='white',
                            max_words=2000,
                            mask=coloring,
                            max_font_size=60,
                            random_state=42,
                            scale=2,
                            font_path=font_path
                            ).generate(word_space_split)
    image_colors = ImageColorGenerator(coloring)
    plt.imshow(my_wordclod.recolor(color_func=image_colors))
    plt.imshow(my_wordclod)
    plt.axis('off')
    plt.show()
