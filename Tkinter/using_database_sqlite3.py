# from tkinter import *
# from PIL import ImageTk, Image
# import sqlite3
#
# root = Tk()
# root.title('Temporary title.')
# root.geometry('400x400')
#
# # Database
#
# # Create a database or connect to one
# conn = sqlite3.connect('Words_sentences_and_statistic_packet.db')
#
# # Create cursor
# cursor = conn.cursor()
#
# # Create table
# cursor.execute('''CREATE TABLE words (
#                 english_version text,
#                 polish_version text
#                 )''')
#
# # Commit Changes
# conn.commit()
#
# # Close connection
# conn.close()
#
# root.mainloop()
