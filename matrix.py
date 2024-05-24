import dearpygui.dearpygui as dpg

def set_matrix_button_callback(sender):
    num = 2
    if(dpg.get_item_alias(sender) == "B1"):
        num = 1
    lab = f"Matrix{num}"
    if(dpg.does_item_exist(lab)):
        dpg.delete_item(lab)
    if num == 1:
        row = dpg.get_value("Input1")
        column = dpg.get_value("Input2")
        with dpg.child_window(label="Matrix 1 input", width=100, height =100, tag=lab,parent="Primary Window", before="begM2"):
            create_matrix(row,column,num,lab)
    else:
        row = dpg.get_value("Input3")
        column = dpg.get_value("Input4")
        with dpg.child_window(label="Matrix 2 input", width=100, height =100, tag=lab,parent="Primary Window"):
            create_matrix(row,column,num,lab)
            

def create_matrix(row,column,num,lab):
    for i in range(row):
        with dpg.group(horizontal=True):
            for j in range(column):
                dpg.add_input_float(tag=f"M{num}{i}{j}", min_value=0, default_value=0, width=60,label="",step=0)
    dpg.set_item_width(lab,column*70+20)
    dpg.set_item_height(lab,row*23+35)
    dpg.add_button(label="Transpose",callback=transpose_button_callback,tag=f"T{num}")

def transpose_button_callback(sender):
    num = 2
    if(dpg.get_item_alias(sender) == "T1"):
        num = 1
    lab = f"Matrix{num}"
    if num == 1:
        column = dpg.get_value("Input1")
        row = dpg.get_value("Input2")
        dpg.set_value("Input1",row)
        dpg.set_value("Input2",column)
    else:
        column = dpg.get_value("Input3")
        row = dpg.get_value("Input4")
        dpg.set_value("Input3",row)
        dpg.set_value("Input4",column)
    values = storeValues(column,row,num)
    dpg.delete_item(lab)
    dpg.delete_item(sender)
    if num == 1:
        with dpg.child_window(label="Matrix 1 input", width=100, height =100, tag=lab,parent="Primary Window", before="begM2"):
            transpose_matrix(row,column,num,values,lab)
    else:
        with dpg.child_window(label="Matrix 2 input", width=100, height =100, tag=lab,parent="Primary Window"):
            transpose_matrix(row,column,num,values,lab)
            

def storeValues(column,row,num):
    values = []
    for i in range(column):
        for j in range(row):
            values.append(dpg.get_value(f"M{num}{i}{j}"))
    return values

def transpose_matrix(row,column,num,values,lab):
    count = 0
    for i in range(row):
        with dpg.group(horizontal=True):
            for j in range(column):
                #for integer only inputs
                #dpg.add_input_int(label="", min_value=0,default_value=values[count], width=80, tag=f"M1{i}{j}",step=0)
                dpg.add_input_float(tag=f"M{num}{i}{j}", min_value=0, default_value=values[count], width=60,label="",step=0)
                count = count+1
    dpg.set_item_width(lab,column*70+20)
    dpg.set_item_height(lab,row*23+35)
    dpg.add_button(label="Transpose",callback=transpose_button_callback,tag=f"T{num}")   

def main():
    dpg.create_context()

    with dpg.window(tag="Primary Window"):
        #matrix 1 sizeList = [row, column] inputs
        dpg.add_text("Matrix 1")
        dpg.add_input_int(label="Rows", default_value=0, width=80, tag="Input1", min_value=0)
        dpg.add_input_int(label="Columns", default_value=0,  width=80, tag="Input2", min_value=0) 
        '''no increment buttons
        with dpg.group(horizontal=True):
            dpg.add_input_int(label="Rows", default_value=0, width=30, tag="Input1",min_value=0,step=0)
            dpg.add_input_int(label="Columns", default_value=0,  width=30, tag="Input2", min_value=0,step=0)
        '''
        dpg.add_button(label="Set Matrix 1 Size", callback=set_matrix_button_callback,tag="B1")
        #with dpg.child_window(label="Matrix 1 input", width=1, height=1, tag="Matrix1"):
        #    dpg.add_text("test text")

        #matrix 2 sizeList = [row, column] inputs
        dpg.add_text("Matrix 2",tag="begM2")
        dpg.add_input_int(label="Rows", default_value=0, width=80, tag="Input3",min_value=0)
        dpg.add_input_int(label="Columns", default_value=0,  width=80, tag="Input4", min_value=0)
        '''no increment buttons
        with dpg.group(horizontal=True):
            dpg.add_input_int(label="Rows", default_value=0, width=30, tag="Input3",min_value=0,step=0)
            dpg.add_input_int(label="Columns", default_value=0,  width=30, tag="Input4", min_value=0,step=0)
        '''
        dpg.add_button(label="Set Matrix 2 Size", callback=set_matrix_button_callback,tag="B2")
        #with dpg.child_window(label="Matrix 2 input", width=100, height =100, tag="Matrix2"):

    #sizeList = [row, column] and name of the primary window viewport
    dpg.create_viewport(title='Matthew\'s Magnificent Matrix Machine', width=600, height=500)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    
    #loop to run other code with main window
    while dpg.is_dearpygui_running():
        # insert here any code you would like to run in the render loop
        # you can manually stop by using stop_dearpygui()
        print("this will run every frame")
        dpg.render_dearpygui_frame()
    
    #end the program
    dpg.destroy_context()

if __name__ == "__main__":
    main()
