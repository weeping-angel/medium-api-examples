import requests
from urllib.parse import quote_plus
import os

l = (
    ('python', 'py', 'python'),
    ('curl', 'sh', 	"shellscript")
)

def preprocess(filename):
    codelines = open(filename, 'r').readlines()
    codelines = [line for line in codelines if line[0]!='#']

    return ''.join(codelines).strip('\n')

def generate_image(code:str, lang:str, filepath:str, bg:str = 'none'):
    # print('\t generating image ...')
    theme = 'nord'
    padding_tb = 65
    padding_lr = 105
    num = 1
    watermark = ''
    url = f"https://kod.so/gen?code={quote_plus(code.strip())}&num={num}&lang={lang}&background={bg}&theme={theme}&watermark={watermark}&paddingtb={padding_tb}&paddinglr={padding_lr}"

    resp = requests.get(url)
    if resp.status_code==200:
        print(filepath)
        open(filepath, 'wb').write(resp.content)
    else:
        print(f'[ERROR - {filepath}]: ', resp.status_code, '\t', str(resp.content))
        print(len(code))

def main():
    for directory, ext, lang in l:
        os.makedirs(f'images/{directory}', exist_ok=True)
        for file in os.listdir(directory):
            filename, extension = file.split('.')
            if extension==ext and (filename in ['archived_articles', 'recommended_lists', 'recommended_users', 'user_books', 'root_tags']):
                # print(file)
                params = { 
                    "code": preprocess(f"{directory}/{file}"),
                    "lang": lang,
                    "filepath": f'images/{directory}/{filename}.png',
                    "bg": 'bg-2.jpg'
                }

                generate_image(**params)

                # generate transparent counterpart

                params['bg'] = 'none'
                params['filepath'] = f"images/{directory}/{filename}-transparent.png"

                generate_image(**params)
        

if __name__=='__main__':
    main()