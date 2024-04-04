import os


def main():
    i = 0
    path = ""  # put the folder file path you want to rename
    for filename in os.listdir(path):
        my_desk = "img" + str(i) + ".jpg"  # You can change the jpg file into any other available image format
        my_source = path + filename
        my_desk = path + my_desk
        os.rename(my_source, my_desk)
        i += 1
        print('successfully rename!')


if __name__ == '__main__':
    main()
