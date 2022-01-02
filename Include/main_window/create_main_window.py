import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class MainWindow:
    root = Tk()
    new_notebook = ttk.Notebook(root)
    list_with_all_tabs_frames = list()

    def window_centring(self):
        screen_width = int(self.get_screen_width() / 2)
        screen_height = int(self.get_screen_height() / 2)

        return '{0}x{1}+{2}+{3}'.format(screen_width, screen_height, int(screen_width / 2), int(screen_height / 2))

    def create_main_window(self):
        self.root.title('Learning english')
        self.root.iconbitmap('D:/PythonProjects/programForEnglishLearning/Icons/eye.ico')
        self.root.geometry(self.window_centring())

    def setting_of_all_notebooks(self):
        self.get_new_notebook().pack(pady=5)

    def new_notebook_words_and_sentence(self, notebook_name):
        new_frame_new_notebook_words_and_sentence = Frame(self.get_new_notebook(),
                                                          width=self.get_screen_width(),
                                                          height=self.get_screen_height())
        new_frame_new_notebook_words_and_sentence.pack(fill='both', expand=1)

        self.get_table_with_all_tabs().append(new_frame_new_notebook_words_and_sentence)
        self.get_new_notebook().add(new_frame_new_notebook_words_and_sentence,
                                    text=notebook_name,
                                    compound=tkinter.TOP)

    def new_notebook_tenses_and_grammar(self, notebook_name):
        new_frame_tenses_and_grammar = Frame(self.get_new_notebook(),
                                             width=self.get_screen_width(),
                                             height=self.get_screen_height())

        new_frame_tenses_and_grammar.pack(fill='both', expand=1)
        self.get_table_with_all_tabs().append(new_frame_tenses_and_grammar)
        self.get_new_notebook().add(new_frame_tenses_and_grammar,
                                    text=notebook_name,
                                    compound=tkinter.TOP)

    def new_notebook_statistics(self, notebook_name):
        new_frame_statistics = Frame(self.get_new_notebook(),
                                     width=self.get_screen_width(),
                                     height=self.get_screen_height())
        new_frame_statistics.pack(fill='both', expand=1)

        self.get_new_notebook().add(new_frame_statistics,
                                    text=notebook_name,
                                    compound=tkinter.TOP)

    def new_notebook_words_and_sentences_packet(self, notebook_name):
        new_frame_words_and_sentences_packet = Frame(self.get_new_notebook(),
                                                     width=self.get_screen_width(),
                                                     height=self.get_screen_height())
        new_frame_words_and_sentences_packet.pack(fill='both', expand=1)

        self.get_new_notebook().add(new_frame_words_and_sentences_packet,
                                    text=notebook_name,
                                    compound=tkinter.TOP)

    @staticmethod
    def add_new_button(frame_name, text='My button', width=20, height=20, padx=1, pady=1, state='normal'):
        new_button = Button(frame_name, text=text, width=width, height=height, padx=padx, pady=pady, state=state)
        new_button.pack()

    def get_root(self):
        return self.root

    def get_new_notebook(self):
        return self.new_notebook

    def get_screen_width(self):
        return self.get_root().winfo_screenwidth()

    def get_screen_height(self):
        return self.get_root().winfo_screenheight()

    def use_root_mainloop(self):
        self.get_root().mainloop()

    def get_table_with_all_tabs(self):
        return self.list_with_all_tabs_frames
