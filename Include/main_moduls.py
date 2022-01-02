from main_window.create_main_window import MainWindow

polish_tabs_name = ('Słówka i zdania', 'Czasy i gramatyka', 'Statystyka', 'Zestawy słówek i zdań')
new_main_window = MainWindow()


def create_main_window():
    new_main_window.create_main_window()
    new_main_window.setting_of_all_notebooks()


def create_new_tab_words_and_sentence():
    new_main_window.new_notebook_words_and_sentence(polish_tabs_name[0])
    new_main_window.add_new_button(new_main_window.get_table_with_all_tabs()[0], 'Bla,bla,Bla')
    new_main_window.add_new_button(new_main_window.get_table_with_all_tabs()[0], 'Ble,ble ble')


def new_notebook_tenses_and_grammar_tab():
    new_main_window.new_notebook_tenses_and_grammar(polish_tabs_name[1])


def notebook_statistics_tab():
    new_main_window.new_notebook_statistics(polish_tabs_name[2])


def notebook_words_and_sentences_packet_tab():
    new_main_window.new_notebook_words_and_sentences_packet(polish_tabs_name[3])


def mainloop():
    new_main_window.use_root_mainloop()


create_main_window()
create_new_tab_words_and_sentence()
new_notebook_tenses_and_grammar_tab()
notebook_statistics_tab()
notebook_words_and_sentences_packet_tab()
mainloop()
