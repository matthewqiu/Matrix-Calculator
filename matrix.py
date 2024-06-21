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
        with dpg.child_window(label="Matrix 2 input", width=100, height =100, tag=lab,parent="Primary Window",before="DPB"):
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
    #row and column are the new transposed row and column values
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
    values = store_values(column,row,num)
    dpg.delete_item(lab)
    dpg.delete_item(sender)
    if num == 1:
        with dpg.child_window(label="Matrix 1 input", width=100, height =100, tag=lab,parent="Primary Window", before="begM2"):
            transpose_matrix(row,column,num,values,lab)
    else:
        with dpg.child_window(label="Matrix 2 input", width=100, height =100, tag=lab,parent="Primary Window",before="DPB"):
            transpose_matrix(row,column,num,values,lab)      

#stores the current values in a list and returns the list. Values are stored up to down left to right 
def store_values(column,row,num):
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
                #dpg.add_input_int(label="", min_value=0,default_value=values[count], width=80, tag=f"M1{j}{i}",step=0)
                dpg.add_input_float(tag=f"M{num}{i}{j}", min_value=0, default_value=values[count+j*row], width=60,label="",step=0)
        count=count+1
    dpg.set_item_width(lab,column*70+20)
    dpg.set_item_height(lab,row*23+35)
    dpg.add_button(label="Transpose",callback=transpose_button_callback,tag=f"T{num}")

def dot_product_button():
    rowA = dpg.get_value("Input1")
    columnA  = dpg.get_value("Input2")
    rowB = dpg.get_value("Input3")
    columnB = dpg.get_value("Input4")
    if(dpg.does_item_exist("Result")):
        dpg.delete_item("Result")
    if(rowA*columnA*rowB*columnB != 0 and columnA == rowB):
        values = dot_product(rowA,rowB,columnB)
        with dpg.child_window(label="Result", width=columnB*70+30, height=rowA*25+35, tag="Result",parent="Primary Window"):
            dpg.add_text("Multiply")
            create_answer_matrix(rowA,columnB,values)
    else:
        with dpg.child_window(label="Result", width=300, height =35, tag="Result",parent="Primary Window"):
            dpg.add_text("Matrix dimensions can not be multiplied")

def dot_product(rowA,rowB,columnB):
    values = []
    rowA_count = 0
    while rowA_count < rowA:
        columnB_count = 0
        while columnB_count < columnB:
            iterator = 0
            sum = 0
            while iterator < rowB:
                sum = sum + (dpg.get_value(f"M1{rowA_count}{iterator}") * dpg.get_value(f"M2{iterator}{columnB_count}"))
                iterator = iterator+1
            columnB_count = columnB_count+1
            values.append(sum)
        rowA_count = rowA_count+1
    return values

def create_answer_matrix(row,column,values):
    count = 0
    for i in range(row):
        with dpg.group(horizontal=True):
            for j in range(column):
                dpg.add_input_float(tag=f"DP{i}{j}", min_value=0, default_value=values[count], width=60,label="",step=0)
                count = count+1 

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
        dpg.add_text("Matrix 2",tag="begM2")
        dpg.add_input_int(label="Rows", default_value=0, width=80, tag="Input3",min_value=0)
        dpg.add_input_int(label="Columns", default_value=0,  width=80, tag="Input4", min_value=0)
        '''no increment buttons
        with dpg.group(horizontal=True):
            dpg.add_input_int(label="Rows", default_value=0, width=30, tag="Input3",min_value=0,step=0)
            dpg.add_input_int(label="Columns", default_value=0,  width=30, tag="Input4", min_value=0,step=0)
        '''
        dpg.add_button(label="Set Matrix 2 Size", callback=set_matrix_button_callback,tag="B2")
        
        dpg.add_button(label="Multiply", callback=dot_product_button,tag="DPB")

    #create and name of the primary window viewport
    dpg.create_viewport(title='Matthew\'s Magnificent Matrix Machine', width=1000, height=800)
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
