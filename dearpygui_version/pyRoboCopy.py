
import os, json
import subprocess as sp

import dearpygui.dearpygui as dpg

import logging 
import logging.config


logging.basicConfig(filename='log',format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8', filemode='w', level=logging.DEBUG)



class JData():
    def __init__(self,file=None,default=[]):
        self.default = default
        if file == None:
            directory = os.path.dirname(os.path.realpath(__file__))
            self.file = os.path.join(directory,'data.json')
        self.data = self.load()
        logging.info('init Json Data Object --> JData')

    def load(self):
        logging.info('loading Json data')
        try:
            with open(self.file,'r') as file:
                return json.load(file)
        except:
            logging.error('error, while loading json file')
            self.data = self.default
            self.save()
            return self.data

    def save(self):
        with open(self.file,'w') as file:
            file.write(json.dumps(self.data,indent=4))
            logging.info(f'saved file {self.file}')

def run_all(data):
    logging.info('running all commands')

    data = [d for d in data if d['enabled'] == True]
    print(*data,sep='\n')

    for d in data:
        
        if os.path.exists(d['src'][:3]) and os.path.exists(d['dest'][:3]):

            purge = '/MIR' if d['purge'] == 1 else '/S' 
            # print(purge)

            # normal terminal 
            # cmd = "start cmd /c robocopy \"" + d['src'] + "\" \"" + d['dest'] + "\" " + purge

            # windows terminal
            cmd = "start wt -p \"pwsh\"  robocopy \"" + d['src'] + "\" \"" + d['dest'] + "\" " + purge

            logging.info(f'running: {cmd}')
            
            # print(cmd)
            os.system(cmd)
        else:
            logging.error(f'error while running: {str(d)}')
            msg = 'src and/or dest are not valid paths'
            print(msg)
            os.system('start cmd /c echo ' + msg)

def get_drives():
    logging.info('getting list of all drives')
    command = "wmic logicaldisk get deviceid, volumename" 
    pipe = sp.Popen(command,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)    

    result = ''
    for line in pipe.stdout.readlines():
        # print(line)
        temp = str(line).replace('b\'','') 
        temp = temp.replace('\\r\\r\\n\'','')
        result += '\n' + temp
        logging.info(f'found drive: {temp}')
    
    return result + '\n'
    


class MainWindow():
    def save_callback(self,sender, app_data):
        self.do.save()
        dpg.delete_item("##commands")
        self.build_commands()
        logging.info('saved data')

    def change_folder_callback(self,sender, app_data):
        try:
            logging.info('change_folder_callback')

            print('index: ',self.index)
            print("Sender: ", sender)
            print("App Data: ", app_data)

            self.do.data[self.index][sender] = app_data['file_path_name']
            self.do.save()
            self.refresh()
        except Exception as e:
            logging.error('change_folder_callback')
            print('sorry error!')
            print(str(e))
            


    def refresh(self):
        try:
            logging.info('refresh()')
            dpg.delete_item("##commands")
            self.build_commands()
        except:
            logging.error('refresh()')
            pass

    def __init__(self):

        logging.info('start - init')

        self.do = JData()
        self.index = 0

        dpg.create_context()
        dpg.create_viewport(title="pyRoboCopy",width=800,height=800)
        dpg.setup_dearpygui()

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

                # dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 200, 0])
                # dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 100, 0])

        with dpg.window(label="Example Window",tag="Primary Window"):
            # dpg.set_title

            dpg.add_file_dialog(directory_selector=True, show=False, callback=self.change_folder_callback, tag='src'
                ,label = 'source path'
                ,modal = True
                ,width=650,height=650)
            dpg.add_file_dialog(directory_selector=True, show=False, callback=self.change_folder_callback, tag='dest'
                ,label = 'destination path'
                ,modal = True
                ,width=650,height=650)

            self.build_commands()

            # shows a list of drives , with names
            with dpg.group(tag='drives',parent='Primary Window',horizontal=True):
                dpg.add_text(get_drives()) 

            with dpg.group(tag='buttons',parent='Primary Window',horizontal=True):
                add_button = dpg.add_button(label=" + ", callback=self.add_new, tag='')
                run_button = dpg.add_button(label="Run All", callback=lambda: run_all(self.do.data), tag='')
                refresh_button = dpg.add_button(label="refresh", callback=self.refresh, tag='')

                with dpg.tooltip(add_button):
                    dpg.add_text('add new command')

                with dpg.tooltip(run_button):
                    dpg.add_text('run all enabled commands')

            dpg.bind_item_theme(add_button, main_button_theme)
            dpg.bind_item_theme(run_button, run_button_theme)

            # with dpg.group(tag='buttons',parent='Primary Window',horizontal=True):
            dpg.add_text('   , SRC, DEST, PURGE, ENABLE, REMOVE')

            self.refresh()
            

        dpg.set_primary_window("Primary Window", True)
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def build_commands(self):
        logging.info('building the list')
        with dpg.group(tag='##commands',parent='Primary Window'):
            for index,data in enumerate(self.do.data):
                r = self.create_row(str(index),data)

                if data['enabled'] == 0:
                    dpg.bind_item_theme(r,self.disabled_theme)
                


    def add_new(self):
        logging.info('add new item to list')
        self.do.data.append(
            {
                "src": "X:\\",
                "dest": "Y:\\",
                "purge": False,
                "enabled": False,
            }
        )
        print(self.do.data)
        self.do.save()
        self.refresh()

    def edit_folder(self,tag,sd):
        logging.info(f'edit_folder({tag},{sd})')
        self.index = int(tag)
        print(sd,self.do.data[self.index][sd])
        dpg.configure_item(sd,default_path=self.do.data[self.index][sd])
        dpg.show_item(sd)

    def edit_boolean(self,tag,type,value):
        logging.info(f'edit_boolean({tag},{type},{value})')
        print(tag,value)
        self.index = int(tag)
        self.do.data[self.index][type] = value
        self.do.save()
        self.refresh()

    def remove_item(self,tag):
        logging.info(f'remove_item({tag})')
        print('remove: ',tag)
        self.index = int(tag)
        del self.do.data[self.index]
        self.do.save()
        self.refresh()

    def minimize_path(self,path):
        # logging.info(f'minimize_path({path})')
        if len(path) <= 35:
            return path
        else: 
            return path[0:3] + '...\\' + path.split('\\')[-1]

    def create_row(self,tag,data):
        logging.info(f'create_row({tag},{str(data)})')

        with dpg.group(horizontal=True) as row:

            enabled = False
            if bool(data['enabled']) and os.path.exists(data['src'][:3]) and os.path.exists(data['dest'][:3]):
                enabled = True

            missing_sd = True
            if os.path.exists(data['src'][:3]) and os.path.exists(data['dest'][:3]):
                missing_sd = False


            if missing_sd:
                err = dpg.add_text('[!]')
                dpg.bind_item_theme(err, self.red_text_theme)

                with dpg.tooltip(err):
                    dpg.add_text('drive might be missing')
            else:
                x = dpg.add_text('   ')


            src_button = dpg.add_button(
                label=self.minimize_path(data['src']),
                callback=lambda: self.edit_folder(tag,'src'),
                width=250,
                enabled = bool(data['enabled']),
                # enabled = enabled
                )
            
            with dpg.tooltip(src_button):
                dpg.add_text(data['src'])
            if os.path.exists(data['src'][:3]) == False:
                dpg.bind_item_theme(src_button,self.red_text_theme)

            dest_button = dpg.add_button(
                label=self.minimize_path(data['dest']),
                callback=lambda: self.edit_folder(tag,'dest'),
                width=250,
                enabled = bool(data['enabled']),
                # enabled = enabled
                ) 
            with dpg.tooltip(dest_button):
                dpg.add_text(data['dest'])
            if os.path.exists(data['dest'][:3]) == False:
                dpg.bind_item_theme(dest_button,self.red_text_theme)

            purge_cb = dpg.add_checkbox(
                label="purge",
                default_value=bool(data['purge']), 
                callback=lambda sender, data: self.edit_boolean(tag,'purge',dpg.get_value(sender)),
                # enabled = bool(data['enabled']),
                enabled = enabled
                )
            with dpg.tooltip(purge_cb):
                dpg.add_text('purge the destintion path')

            enabled_cb = dpg.add_checkbox(
                label="enabled",
                default_value=bool(data['enabled']), 
                # default_value=enabled,
                callback=lambda sender, data: self.edit_boolean(tag,'enabled',dpg.get_value(sender)) ,
                # enabled = ( missing_src == False and missing_dest == False )
                )
            with dpg.tooltip(enabled_cb):
                dpg.add_text('will only run if enabled')

            dpg.add_button(
                label='remove', 
                callback=lambda: self.remove_item(tag),
                enabled = True
                ) 

            return row


if __name__ == "__main__":
    MW = MainWindow()


