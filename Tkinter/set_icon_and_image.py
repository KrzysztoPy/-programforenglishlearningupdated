# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# root.title('Nothing')
# root.iconbitmap('C://Users//Kriss//Desktop//eye.ico')
#
# '''
# If you want use image you need install:
# pip install Pillow and from PIL import ImageTk,Image
# '''
#
# # # Step 1: Define image
# # my_img = ImageTk.PhotoImage(Image.open('C://Users//Kriss//Desktop//eye.ico'))
# #
# # # Step 2: Put imagine on label or something similar
# # my_image_label = Label(image=my_img)
# # # Step 3: View on screen
# # my_image_label.pack()
#
# #######################################################################################################################
# # Moving between photos
#
# img_1 = ImageTk.PhotoImage(Image.open('C:/Users/Kriss/Desktop/XYZ/Koteł.PNG'))
# img_2 = ImageTk.PhotoImage(Image.open('C:/Users/Kriss/Desktop/XYZ/Koteł1.PNG'))
# img_3 = ImageTk.PhotoImage(Image.open('C:/Users/Kriss/Desktop/XYZ/songo1.PNG'))
#
# my_image_list = [img_1, img_2, img_3]
# my_image_list_label = Label(image=my_image_list[0])
# status = Label(root, text='Image 1 of {}'.format(my_image_list.__len__()))
#
#
# def sub_number():
#     return
#
#
# def preview_image(currently_chosen_picture):
#     global my_image_list_label
#     global preview_image_button
#     global next_image_button
#     global status
#
#     my_image_list_label.grid_forget()
#     if currently_chosen_picture == 0:
#         currently_chosen_picture = my_image_list.__len__() - 1
#         my_image_list_label = Label(image=my_image_list[currently_chosen_picture])
#
#     else:
#         currently_chosen_picture -= 1
#         my_image_list_label = Label(image=my_image_list[currently_chosen_picture])
#
#     preview_image_button = Button(root, text='<<', command=lambda: preview_image(currently_chosen_picture), padx=50,
#                                   pady=20, width=40)
#     next_image_button = Button(root, text='>>', command=lambda: next_image(currently_chosen_picture), padx=50,
#                                pady=20, width=40)
#     status = Label(root, text='Image {} of {}'.format(currently_chosen_picture + 1, my_image_list.__len__()))
#
#     my_image_list_label.grid(row=0, column=0, columnspan=3)
#     preview_image_button.grid(row=1, column=0)
#     next_image_button.grid(row=1, column=1)
#     status.grid(row=2, column=1)
#
#
# def next_image(currently_chosen_picture):
#     global my_image_list_label
#     global preview_image_button
#     global next_image_button
#     global status
#
#     my_image_list_label.grid_forget()
#
#     if currently_chosen_picture == my_image_list.__len__() - 1:
#         currently_chosen_picture = 0
#         my_image_list_label = Label(image=my_image_list[currently_chosen_picture])
#
#     else:
#         currently_chosen_picture += 1
#         my_image_list_label = Label(image=my_image_list[currently_chosen_picture])
#
#     preview_image_button = Button(root, text='<<', command=lambda: preview_image(currently_chosen_picture), padx=50,
#                                   pady=20, width=40)
#     next_image_button = Button(root, text='>>', command=lambda: next_image(currently_chosen_picture), padx=50,
#                                pady=20, width=40)
#     status = Label(root, text='Image {} of {}'.format(currently_chosen_picture + 1, my_image_list.__len__()))
#
#     my_image_list_label.grid(row=0, column=0, columnspan=3)
#     preview_image_button.grid(row=1, column=0)
#     next_image_button.grid(row=1, column=1)
#     status.grid(row=2, column=1)
#
#
# preview_image_button = Button(root, text='<<', command=lambda: preview_image(0), padx=50,
#                               pady=20, width=40)
# next_image_button = Button(root, text='>>', command=lambda: next_image(0), padx=50, pady=20,
#                            width=40)
#
# my_image_list_label.grid(row=0, column=0, columnspan=3)
# preview_image_button.grid(row=1, column=0)
# next_image_button.grid(row=1, column=1)
# status.grid(row=2, column=1)
#
# root.mainloop()
