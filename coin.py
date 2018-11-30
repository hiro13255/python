import random

def input_guess():
    while True:
        print('コインの裏表を当ててください。\n裏表で入力してください-->')
        guess_str = input()
        if guess_str =='表':
            return 1
        elif guess_str =='裏':
            return 0
        else:
            print('表か裏で入力してください')

toss = random.randint(0,1) #0:裏 1:表
guess = input_guess()

if toss == guess:
    print('あたり！')
else:
    print('はずれ！もう一度入力してください-->')
    guess = input_guess
    if toss == guess:
        print('あたり！')
    else:
        print('残念！このゲームは苦手ですね')

