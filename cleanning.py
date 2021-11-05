
import processing
import os
import urllib.request
from bs4 import BeautifulSoup

def clean_script(html):
    soup =  BeautifulSoup(html,features="html.parser")
    for script in soup(["script",'style']):
        script.extract()
    text = soup.get_text()
    return text

def download_html(url_path, out_path):
    with urllib.request.urlopen(url_path) as response:
        html = response.read()
        text = clean_script(html)
        text =text.strip()
        with open(out_path, 'a',encoding='utf-8') as fw:
            fw.write(text)
    return text


def clean_html_file(input_path, output_path):
    #if os.path.exists(output_path):
        #raise Exception("Output path existed")
    with open(input_path, 'r',encoding='utf-8') as fr:
        text = fr.read()
    doc = processing.text_preprocess(text)
    #print(doc)
    with open(output_path, 'a',encoding='utf-8') as fw:
        fw.write(doc+'\n')


def clean_files_from_dir(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    input_files = os.listdir(input_dir)
    for input_file in input_files:
        input_file_path = os.path.join(input_dir,input_file)
        if input_file.startswith('.') or os.path.isdir(input_file):
            continue
        #output_file_path = os.path.join(output_dir, input_file)
        clean_html_file(input_file_path, output_dir)



def test_download_html():
    url_path = "https://kenh14.vn/nam-sinh-lam-han-bang-thong-bao-mong-hang-xom-han-che-am-thanh-de-thi-online-soi-thanh-tich-hoc-la-biet-ngay-tai-sao-20211030122421577.chn"
    output_path = "data/html/html_data4.txt"
    download_html(url_path,output_path)


def test_clean_file():
    data_path = "data/html/html_data.txt"
    output_path = "data/clean/data.txt"
    clean_html_file(data_path, output_path)


def test_clean_files_in_dir():
    input_dir = 'data/html'
    output_dir = 'data/clean/data.txt'
    clean_files_from_dir(input_dir, output_dir)

#https://kenh14.vn/tu-1-11-them-8-tuyen-xe-buyt-tai-tphcm-hoat-dong-tro-lai-20211030161038631.chn
#https://kenh14.vn/u23-viet-nam-doi-mua-buot-tap-luyen-trong-ngay-kyrgyzstan-lanh-dot-ngot-20211029175134401.chn
#https://kenh14.vn/nam-sinh-lam-han-bang-thong-bao-mong-hang-xom-han-che-am-thanh-de-thi-online-soi-thanh-tich-hoc-la-biet-ngay-tai-sao-20211030122421577.chn
#https://kinhtedothi.vn/ha-noi-kinh-te-thang-10-dan-hoi-phuc-439503.html

if __name__ == '__main__':
    #test_download_html()
    #test_clean_file()
    #test_clean_files_in_dir()
    processing.remove_stopwords()