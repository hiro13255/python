import webbrowser,requests,shelve
import pyperclip as py 
from bs4 import BeautifulSoup

error_shelf = shelve.open('pyERROR')
error_texts = py.paste()#クリップボードから貼り付け
print('SEARCHING ERROR>>> '+error_texts)

def query_string_remove(url):
    return url[:url.find('&')]

def googling(query,selector,num):
    url = 'https://www.google.co.jp/search?q=' + query
    res = requests.get(url).text
    soup = BeautifulSoup(res,'html.parser')
    tags = soup.select(selector)
    open_num = min(num,len(tags))
    print('serching...')
    for i in range(open_num):
        url = tags[i].get('href').replace('/url?q=','')
        open_link = query_string_remove(url)
        webbrowser.open(open_link)#開く

def mk_error_contents():
    print('エラーの内容を入力してください')
    error_contents = input(':')
    return  error_contents

def mk_error_sol_list():
    sol_list = []
    while True:
        print('解決策を追加してください(Enterで終了）')
        sol = input(':')
        sol_list.append(sol)
        if sol=='':
            del sol_list[-1]#''を消す
            break
        return sol_list

def append_error_dictionary(error_contents,error_sol_list):#shelf[key]に辞書を追加
    error_dictionary = {}
    error_dictionary['contents'] = error_contents
    error_dictionary['solutions'] = error_sol_list
    return error_dictionary

def display_error(error_contents,error_sol_list):#エラー内容と解決策を表示
    print(' ')
    print('ERROR->:' + error_texts)
    print('CONTENTS:' + error_contents)
    print('-' * 20)
    for sol in error_sol_list:
        print('・' + sol)
    print('-' * 20)

def y_or_n():#yかnで入力しなかった場合
    print('yかnで入力してください')
    print('-' * 20)

if error_texts in error_shelf.keys():
    print(error_texts + 'を確認しました')
    contents = error_shelf[error_texts]['contents']
    sol_list = error_shelf[error_texts]['solutions']

    if contents =='':
        print('エラーの内容が登録されていません')
        while True:
            print('Googleで検索しますか?(y/n)')
            yn = input(':')
            if yn == 'y':
                googling(error_texts,'.r a',5)
                break
            elif yn =='n':
                break
            else:
                y_or_n()
        contents = mk_error_contents()

    if sol_list==[]:
        print('解決策が登録されていません')
        while True:
            print('Google電検索しますか？(y/n)')
            yn = input(':')
            if yn == 'y':
                googling(error_texts,'.r a',5)
                break
            elif yn == 'n':
                break
            else:
                y_or_n()
            sol_list = mk_error_sol_list()
    
    display_error(contents,sol_list)
    error_shelf[error_texts] = append_error_dictionary(contents,sol_list)

else:
    while True:
        print('登録されてないエラーです\nGoogle検索しますか?(y/n)')
        yn = input(':')
        if yn == 'y':
            googling(error_texts,'.r a',5)
            break
        elif yn == 'n':
            break
        else:
            y_or_n()
        
    contents = mk_error_contents()
    sol_list = mk_error_sol_list()
    display_error(contents,sol_list)

    error_shelf[error_texts] = append_error_dictionary(contents,sol_list)

error_shelf.close()


