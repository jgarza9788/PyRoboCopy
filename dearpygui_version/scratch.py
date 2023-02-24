



#https://stackoverflow.com/questions/4408377/how-can-i-get-terminal-output-in-python

# import time
# import subprocess as sp
# # from multiprocess import Process, Queue
# from multiprocess import Pool


# def f(cmd):
#     result = sp.Popen(cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)   
#     return result


# cmds = []
# cmds.append(" robocopy \"" + r"C:\Users\JGarza\Desktop\New folder" + "\" \"" + r"C:\Users\JGarza\Desktop\New folder (2)" + "\" " )
# # cmds.append(" robocopy \"" + r"C:\Users\JGarza\Desktop" + "\" \"" + r"C:\Users\JGarza\Desktop\New folder (2)" + "\" " )
# # cmds.append(" robocopy \"" + r"D:\PSDs" + "\" \"" + r"C:\Users\JGarza\Desktop\New folder (2)" + "\" " )

# results= []
# def log_results(r):
#     results.append(r)

# with Pool() as p:
#     p.map_async(f,cmds,callback=log_results)

# print(*results,sep='\n')

# print(r)
# print(type(r))

# print(r.get())

# for i in r.get(timeout=1):
#     for line in i.stdout.readlines():
#         # print(line)
#         temp = str(line).replace('b\'','') 
#         temp = temp.replace('\\r\\r\\n\'','')
#         temp = temp.replace('\\r\\n\'','')
#         temp = temp.replace('\\t','')
#         print(temp)



# cmd = "wmic logicaldisk get deviceid, volumename" 
# result = sp.Popen(cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)    

# print(*result.stdout.readlines(),sep='\n')



    # print(line.decode('utf-8'))


# print(*result.stdout.readlines(),sep='\n')
# time.sleep(0.5)
# print(*result.stdout.readlines(),sep='\n')

# temp = ''
# for line in result.stdout.readlines():
#     # print(line)
#     temp = str(line).replace('b\'','') 
#     temp = temp.replace('\\r\\r\\n\'','')
# print(temp)


# import dearpygui.dearpygui as dpg

# dpg.create_context()
# dpg.create_viewport()
# dpg.setup_dearpygui()

# with dpg.theme() as disabled_theme:
#     with dpg.theme_component(dpg.mvInputFloat, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0))
#         dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 0, 0))

#     with dpg.theme_component(dpg.mvInputInt, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0))
#         dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 0, 0))

# dpg.bind_theme(disabled_theme)

# with dpg.window(label="tutorial"):
#     dpg.add_input_float(label="Input float", enabled=False)
#     dpg.add_input_int(label="Input int", enabled=False)


# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()