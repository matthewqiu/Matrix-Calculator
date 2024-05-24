def set_matrix_button_callback1():
    lab = "Matrix1"
    row = dpg.get_value("Input1")
    column = dpg.get_value("Input2")
    if(dpg.does_item_exist(lab)):
        dpg.delete_item(lab)
    with dpg.child_window(label="Matrix 1 input", width=200, height =100, tag=lab,parent="Primary Window", before="begM2"):
        for i in range(row):
            with dpg.group(horizontal=True):
                for j in range(column):
                    #for integer only inputs
                    #dpg.add_input_int(label="", min_value=0,default_value=0, width=80, tag=f"M1{i}{j}",step=0)
                    dpg.add_input_float(tag=f"M1{i}{j}", min_value=0, default_value=0, width=60,label="",step=0)
        dpg.set_item_width(lab,column*70+20)
        dpg.set_item_height(lab,row*23+35)
        dpg.add_button(label="Transpose",callback=transpose_button_callback)

def set_matrix_button_callback2():
    lab = "Matrix2"
    row = dpg.get_value("Input3")
    column = dpg.get_value("Input4")
    if(dpg.does_item_exist(lab)):
        dpg.delete_item(lab)
    with dpg.child_window(label="Matrix 2 input", width=200, height =100, tag=lab,parent="Primary Window"):
        for i in range(row):
            with dpg.group(horizontal=True):
                for j in range(column):
                    #for integer only inputs
                    #dpg.add_input_int(label="", min_value=0,default_value=0, width=80, tag=f"M2{i}{j}",step=0)
                    dpg.add_input_float(tag=f"M2{i}{j}", min_value=0, default_value=0, width=60,label="",step=0)
        dpg.set_item_width(lab,column*70+20)
        dpg.set_item_height(lab,row*23+35)
        dpg.add_button(label="Transpose",callback=transpose_button_callback2,user_data=2)