import os
import json5 as json
import subprocess as sp
import dearpygui.dearpygui as dpg

from utils.menu import menu
from utils.JData import JData #data manager 

class MainWindow():
    def __init__(self):
        self.DIR = os.path.dirname(os.path.realpath(__file__))
        self.JData = JData(file=os.path.join(self.DIR,'data.json'))

        # self.DIR = os.path.dirname(os.path.realpath(__file__))
        # self.dfile = os.path.join(self.DIR,'data.json')
        # self.data = funct.get_data(self.dfile)

        # self.config = funct.get_data(os.path.join(self.DIR,'config.json'))
        # self.always_exlcude =self.config['always_exclude']
        
        # self.results = []
        # self.results = funct.search(self.data[0])
        # self.filtered_results_count = len(self.results)

        # self.layout = os.path.join(self.DIR,'layout.ini')

        dpg.create_context()

        # with dpg.font_registry():
        #     df = os.path.join(self.DIR,"fonts",'Hack Regular Nerd Font Complete Mono Windows Compatible.ttf')
        #     # default_font = dpg.font(df, 14)
        #     # with dpg.font(df, 14) as font1:
        #     dfont = dpg.add_font(df, 14)
        #     dpg.bind_font(dfont)
        # dpg.show_font_manager()
    

        # self.mythemes = {}
        # self.mythemes = theme.get_themes()

        # dpg.configure_app(
        #     docking=True, 
        #     docking_space=True,
        #     load_init_file=self.layout 
        #     ) 
        

        with dpg.theme() as disabled_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Text, [100, 100, 100])
                dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 37, 37])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [100, 0, 0])
        self.disabled_theme = disabled_theme

        with dpg.theme() as main_button_theme:
            with dpg.theme_component(dpg.mvAll):
                # dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255])
                dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 100, 255])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 200, 255])

        with dpg.theme() as run_button_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Text, [0, 0, 0])
                dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 200, 0])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 100, 0])

        with dpg.theme() as red_text_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
        self.red_text_theme = red_text_theme

        dpg.create_viewport(title='pyRoboCopy', width=600, height=800,x_pos = 400,y_pos = 25,)

        dpg.setup_dearpygui()

        # self.windows = {}
        # self.windows["main_window"] = "main_window"

        # main_window

        with dpg.window(tag="main_window",
            label='main',
            no_close=True,
            # no_title_bar=True,
            no_collapse=True
            ):
            

            with dpg.group(tag='buttons',horizontal=True):
                add_button = dpg.add_button(label=" + ", callback=self.add_new, tag='')
                run_button = dpg.add_button(label="Run All", callback= self.run_all, tag='')

                with dpg.tooltip(add_button):
                    dpg.add_text('add new command')

                with dpg.tooltip(run_button):
                    dpg.add_text('run all enabled commands')

            dpg.bind_item_theme(add_button, main_button_theme)
            dpg.bind_item_theme(run_button, run_button_theme)

            self.create_table()


        # self.filter_window = dpg.generate_uuid()
        # self.item_window = dpg.generate_uuid()
        # self.items_tags = []
        # self.result_window = dpg.generate_uuid()
        # self.result_tags = []
        # self.new_search_window = dpg.generate_uuid()

        # menu(self)
        # new_search_window(self)
        # filter_window(self)

        # result_window(self)
        # self.refresh_results_window()
        
        # item_window(self)
        # self.refresh_item_window()

        # dpg.show_viewport()
        # while dpg.is_dearpygui_running():
        #     dpg.render_dearpygui_frame()
        # dpg.destroy_context()


        dpg.set_primary_window("main_window", True)
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def delete_ui_objects(self,tag_list):
        for tag in tag_list:
            try:
                dpg.delete_item(tag)
            except:
                pass

    def add_new(self):
        print("add new item")

    def run_all(self):
        print("add new item")

    def create_table(self):
        with dpg.table(
            header_row=True, 
            resizable=True, 
            policy=dpg.mvTable_SizingStretchProp,
            # borders_outerH=True, 
            borders_innerV=True, 
            borders_innerH=True, 
            # borders_outerV=True
            ):

            dpg.add_table_column(label="*")
            dpg.add_table_column(label="Src")
            dpg.add_table_column(label="Dest")
            dpg.add_table_column(label="Purge")
            dpg.add_table_column(label="Enabled")
            dpg.add_table_column(label="Remove")
            # dpg.add_table_column(label="Remove")

            # once it reaches the end of the columns

            for index,data in enumerate(self.JData.data):
                self.create_row(str(index),data)

                # if data['enabled'] == 0:
                #     dpg.bind_item_theme(r,self.disabled_theme)

            # for i in range(0, 4):
            #     with dpg.table_row():
            #         for j in range(0, 3):
            #             with dpg.table_cell():
            #                 dpg.add_button(label=f"Row{i} Column{j} a")
            #                 dpg.add_button(label=f"Row{i} Column{j} b")

            # with dpg.table_row():
            #     with dpg.table_cell():
            #         dpg.add_text('')

            # with dpg.table_row():
            #     with dpg.table_cell():
            #         with dpg.group(tag='buttons',horizontal=True):
            #             dpg.add_button(label=" + ", callback=self.add_new, tag='')
            #     # with dpg.table_cell():
            #             dpg.add_button(label="Run All", callback= self.run_all, tag='')

    def minimize_path(self,path):
        if len(path) <= 35:
            return path
        else: 
            return path[0:3] + '...\\' + path.split('\\')[-1]

    def create_row(self,tag,data):

        with dpg.table_row():

            enabled = False
            if bool(data['enabled']) and os.path.exists(data['src'][:3]) and os.path.exists(data['dest'][:3]):
                enabled = True

            missing_sd = True
            if os.path.exists(data['src'][:3]) and os.path.exists(data['dest'][:3]):
                missing_sd = False

            with dpg.table_cell():
                if missing_sd:
                    err = dpg.add_text('[!]')
                    dpg.bind_item_theme(err, self.red_text_theme)

                    with dpg.tooltip(err):
                        dpg.add_text('drive might be missing')
                else:
                    x = dpg.add_text('   ')

            with dpg.table_cell():

                src_button = dpg.add_button(
                    label=self.minimize_path(data['src']),
                    # callback=lambda: self.edit_folder(tag,'src'),
                    width=250,
                    enabled = bool(data['enabled']),
                    )
                
                with dpg.tooltip(src_button):
                    dpg.add_text(data['src'])

                if os.path.exists(data['src'][:3]) == False:
                    dpg.bind_item_theme(src_button,self.red_text_theme)

            with dpg.table_cell():
                dest_button = dpg.add_button(
                    label=self.minimize_path(data['dest']),
                    # callback=lambda: self.edit_folder(tag,'dest'),
                    width=250,
                    enabled = bool(data['enabled']),
                    ) 
                with dpg.tooltip(dest_button):
                    dpg.add_text(data['dest'])

                if os.path.exists(data['dest'][:3]) == False:
                    dpg.bind_item_theme(dest_button,self.red_text_theme)


            with dpg.table_cell():
                purge_cb = dpg.add_checkbox(
                    label="",
                    default_value=bool(data['purge']), 
                    # callback=lambda sender, data: self.edit_boolean(tag,'purge',dpg.get_value(sender)),
                    enabled = bool(data['enabled']),
                    )
                with dpg.tooltip(purge_cb):
                    dpg.add_text('purge the destintion path')


            with dpg.table_cell():
                enabled_cb = dpg.add_checkbox(
                    label="",
                    default_value=bool(data['enabled']), 
                    # default_value=enabled,
                    # callback=lambda sender, data: self.edit_boolean(tag,'enabled',dpg.get_value(sender)) ,
                    # enabled = ( missing_src == False and missing_dest == False )
                    )
                with dpg.tooltip(enabled_cb):
                    dpg.add_text('will only run if enabled')

            with dpg.table_cell():
                dpg.add_button(
                    label='--X--', 
                    callback=lambda: self.remove_item(tag),
                    enabled = True
                    ) 

            # # return row


if __name__ == "__main__":
    MW = MainWindow()