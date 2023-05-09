from tkinter import *
from PIL import Image, ImageTk

# 	PNG_IMAGE = 'kantor.png'

# 	pygame.display.init()
# 	img = pygame.image.load(_PNG_IMAGE)
# 	screen = pygame.display.set_mode(img.get_size(400,400))
# 	screen.blit(img, (0, 0))
# 	pygame.display.flip()

# , pygame.FULLSCREEN
	
	# 	pygame.quit()

def image():
	root = Tk()

	img = ImageTk.PhotoImage(Image.open("ricardo.png"))

	b = Label(image = img)

	b.pack()

	root.mainloop()


