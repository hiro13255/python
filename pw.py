import shelve,sys,random,re,string
import pyperclip as py 

name = sys.argv[1]
pw_shelf = shelve.open('pw')

def strength_test(pw):#pwが強ければTrue,でなければFalse
    test_A = re.search(re.compile(r'[A-Z]+'),pw)
    test_a = re.search(re.compile(r'[a-z]+'),pw)
    test_0 = re.search(re.compile(r'[0-9]+'),pw)
    test_symbol = re.search(re.compile('[!-/:-@[-`{-~]+'),pw)
    if test_A and test_a and test_0 and test_symbol:
        return True
    else:
        return False

def display_list():#登録されているnameを出力
    name_list = list(pw_shelf.keyencoding())
    name_list.sort(key=str.lower)
    print('アルファベット順'.center(20,'-'))
    for k in name_list:
        print(k)
    print('-' * 20)

if sys.argv[1] == 'list':
    display_list()
    sys.exit()

if name in pw_shelf.keys():
    print(name + 'のパスワードを確認しました')
    py.copy(pw_shelf[name])
    print('パスワードをコピーしました')
else:
    print(name + 'のパスワードが登録されていません\nパスワードを生成して登録しますか(y/n)')
    yn = input()
    if yn == 'y':
        print('パスワードを生成します\nパスワードの文字数を入力してください')
        character_num = int(input())
        while True:
            str = string.ascii_letters + string.digits + string.punctuation
            pw_lst = random.sample(str,character_num)
            pw = ''.join(pw_lst)
            if strength_test(pw):
                py.copy(pw)
                pw_shelf[name] = pw
                print('パスワードの登録とコピーが完了しました')
                break
            else:
                print('exit')