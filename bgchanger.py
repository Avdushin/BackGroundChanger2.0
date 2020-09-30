import os


#Window man.md
man = open('man.md', mode='r', encoding='UTF-8')
print(man.read())


#programm
print('what image do you want to put on the background?')# Какое изображение хотите поставить на фон?
print('Place the image in the program folder. Path: "./changerbg/')#Поместите изображение в папку программы. Путь: "./bgchanger/

print('Be sure to enter its format!')#Обязательно введите его формат!
# print('Image name: ')#Имя изображения:

img = str(input("Enter image name (*.jpg,*.png,*.jpeg): "))#Введите название изображения: 

print(" ")


#move pictore to background's directory '/usr/share/backgrounds'.
os.system('sudo cp'  + " " + img + " " +  '/usr/share/backgrounds/')

print(" ")


print("Input this comands: ")#Введите эти команды
print(" ")
print(" cd")
print(" ")
print(' sudo ./ubuntu-20.04-change-gdm-background /usr/share/backgrounds/' + img)
#os.system('sudo ./ubuntu-20.04-change-gdm-background /usr/share/backgrounds/' + img)

print(" ")
print(" ")	