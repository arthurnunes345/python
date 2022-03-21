from tkinter import *
root = Tk()
tela = Canvas(width = 200, height = 200)

imagem = PhotoImage(file = 'Arthur.jpg')

tela.create_image(50, 50, image = imagem)

tela.pack()

root.mainloop()