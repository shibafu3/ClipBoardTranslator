"""
paper_translator.py
"""
from time import sleep
from tqdm import tqdm
import pyperclip
from googletrans import Translator
from plyer import notification

"""
GLOBALS
"""
tl = Translator()

"""
METHODS
"""
def split_text(text):
    replaces = [['-\n', ''],
                ['\n', ''],
                ['Fig. ', 'Fig'],
                ['Figs.', 'Figs'],
                ['et al.', 'et al'],
                ['e.g.', 'eg'],
                ['Sec.', 'Sec'],
                ['i.e.', 'ie'],
                ['- ', '']]
    for li in replaces:
        text = text.replace(li[0], li[1])
    li = text.split('. ')
    li = [s + '.' for s in li]
    return li

"""
MAIN
"""
if __name__ == '__main__':
    ######## MAIN ########
    pyperclip.copy('')
    text = pyperclip.paste()
    output = ''
    while True:
        if text != pyperclip.paste():
            li = split_text(pyperclip.paste())
            for s, _ in zip(li, tqdm(range(len(li)))):
                if len(s) < 3:
                    continue
                trans = tl.translate(s, src='en', dest='ja').text
                output += trans + '\n'
            print(output)
            text = pyperclip.paste()
            output = ''
        sleep(0.5)