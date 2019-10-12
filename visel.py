from tkinter import *
import random

root = Tk()
root.title('Висилица')
canvas = Canvas(root, width=600, height=600)
canvas.pack()


words = ['Толерантность', 'эксгумация', 'либерализм', 'экспонат', 'пышность', 'скабрёзность', 'шаловливость',
         'экспозиция', 'индульгенция', 'контрацептив', 'шкворень', 'эпиграф', 'эпитафия', 'барбекю', 'жульен',
         'энцефалопатия', 'парашютист', 'импозантность', 'индифферент', 'демультипликатор', 'педикулёз', 'выхухоль',
         'россомаха', 'сущность', 'поэтапность', 'напыщенность', 'возвышенность']
square = 33  #
fag = '''тут находятся правила игры'''


def hidden_word():
    x_hidden_letter = 282
    step_hidden_letter = 30
    word = random.choice(words)
    #if len(word) > 6:
    #first_and_last= word[1: -1]
    #hidden_letter = []
    for i in word:
        canvas.create_text(x_hidden_letter, 40, text='_', fill='black', font=('Helvetica', 16))
        x_hidden_letter = x_hidden_letter + step_hidden_letter

def background():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + square, y + square, fil='white', outline='blue')
            x = x + square
        y = y + square

but_start = Button(root, text='начать играть', width=10, height=2, command=lambda: hidden_word())
# background()
#hidden_word()
canvas.create_text(310, 240, text=fag, fill='black', font=('Helvetica', 16))
but_start.place(x=260, y=550)
but_start['bg'] = 'green'
root.mainloop()
