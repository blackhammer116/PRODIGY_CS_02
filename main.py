from tkinter import *
from tkinter import filedialog
import platform


if platform.system() == "Windows":
    root = Tk()
    root.geometry("300x150")


    def encrypt_image():
        """
        A function to encrypt a give image
        :return:
        """
        imageFile = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg'),
                                                                ('png file', '*.png'),
                                                                ('jpeg file', '*.jpeg')])

        if imageFile is not None:
            print(imageFile)
            key = entry1.get(1.0, END)
            if key is None:
                key = 5
            fi = open(imageFile.name, 'rb')
            image = fi.read()
            fi.close()
            print(image)
            image = bytearray(image)

            for index, value in enumerate(image):
                image[index] = value^int(key)
                file_write = open(imageFile.name, 'wb')
                file_write.write(image)
                file_write.close()

    b1 = Button(root, text="Encrypt/Decrypt", command=encrypt_image)
    b1.place(x=100,y=10)
    entry1 = Text(root, height=1, width=15)
    entry1.place(x=90, y=50)

    root.mainloop()

elif platform.system() == "Linux":
    while(1):
        print("*"*31)
        print("* Welcome to Image encryption  *")
        print("*"*31)
        try:
            imageFile = input("\nPlease Enter the absolute path of the image[TO EXIT ENTER: 1]: ")
            if imageFile == '1':
                print("Good Bye ;)")
                break
            key = input("Enter your key Note key must be type int: ")
            fi = open(imageFile, 'rb')
            image = fi.read()
            fi.close()
            # print(image)
            image = bytearray(image)
        except:
            print("Make sure to enter the absolute path of the image. And also you key MUST be int type")

        for index, value in enumerate(image):
            image[index] = value ^ int(key)
            file_write = open(imageFile, 'wb')
            file_write.write(image)
            file_write.close()
