# 1def countdown(name, seconds = 5 ):
#     import time
#
#     for sec in range(seconds, -1, -1):
#         if sec > 0:
#             print(f'Ракета {name} полетит через {sec}')
#         else:
#             print('lift off')
#         time.sleep(1)
#
#
# countdown('Falcon',0)
import random
import tkinter
num_of_symb = 8
def generete_password (symbs = 6): #тут поумолчанию
    symbols = []
    for i in range(symbs):
        num = random.randint(1, 3)
        if num == 1:
            symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols.append(random.choice('0123456789'))
    password = ''.join(str(symb) for symb in symbols)
    text.delete('1.0', tkinter.END)
    text.insert('1.0', password)
# print(generete_password(8)) #тут можно поменять количество символов
window = tkinter.Tk ()
window.config (background = 'black' )
window.geometry ('800x600')
window.title ('генератор поролей')
text = tkinter.Text (
    font=('arial',60),
    height=1,
    width=num_of_symb + 1,
    bg = 'black',
    fg = 'white',
    borderwidth=10
)
text.pack (expand = 1)
tkinter.Button (
    text = 'сгенерировать пороль',
bg = 'black',
    fg = 'white',
    borderwidth=10,
    command=lambda : generete_password(num_of_symb)
).pack(expand=1)



window.mainloop()
