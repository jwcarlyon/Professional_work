#This is a GUI run by a jupyter notebook file. This example will produce a
# range of colormaps for the
#Python/HTML/CSS written by Joseph Carlyon with a few public libraries
#FOR HELP UNDERSTANDING CONTENT:
# --- USER GUIDES --- #
# https://ipywidgets.readthedocs.io/en/latest/user_guide.html
# ^^^ ipywidgets explained hopefully in a clear way ^^^
#
# https://astronautweb.co/snippet/font-awesome/
# ^^^ widgets have style properties. like a check mark or warning sign. this is a list of CSS names which are built in to widgets
# note that any icon or name you chose must be edited to remove the first 2 letters 'fa'. so 'fa-ok' becomes 'ok'
#
#https://docs.python.org/3/library/os.html
#^^^os is used to access the filesystem
# --- USER GUIDES --- #

import importlib_resources #this reqired (pip install importlib_resources) command in my windows 10 terminal
import os#This libray allows us to access the filesystem and read/write information
import ipywidgets as wgts # a library of fxns that provides visual objects for a user to interact with -
import numpy as np #for mathematical functions - put very simply
from IPython.display import display, clear_output
#this imports 2 commands which can change the visual readout of the user's program state in a jupyter cell

import Helper_fxns as helper #Written by Joseph Carlyon - all above libraries are publicly available

class read():
    def __init__(self, arg1 = "fortran_assets/PPM2F-05-28-20-flags.f"):
        self.reading_file = arg1
        self.working_file = ''
        self.preprocessor_flags = ''
        self.srend_file = ''
        self.o2_file = ''
        self.analysis_file = ''
reader = read()
#this creates a space for the name of our file

class text_object():
    def __init__(self, key, iscomments, catch = None):
        self.output_list = []
        self.iscomments = iscomments
        self.description = key
        self.text = wgts.Text(value = helper.get_flag_value(reader.reading_file, key), description = key, description_tooltip = 'update')
        self.text.observe(self.update_all, 'value')
        self.output_list.append(self.text)
        self.banner = wgts.HTML(value = "<p><ul><li><b>{}</b></li></ul></p>".format(self.description))
        self.obj_data = wgts.VBox(children = [self.banner, self.text])

        if not helper.comment_bool(helper.get_flag_value(reader.reading_file, key)):
            #set 'children of VBox to be an HTML and a Text line'
            if self.iscomments:
                comments =  helper.get_comments(reader.reading_file, key)
            self.value =  helper.get_flag_value(reader.reading_file, key)
            self.text.value = self.value
            self.text.description = key

            if self.iscomments and comments[0] != '!':
                #print("butt0 should work")
                self.comms = wgts.HTML(value = comments)
                self.butt0 = wgts.Button(description = 'Hide comments', disabled = False, button_style = 'info', icon = 'indent')
                self.obj_data = wgts.HBox(children = [wgts.VBox(children = [self.banner, self.text, self.butt0]), self.comms])
                self.butt0.on_click(self.handle_butt0)
                self.butt0_logic = True
                self.handle_butt0(None)

    def handle_butt0(self, obj):
        if self.butt0_logic:
            self.obj_data = wgts.HBox(children = [wgts.VBox(children = [self.banner, self.text]), self.butt0])
            self.butt0.description = 'Show comments'
            self.butt0.icon = 'outdent'
            self.butt0_logic = False
        else:
            self.obj_data = wgts.HBox(children = [wgts.VBox(children = [self.banner, self.text, self.butt0]), self.comms])
            self.butt0.icon = 'indent'
            self.butt0.description = 'Hide comments'
            self.butt0_logic = True

    def add_widget(self, widget):
        #this function takes a widget and adds it to the display list
        if self.iscomments:
            self.obj_data =  wgts.HBox(children = [wgts.VBox(children = [self.banner, self.text, widget, self.butt0]), self.comms])
            self.output_list = [self.text, widget]
            widget.observe(self.update_all, 'value')
        else:
            self.obj_data = wgts.VBox(children = [self.banner, self.text, widget])
            self.output_list = [self.text, widget]
            widget.observe(self.update_all, 'value')

    def detach_widgets(self):
        #this function seems useless. It should return the detached widget
        if self.iscomments:
            self.obj_data =  wgts.HBox(children = [wgts.VBox(children = [self.banner, self.text, self.butt0]), self.comms])
            #self.output_list = [self.text, widget]

            #self.link_objects = wgts.dlink((widget, 'value'), (self.text, 'value'))
        else:
            self.obj_data = wgts.VBox(children = [self.banner, self.text])
            #self.output_list = [self.text, widget]
            #widget.observe(self.update_all, 'value')
            #self.link_objects = wgts.dlink((widget, 'value'), (self.text, 'value'))

    def update_all(self, value):
        #print("!!!Debug, trying to understand what gets passed in. value({})".format(value))
        #!!!Debug, trying to understand what gets passed in - an object.
        # below is a FloatSlider-change object. info we want can be accessed
        # as follows - value['new'] - or - value['owner'].value

        # value({'name': 'value', 'old': 0.0, 'new': 0.2,
        # 'owner': FloatSlider(value=0.2, continuous_update=False,
        # description='Opacity value - end', max=1.0, readout_format='.4'),
        # 'type': 'change'})
        if helper.is_int(str(value)) or helper.is_float(str(value)):
            for x in self.output_list:
                if x.description_tooltip == 'update':
                    try:
                        x.value = value
                    except:
                        try:
                            x.value = float(value)
                        except:
                            try:
                                x.value = int(value)
                            except:
                                try:
                                    x.value = str(value)
                                except:
                                    print("update errored out, value: ({})\nOutput_list: ({})".format(value, self.output_list))
                                    pass

    def get_description(self):
        return self.description

    def get_value(self):
        return self.text.value

    def get_iscomm(self):
        return self.iscomments

class slider_object(text_object):#why do I have to call text_object again?
    #This is an example of inheiritance in python 3.x
    # by calling text object we indicate text_object is the parent class
    def __init__(self, key, iscomments, type):
        super(slider_object, self).__init__(key, iscomments)#what is super?
        #so, super(...) is a reference to the parent class
        # by adding ".__init(...)" we call the constructor for a text_object
        # this is how you specify those initializer values and allow our child class
        # to call methods which belong to that text_object - these methods don't
        # have to be declared in any other way - this would over-write the original method...
        spec = type.split() #"int 255 0 1 vertical"
        description = self.get_description()
        if spec[0] == 'float':
            self.linked_slider = wgts.FloatSlider(value = 0.0, min = float(spec[2]), max = float(spec[1]), step = float(spec[3]), description = description, description_tooltip = 'update', disabled = False, continuous_update = False, orientation = spec[5], readout = True, readout_format = spec[4])
        elif spec[0] == 'int':
            self.linked_slider = wgts.IntSlider(value = 15, min = int(spec[2]), max = int(spec[1]), step = int(spec[3]), description = description, description_tooltip = 'update', disabled = False, continuous_update = False, orientation = spec[4], readout = True, readout_format = 'd')
        else:
            self.linked_slider = wgts.IntSlider(value = 15, min = 0, max = 255, step = 5, description = description, description_tooltip = 'update', disabled = False, continuous_update = False, orientation = 'horizontal', readout = True, readout_format = 'd')

        self.linked_slider.observe(self.update_all, 'value')
        self.add_widget(self.linked_slider)

    def get_description(self):
        return super(slider_object, self).get_description()

    def update_all(self, obj):
        #note this function is linked to data-holding widgets within this class [text, slider]
        # this overrides this original update_all as well - can be observed by uncommenting the print line below
        # my menu will have a user update a value in any data-holding widget -
        # then that object will call update_all with an object as below
        # obj = {'name': 'value', 'old': '!!!none found', 'new': '0.0', 'owner': Text(value='0.0', description='Alpha Color value', description_tooltip='update'), 'type': 'change'}
        # this will be handled with a logic which checks for an inevitable redundant call
        # to update_all because using the ".observe" method this way causes a recursive event loop
        #print("debugging obj: ({})".format(obj))
        try:
            valid = False
            for x in self.output_list:
                if(str(obj['new']) != str(x.value)):
                    valid = True
            if valid:
                super(slider_object, self).update_all(obj['new'])
        except:
            super(slider_object, self).update_all(obj)
            #these super(...) reference the object from the constructor call in __init__
            # so the original update_all method still exists and is called in either case
            # when called with obj['new'] we assume the observe function has passed
            # a dictionary type variable in as obj. This will cause an error if
            # the menu updates the text by calling update_all(float_type).
            # except will catch that error and simply call the original funciton
            # while treating the obj variable as a floating point value

    def detach_slider(self):
        self.detach_widgets()
        return self.linked_slider

    def value(self):
        return self.text.value

class pre_menu0():
    def __init__(self):
        #This menu decides where to send the user in our program
        # rerender or not, basically.

        self.exp0 = wgts.HTML(value = ("<h1>Set-Up Menu</h1><p>Please select a mode</p>"))
        self.exp1 = wgts.HTML(value = ("<h2>Rerender mode</h1><p>isrerender defaults to 1,<br>also tweaking of colormaps</p>"))
        self.exp2 = wgts.HTML(value = ("<h2>Non-rerender mode</h1><p>isrerender defaults to 0,<br>preprocessor flags file set-up only</p>"))

        self.butt0 = wgts.Button(description = 'Non-rerender',disabled=False,button_style='info',icon='check')
        self.butt1 = wgts.Button(description = 'Rerender',disabled=False,button_style='info',icon='check')
        self.mode0 = wgts.VBox([self.exp1, self.butt1])
        self.mode1 = wgts.VBox([self.exp2, self.butt0])

        self.butt0.on_click(self.handle_submit0)
        self.butt1.on_click(self.handle_submit1)
        display(self.exp0, self.mode0, self.mode1)

    def handle_submit0(self,obj):
        print("This is a demo. Please select a Rerender session")

    def handle_submit1(self,obj):
        clear_output()
        next_up = pre_menu1(1)

class pre_menu1():
    def __init__(self, rerender):
        #This menu now accepts all the relevant files for a rerender.
        # Add buttons for options and functions to handle the choices

        self.exp0 = wgts.HTML(value = ("<h1>File set-up</h1><p>Please enter the necessary files</p>"))
        #exp0 is meant to explain the flag setting menus
        self.exp1 = wgts.HTML(value = ("<h2>Preprocessor Flag setting mode</h2><p>Please enter a filename."
                                    "<br>These menus cover problem set-up. They ignore other files<br>"
                                    "and allows for a new run to be set up.</p>"))
        self.read0 = wgts.Text(value = reader.reading_file, description = "Flags")

        self.select0 = wgts.Dropdown(options = list(range(1,13)), description = 'Select month:', value = 1)
        self.select1 = wgts.Dropdown(options = list(range(1,32)), description = 'Select day:', value = 1)
        self.select2 = wgts.Dropdown(options = list(range(0,100)), description = 'Select year:', value = 20)
        self.select0.observe(self.update_date)
        self.select1.observe(self.update_date)
        self.select2.observe(self.update_date)

        #self.select0.observe(self.update_colormap, 'value')

        # exp2 should also explain some flag setting menus but should mention tweaking and colormaps
        self.exp2 = wgts.HTML(value = ("<h2>File set up</h2><p>Please enter a filename and select file mode"
                            " No whitespace.<br> This mode sets view point and colormaps.<br>Mode requires"
                            " a few more related files. This mode can be ignored for a normal rerender menu</p>"))

        self.butt0 = wgts.Button(description='Flags setup',disabled=False,button_style='info',icon='check')
        self.butt1 = wgts.Button(description='Srend setup',disabled=False,button_style='info',icon='check')
        self.butt0.on_click(self.handle_submit0)
        self.butt1.on_click(self.handle_submit1)

        self.mode0 = wgts.VBox([self.exp1, self.read0, self.butt0])
        #mode0 needs to lead to menu_normal
        self.mode1 = wgts.VBox([self.exp2, self.select0, self.select1, self.select2, self.read0, self.butt1, self.butt0])
        #mode1 needs to lead question about tweaking or not
        if rerender == 0:
            self.mode_chosen = wgts.HBox([self.mode0])
        else:
            self.mode_chosen = wgts.HBox([self.mode1])


        display(self.exp0, self.mode_chosen)

    def update_date(self, obj):
        #print("Debugging, entered object: {}".format(obj))
        if obj['name'] == 'value':
            if 'day' in obj['owner'].description:
                day = str(obj['new'])
                if len(day) < 2:
                    day = '0' + day
            else:
                day = str(self.select1.value)
                if len(day) < 2:
                    day = '0' + day
            if 'month' in obj['owner'].description:
                month = str(obj['new'])
                if len(month) < 2:
                    month = '0' + month
            else:
                month = str(self.select0.value)
                if len(month) < 2:
                    month = '0' + month
            if 'year' in obj['owner'].description:
                year = str(obj['new'])
                if len(year) < 2:
                    year = '0' + year
            else:
                year = str(self.select2.value)
                if len(year) < 2:
                    year = '0' + year
            self.read0.value = "PPM2F-{}-{}-{}-flags.f".format(month, day, year)

    def handle_submit0(self,obj):
        print("This is a demo. Please select the Srend file type.")

    def handle_submit1(self, obj):
        #this is a new datatype to condense the definition for simple text entries and labels
        try:
            os.mkdir("output")
        except FileExistsError:
            pass
        if(os.path.isfile((os.getcwd()) + '/' + self.read0.value)):
            clear_output()
            self.read1 = text_object("DataAnalysis", False)
            self.read2 = text_object("O2", False)
            self.read3 = text_object("srend.F90", False)

            self.read1.text.on_submit(self.handle_submit2)
            self.read2.text.on_submit(self.handle_submit2)
            self.read3.text.on_submit(self.handle_submit2)

            date = "{}-{}-{}".format(self.read0.value.split('-')[1], self.read0.value.split('-')[2], self.read0.value.split('-')[3])
            self.read1.text.value = "PPM2F-{}-DataAnalysis.f".format(date)
            self.read2.text.value = "PPM2F-{}-O2.f".format(date)
            self.read3.text.value = "srend.F90"

            display(self.exp0, self.read1.obj_data, self.read2.obj_data, self.read3.obj_data)
        else:
            print("Preprocessor was not found, please ensure no whitespace in the path and correct filepath in choice: {}".format(self.read0.description))

    def handle_submit2(self, obj):
        if (os.path.isfile((os.getcwd()) + '/' + self.read1.text.value)):
            if (os.path.isfile((os.getcwd()) + '/' + self.read2.text.value)):
                if (os.path.isfile((os.getcwd()) + '/' + self.read3.text.value)):
                    reader.analysis_file = self.read1.text.value
                    reader.o2_file = self.read2.text.value
                    reader.srend_file = self.read3.text.value
                    clear_output()
                    next_up = menu_tweaking_session0()
                else:
                    print("Could not find file: {} in entry {}".format(self.read3.text.value, self.read3.description))
            else:
                print("Could not find file: {} in entry {}".format(self.read2.text.value, self.read2.description))
        else:
            print("Could not find file: {} in entry {}".format(self.read1.text.value, self.read1.description))

    def handle_file_change(self, obj):
        if obj.change['new'] != self.read0.value:
            print("debugging values\n obj.change['new']: {}\n self.read0.value {}".format(obj.change['new'], self.read0.value))
            self.read0.value = obj.change['new']
        else:
            print("No change debugging values\n obj.change['new']: {}\n self.read0.value {}".format(obj.change['new'], self.read0.value))

class pre_menu2():
    def __init__(self):
        #establish if this is a tweaking session
        self.exp0 = wgts.HTML(value = "<h1>Postprocessing session set-up</h1><p></p>")
        if helper.is_int(helper.get_flag_value(reader.preprocessor_flags, "istweaking")):
            self.tweaking = text_object("istweaking", True)
            #print("Found tweak flag")
            #wgts.Text(description = "istweaking", value = helper.get_flag_value(reader.preprocessor_flags, "istweaking"))
        else:
            self.tweaking = text_object("istweaking", True)
            #print("Not found tweak flag")
        self.tweaking.update_all("1")
        self.setup_comments(self.tweaking)

        self.butt0 = wgts.Button(description = 'Moms Data', disabled = False, button_style = 'info', icon = 'drink')
        self.butt1 = wgts.Button(description = 'Rerender', disabled = False, button_style = 'info', icon = 'drink')

        self.butt0.on_click(self.handle_butt0)
        self.butt1.on_click(self.handle_butt1)

        display(self.exp0, self.tweaking.obj_data, self.butt0, self.butt1)

    def handle_butt0(self, obj):
        #moms
        clear_output()
        print("Can we do a moms data processing rerender?")
        next_up = menu_moms0()

    def handle_butt1(self, obj):
        #rerender
        #clear_output()
        valid = True
        if not((self.tweaking.get_value() == "1") or (self.tweaking.get_value() == "0")):
            valid = False
            print("istweaking requires an integer value of 1 or 0")
        if valid:
            self.write_submission()
            next_up = menu0()

    def handle_butt2(self, obj):
        clear_output()
        display(self.exp0, self.tweaking.obj_data, self.butt0, self.butt1)

    def write_submission(self):
        if helper.is_int(helper.get_flag_value(reader.preprocessor_flags, "istweaking")):
            #our flags file is up to date, update the file with the user's tweaking method and move on
            # copy everything until istweaking
            data = helper.copy_until_from(reader.preprocessor_flags, "istweaking", )#imporant that this last argument is blank
            data += "\n#define istweaking {}\n".format(self.tweaking.get_value())
            data += helper.copy_after(reader.preprocessor_flags, "istweaking")
            #data is now an updated copy of the flags file
            helper.new_file_plus(reader.preprocessor_flags, "output/updated_flags.f", [], data)
            #new_file_plus, when entered like this, simply gives us a new file with the
            # lines copied into data. First argument is not checked, second is the new file name
            # and data is hopefully a carbon copy of the original with the user's value for istweaking

            reader.preprocessor_flags = "output/updated_flags.f"
            #print("debugging")
            clear_output()

        else:
            helper.new_file_plus(reader.preprocessor_flags, "updated_flags.f", ["mmdumpincr", "isstereo"] ,"#define istweaking {}\n".format(self.tweaking.get_value()))
            #this function simply makes a new copy of the file in a folder called "output" filename: updated_flags.f
            # the new file will have a definition for istweaking based off whatever the user selects
            reader.preprocessor_flags = "output/updated_flags.f" #now the program will only read from our new file
            clear_output()

    def setup_comments(self, txt_obj):
        if txt_obj.iscomments:
            try:
                txt_obj.butt0.on_click(self.handle_butt2)
            except AttributeError:
                print("comments were not found for {}".format(txt_obj.get_description()))

class menu_tweaking_session0():
    def __init__(self, num = 0):
        #display colormap default at 701 if it exists
        #(self.indexes, self.alpha_knots, self.rbg_knots, self.dicts) = helper.get_colormaps(reader.srend_file)
        (self.indexes, self.dicts) = helper.get_colormaps(reader.srend_file)
        #this tuple contains a list of all start and end points for colormaps inside indexes
        # dicts holds all the vectors - recallable by map number as a string value ex. '799'
        self.sREND_COTAB_KEYS = helper.get_flag_value(reader.preprocessor_flags, "SREND_COTAB_KEYS")
        default_map = False
        self.rgb_source, self.alpha_source = "", ""
        self.alpha_colormap, self.rgb_colormap = "", ""
        #self.img_rgb, self.img_alpha = wgts.Image(), wgts.Image()
        self.cmap_a_indexes = []
        self.cmap_rgb_indexes = []

        alpha_indexes = list(map(lambda x : "num({})to({})".format(x[0][0], x[0][1]), self.indexes))
        rgb_indexes = list(map(lambda x : "num({})to({})".format(x[1][0], x[1][1]), self.indexes))
        #these create the lists of ranges which are predefined in select0 and 1

        self.alpha_range = []
        self.rbg_range = []

        for x in range(0,len(self.indexes)):
            if self.indexes[x][0][0] == 701:
                default_map = True


        layout = "float 1.0 0.0 0.1 .4f vertical"
        self.colormap_r = slider_object("R", False, layout)
        self.colormap_b = slider_object("B", False, layout)
        self.colormap_g = slider_object("G", False, layout)
        self.colormap_a = slider_object("Alpha value", False, layout)

        layout = "int 255 0 1 vertical"
        self.colormap_i = slider_object("RGB Color index", False, layout)
        self.colormap_ai = slider_object("Alpha index", False, layout)
        #below are initializations for the sliders - alread linked to the corresponding text object
        # but not included in the .obj_data list. This way the slider can be display separately
        self.slider_i, self.slider_r, self.slider_g, self.slider_b = self.colormap_i.detach_slider(), self.colormap_r.detach_slider(), self.colormap_g.detach_slider(), self.colormap_b.detach_slider()
        self.slider_ai, self.slider_a = self.colormap_ai.detach_slider(), self.colormap_a.detach_slider()
        self.colormap_i_slds = wgts.HBox(children = [self.colormap_i.obj_data, self.colormap_ai.obj_data])
        self.colormap_rn_slds = wgts.HBox(children = [self.colormap_r.obj_data, self.colormap_a.obj_data])

        self.colormap_i.text.on_submit(self.set_user_knot)
        self.colormap_r.text.on_submit(self.set_user_knot)
        self.colormap_b.text.on_submit(self.set_user_knot)
        self.colormap_g.text.on_submit(self.set_user_knot)
        self.colormap_a.text.on_submit(self.set_user_knot)
        self.colormap_ai.text.on_submit(self.set_user_knot)


        self.select0 = wgts.Dropdown(options = alpha_indexes, description = 'Alpha presets:', description_tooltip = 'alpha')
        self.select1 = wgts.Dropdown(options = rgb_indexes, description = 'RGBA presets:')
        #these hold the start and end knot index numbers of all maps
        #these are just for selecting a new size for the user color maps
        self.select4 = wgts.Dropdown(options = list(range(1, 11)), value = 1, description = 'Alpha_knot #:', description_tooltip = 'alpha')
        self.select5 = wgts.Dropdown(options = list(range(1, 11)), value = 1, description = 'RBG_knot #:', description_tooltip = 'rbg')

        self.select0.observe(self.update_default_range, 'value')
        self.select1.observe(self.update_default_range, 'value')
        self.select4.observe(self.knot_select, 'value')
        self.select5.observe(self.knot_select, 'value')

        #the following is for building HTML code to display colormap as vector arrays
        self.rows0, self.rows1, self.rows2, self.rows3, self.user_rows0, self.user_rows1 = "", "", "", "", "", ""
        self.html_maps0 = ("<!DOCTYPE html>"
                            "<html lang = 'en'>"
                            "  <head><style type='text/css'>"
                            "  table{width: 100%;border: thin solid black;}"
                            "  th,td{color: black;border: thin solid black;}</style>"
                            "<script>"
                            "  var opy,iny,r,b,g;"
                            "  window.onload=function(){"
                            "    opy=document.getElementById('opacity').innerHTML;"
                            "    iny=document.getElementById('intensity').innerHTML;"
                            "    r=document.getElementById('r').innerHTML;"
                            "    b=document.getElementById('b').innerHTML;"
                            "    g=document.getElementById('g').innerHTML;"
                            "    document.getElementById('colour').style.backgroundColor = 'rgb(255, 99, 71)';"
                            "  };"
                            "</script></head>"
                            "  <body>"
                            "    <h3>Retrieved values from srend</h3>"
                            "    <p>This shows any range of knots already written in the srend.F90 file for reference</p>"
                            "    <table>"
                            "      <tr><th>Knot #</th><th>Alpha Index</th><th>Alpha</th></tr>")
        #our update fxn will add in rows from dictionary values
        self.html_maps1 = "</table><table><tr><th>Knot #</th><th>Color Index</th><th>R</th><th>G</th><th>B</th></tr>"
        self.html_maps2 = "</table></body></html>"
        self.html_user_maps0 = ("<!DOCTYPE html>"
                            "<html lang = 'en'>"
                            "  <head><style type='text/css'>"
                            "  table{width: 100%;border: thin solid black;}"
                            "  th,td{color: black;border: thin solid black;}</style>"
                            "<script>"
                            "  var opy,iny,r,b,g;"
                            "  window.onload=function(){"
                            "    opy=document.getElementById('opacity').innerHTML;"
                            "    iny=document.getElementById('intensity').innerHTML;"
                            "    r=document.getElementById('r').innerHTML;"
                            "    b=document.getElementById('b').innerHTML;"
                            "    g=document.getElementById('g').innerHTML;"
                            "    document.getElementById('colour').style.backgroundColor = 'rgb(255, 99, 71)';"
                            "  };"
                            "</script></head>"
                            "  <body>"
                            "    <h3>User colormap</h3>"
                            "    <p>These data are to be set by the user. The map size is selectable by dropdown for both alpha and rgba knots. Select which knot to alter with the 'Current knot' dropdown, then adjust with the sliders or use the text box. Copy and paste is encouraged. If the knot value is correct, press the 'Update Knot' button to set the custom value and move on.</p>"
                            "    <table>"
                            "      <tr><th>Knot #</th><th>Alpha Index</th><th>Alpha</th></tr>")
        self.html_user_maps1 = "</table><table><tr><th>Knot #</th><th>Color Index</th><th>R</th><th>G</th><th>B</th></tr>"
        self.html_user_maps2 = "</table></body></html>"

        self.exp0 = wgts.HTML(value = "<h1>Color Map Menu</h1><p>This menu will help setup colormaps by creating a new srend.F90 file. Colormaps 701 up to 710 will be replaced with the user table below. Press continue to move on to the final colormap (790 - 799). The 1st table below is for your reference, the next tracks the values of your custom colormap</p>")

        self.exp1 = wgts.HTML(value = self.html_maps0 + self.rows0 + self.html_maps1 + self.rows1 + self.html_maps2)
        self.exp2 = wgts.HTML(value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2)
        #.format(self.colormap_r.text.value, self.colormap_g.text.value, self.colormap_b.text.value, self.colormap_a.text.value, self.colormap_ai.text.value))

        self.butt0 = wgts.Button(description = 'Copy complete alpha map', description_tooltip = "alpha", disabled = False, button_style = 'danger', icon = 'drink')
        self.butt1 = wgts.Button(description = 'Copy complete rgb map', disabled = False, button_style = 'danger', icon = 'drink')
        self.butt2 = wgts.Button(description = 'Alter alpha knot', description_tooltip = "alpha", disabled = False, button_style = 'danger', icon = 'drink')
        self.butt3 = wgts.Button(description = 'Alter rgb knot', disabled = False, button_style = 'danger', icon = 'drink')
        self.butt4 = wgts.Button(description = 'Accept Map', disabled = False, button_style = 'success', icon = 'drink')
        self.butt5 = wgts.Button(description = 'Display maps', disabled = False, button_style = 'info', icon = 'drink')
        self.butt0.on_click(self.copy_default_map)
        self.butt1.on_click(self.copy_default_map)
        self.butt2.on_click(self.set_user_knot)
        self.butt3.on_click(self.set_user_knot)
        self.butt4.on_click(self.handle_butt4)
        self.butt5.on_click(self.display_maps)

        self.select_ranges = wgts.HBox(children = [wgts.VBox(children = [self.select0, self.butt0]), wgts.VBox(children = [self.select1, self.butt1])])
        self.user_knot_select = wgts.HBox(children = [self.select4, self.select5])
        self.sliders = wgts.HBox(children = [self.slider_ai, self.slider_a, self.slider_i, self.slider_r, self.slider_g, self.slider_b, self.butt2, self.butt3])
        self.current_knot = wgts.VBox(children = [self.colormap_i_slds, self.colormap_rn_slds, self.colormap_g.obj_data, self.colormap_b.obj_data])
        self.knot_index = 0
        self.output_rgb = [(-1, float("NaN"), float("NaN"), float("NaN"), False) for x in range(0, 10)]
        self.output_alpha = [(-1 ,float("NaN"), False) for x in range(0, 10)]
        self.colormap_dict  = {'alpha' : [], 'red' : [], 'green' : [], 'blue' : []}
        #self.ending = wgts.VBox(children = [self.colormap_end_r.obj_data, self.colormap_end_b.obj_data, self.colormap_end_g.obj_data, self.colormap_end_o.obj_data, self.colormap_end_i.obj_data, self.colormap_end_oi.obj_data])
        #find colormap
        display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))
        if default_map:
            self.select0.value, self.select1.value = "num(701)to(709)", "num(701)to(709)"
            #self.select2, self.select3 = 10, 10

        #setting these values will call display
    def display_maps(self, obj):
        #self.show_map(self.original_alpha)
        self.show_map(self.output_alpha)
        #self.show_map(self.original_rgb)
        self.show_map(self.output_rgb)

    def show_map(self, cmap):
        #we need to enforce that there are at least 2 valid knots
        # this function is technically generic and the logic is
        # a dispatch algorithm
        i = 0
        if len(cmap[0]) == 5:
            for x in cmap:
                if x[4]:
                    i += 1
            if i > 1:
                self.rgb_colormap = helper.create_ppm_cmap(cmap, self.rgb_source)
                self.img_rgb = wgts.Image(value = self.rgb_colormap, format = 'jpg')
                display(self.img_rgb)
            else:
                print("RGB colormap too small")
        elif len(cmap[0]) == 3:
            for x in cmap:
                if x[2]:
                    i += 1
            if i > 1:
                self.alpha_colormap = helper.create_ppm_cmap(cmap, self.alpha_source)
                self.img_alpha = wgts.Image(value = self.alpha_colormap, format = 'jpg')
                display(self.img_alpha)
            else:
                print("Alpha colormap too small")
        else:
            print("invalid colormap({})".format(cmap))

    def knot_select(self, obj):
        if(obj.owner.description_tooltip) == 'alpha':
            #print("debugging, set knot vector: {}".format(self.output_alpha[self.select4.value - 1]))
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td></tr>"
            knot_num = 1
            self.user_rows0 = ""
            for x in self.output_alpha:
                if x[2]:
                    if knot_num == self.select4.value:
                        self.user_rows0 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1])
                        self.colormap_ai.update_all(x[0])
                        self.colormap_a.update_all(x[1])
                    else:
                        self.user_rows0 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1])
                knot_num += 1
            #self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2

        else:
            #rgb_vector = ((self.colormap_i.get_value()), (self.colormap_r.get_value()), (self.colormap_g.get_value()), (self.colormap_b.get_value()))
            #self.output_rgb[self.select5.value - 1] = rgb_vector
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>"
            knot_num = 1
            self.user_rows1 = ""
            for x in self.output_rgb:
                if x[4]:
                    if knot_num == self.select5.value:
                        self.user_rows1 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                        self.colormap_r.update_all(x[1])
                        self.colormap_g.update_all(x[2])
                        self.colormap_b.update_all(x[3])
                        self.colormap_i.update_all(x[0])
                    else:
                        self.user_rows1 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                knot_num += 1
        self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2
        clear_output()
        display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))

    def set_user_knot(self, obj):
        if ('alpha' in (obj.description)) or ('Alpha' in (obj.description)):
            #set user alpha knot for the current value being viewed - self.output_alpha @ self.select2.value
            #index_a = int(self.select0.options.index(self.select0.value))
            #(-1 ,float("NaN"), False)
            alpha_vector = (int(self.colormap_ai.get_value()), float(self.colormap_a.get_value()), True)
            self.output_alpha[self.select4.value - 1] = alpha_vector
            # take the list and create an html formatted lists
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td></tr>"
            #print("debugging, set knot vector: {}".format(self.output_alpha[self.select4.value - 1]))
            knot_num = 701
            self.user_rows0 = ""
            for x in self.output_alpha:
                if x[2]:
                    if knot_num == self.select4.value:
                        self.user_rows0 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1])
                    else:
                        self.user_rows0 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1])
                knot_num += 1

        else:
            rgb_vector = (int(self.colormap_i.get_value()), float(self.colormap_r.get_value()), float(self.colormap_g.get_value()), float(self.colormap_b.get_value()), True)
            self.output_rgb[self.select5.value - 1] = rgb_vector
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>"
            knot_num = 701
            self.user_rows1 = ""
            for x in self.output_rgb:
                if x[4]:
                    if knot_num == self.select5.value:
                        self.user_rows1 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                    else:
                        self.user_rows1 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                knot_num += 1
        #this loop sets the html for exp1 to read out the relevant datas
        self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2
        clear_output()
        display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))
        self.display_maps(None)

    def copy_default_map(self, obj):
        #This function will set user knots to values from the srend table
        if(obj.description) == 'Copy complete alpha map':
            difference = len(self.output_alpha) - len(self.alpha_colormap)
            if difference > 0:
                #this means that our output alpha has multiple unused vectors
                for x in range(difference):
                    self.output_alpha[-(x + 1)] = (self.output_alpha[-(x + 1)][0], self.output_alpha[-(x + 1)][1], False)
                    #print("debugging output_alpha: index({}) and vector({})".format(-(x + 1), self.output_alpha[-(x + 1)]))
            elif(difference < 0):
                #this means the default colormap is longer than our pre-set array in self.output_alpha
                # This is no longer allowed. Print an error message
                print("Desired colormap is longer than the allotted 10 knots.\nPlease use copy and paste to enter values or pick a shorter map")
                return
                '''
                output = [(-1 ,float("NaN"), False) for x in range(len(self.alpha_colormap))]
                for x in range(len(self.output_alpha)):
                    output[x] = self.output_alpha[x]
                self.output_alpha = output
                #self.select2.options = range(2, len(self.output_alpha) + 1)
                #self.select4.options = range(1, len(self.output_alpha) + 1)

                #print("debugging output_alpha: length({})".format(len(self.output_alpha)))
                '''
            self.alpha_source = "alpha-{}".format(self.select0.value)
            for x in range(0, len(self.alpha_colormap)):
                self.output_alpha[x] = (self.alpha_colormap[x][0] ,self.alpha_colormap[x][1], True)
                #set each vector within self.output_alpha to the corresponding value in self.alpha_colormap
                #print("debugging alpha_colormap: index({}) and vector({})".format(x, self.alpha_colormap[x]))
            self.user_rows0 = ""
            for x in range(0, 10):
                #print("Debug, user row defined: {}, i{}, a{}".format((x + 1), self.output_alpha[x][0], self.output_alpha[x][1]))
                if self.output_alpha[x][2]:
                    self.user_rows0 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), str(self.output_alpha[x][0]).split('.')[0], self.output_alpha[x][1])
                    #print("debugging output true false: num({}) output_alpha@x({})".format(x, self.output_alpha[x]))
                    #self.user_rows1 += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), self.output_rgb[x][0], self.output_rgb[x][1], self.output_rgb[x][2], self.output_rgb[x][3])
                #else:
                    #print("debugging output true false: num({}) output_alpha@x({})".format(x, self.output_alpha[x]))
        else:
            #set each vector within self.output_rgb to the corresponding value in self.rgb_colormap
            difference = len(self.output_rgb) - len(self.rgb_colormap)
            if difference > 0:
                #this means that our output alpha has multiple unused vectors
                for x in range(difference):
                    self.output_rgb[-(x + 1)] = (self.output_rgb[-(x + 1)][0], self.output_rgb[-(x + 1)][1],  self.output_rgb[-(x + 1)][2], self.output_rgb[-(x + 1)][3], False)
                    #print("debugging rgb_colormap: index({}) and vector({})".format(x, self.rgb_colormap[x]))
                    #print("debugging output_alpha: index({}) and vector({})".format(-(x + 1), self.output_alpha[-(x + 1)]))
            elif(difference < 0):
                #this means the default colormap is longer than our pre-set array in self.output_alpha
                # No longer allowed. Error message
                print("Desired colormap is longer than the allotted 10 knots.\nPlease use copy and paste to enter values or pick a shorter map")
                return
                '''
                output = [(-1 ,float("NaN"), float("NaN"), float("NaN"), False) for x in range(len(self.rgb_colormap))]
                for x in range(len(self.output_rgb)):
                    output[x] = self.output_rgb[x]
                self.output_rgb = output
                #self.select3.options = range(2, len(self.output_rgb) + 1)
                self.select5.options = range(1, len(self.output_rgb) + 1)

                #print("debugging output_rgb: length({})".format(len(self.output_rgb)))
                '''
            self.rgb_source = "rgb-{}".format(self.select1.value)
            for x in range(0, len(self.rgb_colormap)):
                self.output_rgb[x] = (self.rgb_colormap[x][0], self.rgb_colormap[x][1], self.rgb_colormap[x][2], self.rgb_colormap[x][3], True)
                #set each vector within self.output_alpha to the corresponding value in self.alpha_colormap
                #print("debugging rgb_colormap: index({}) and vector({})".format(x, self.rgb_colormap[x]))
            self.user_rows1 = ""
            for x in range(0, 10):
                #print("Debug, user row defined: {}, i{}, a{}".format((x + 1), self.output_alpha[x][0], self.output_alpha[x][1]))
                if self.output_rgb[x][4]:
                    self.user_rows1 += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), str(self.output_rgb[x][0]).split('.')[0], self.output_rgb[x][1], self.output_rgb[x][2], self.output_rgb[x][3])
                    #self.user_rows0 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), self.output_alpha[x][0], self.output_alpha[x][1])
                    #print("debugging output true false: num({}) output_rgb@x({})".format(x, self.output_rgb[x]))
                #else:
                    #print("debugging output true false: num({}) output_rgb@x({})".format(x, self.output_rgb[x]))


        self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2
        clear_output()
        display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))

    def update_default_range(self, obj):
        #call update_maps with the location of the start and end indexes
        # and 2 dictionaries for the different values
        #print("Debug: passed in object to update colormap({})\nalso here are select keys({})".format(obj, self.select0.keys))
        index_a = int(self.select0.options.index(self.select0.value))
        index_rgb = int(self.select1.options.index(self.select1.value))
        start_a = self.indexes[index_a][0]
        start_rbg = self.indexes[index_rgb][1]
        #Use index for displaying which range of rgba or alpha knots to be altered
        if(obj.owner.description_tooltip) == 'alpha':
            #alpha_map_len = (self.indexes[index_a][0][1] - self.indexes[index_a][0][0])
            #self.select2.options = list(range(self.indexes[index_a][0][1] - (self.indexes[index_a][0][0])))
            self.alpha_source = "alpha-{}".format(self.select0.value)
            self.rows0 = ""
            #row2 as well needs to be handled
            self.alpha_colormap = []
            for x in range(start_a[0], (start_a[1] + 1)):
                #print("debugging alpha here is dict key: ({})\nstart({})\nmax({})".format(x, self.indexes[index_a][0][0], self.indexes[index_a][0][1]))
                #x is an dictionary index
                knot = self.dicts[0][str(x)]
                self.rows0 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(x, str(knot[0]).split('.')[0], knot[1])
                self.alpha_colormap.append(knot)
            #self.show_colormap(colormap)
        else:
            #rgb_map_len = (self.indexes[index_rgb][1][1] - self.indexes[index_rgb][1][0])
            #self.select3.options = range(self.indexes[index_rgb][1][1] - (self.indexes[index_rgb][1][0]))
            self.rgb_source = "rgb-{}".format(self.select1.value)
            self.rows1 = ""
            #add in script for rows3
            self.rgb_colormap = []
            for x in range(start_rbg[0], (start_rbg[1] + 1)):
                #print("debugging rgb here is dict key: ({})\nstart({})\nmax({})".format(x, self.indexes[index_a][0][0], self.indexes[index_a][0][1]))
                #x is an dictionary index
                knot = self.dicts[1][str(x)]
                self.rows1 += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(x, str(knot[0]).split('.')[0], knot[1], knot[2], knot[3])
                self.rgb_colormap.append(knot)
            #self.num_rgb_knots = len(self.rgb_colormap)
        self.exp1.value = self.html_maps0 + self.rows0 + self.html_maps1 + self.rows1 + self.html_maps2

    def update_user_range(self, obj):
        if obj.owner.description_tooltip == 'alpha':
            #select2.value holds the new maximum number of alpha_knots to display
            # self.output_alpha holds the list of user-defined values
            # self.user_rows0 holds the rows for the alpha table
            self.user_rows0 = ""
            self.colormap_dict['alpha'] = []
            #self.alpha_source = self.select0.value
            #print("debugging length of arrays: {} and {}".format(len(self.output_alpha), len(self.output_rgb)))
            for x in range(0, 10):
                #print("Debug, user row defined: {}, i{}, a{}".format((x + 1), self.output_alpha[x][0], self.output_alpha[x][1]))
                if self.output_alpha[x][2]:
                    self.user_rows0 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), self.output_alpha[x][0], self.output_alpha[x][1])
                    #logic to set self.colormap_dict data to correct format
                    '''if x == 0:
                        self.colormap_dict['alpha'].append([0.0, 0.0, 0.0])
                    elif x == 9:
                        self.colormap_dict['alpha'].append([1.0, 1.0, 1.0])
                    else:
                        self.colormap_dict['alpha'].append([self.output_alpha[x][0], self.output_alpha[x][1], self.output_alpha[x][1]])
                    '''
        else:
            self.colormap_dict['red'], self.colormap_dict['green'], self.colormap_dict['blue'] = [], [], []
            self.user_rows1 = ""
            #self.rgb_source = self.select1.value
            for x in range(0, 10):
                #print("Debug, user row defined : {}, i{}, r{}, b{}, g{}".format((x + 1), self.output_rgb[x][0], self.output_rgb[x][1], self.output_rgb[x][2], self.output_rgb[x][3]))
                if self.output_rgb[x][4]:
                    self.user_rows1 += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), self.output_rgb[x][0], self.output_rgb[x][1], self.output_rgb[x][2], self.output_rgb[x][3])
                    '''if x == 0:
                        self.colormap_dict['red'].append([0.0, 0.0, 0.0])
                        self.colormap_dict['green'].append([0.0, 0.0, 0.0])
                        self.colormap_dict['blue'].append([0.0, 0.0, 0.0])
                    elif x == 9:
                        self.colormap_dict['red'].append([1.0, 1.0, 1.0])
                        self.colormap_dict['green'].append([1.0, 1.0, 1.0])
                        self.colormap_dict['blue'].append([1.0, 1.0, 1.0])
                    else:
                        self.colormap_dict['red'].append([(self.output_rgb[x][0] / 255.0), self.output_rgb[x][1], self.output_rgb[x][1]])
                        self.colormap_dict['green'].append([(self.output_rgb[x][0] / 255.0), self.output_rgb[x][2], self.output_rgb[x][2]])
                        self.colormap_dict['blue'].append([(self.output_rgb[x][0] / 255.0), self.output_rgb[x][3], self.output_rgb[x][3]])
                    '''
        #self.show_colormap(self.output_rgb)
        self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2

    def handle_butt4(self, obj):
        valid = True
        for x in self.output_alpha:
            if x[2]:#this entry in the array is a boolean value
                if not helper.is_int(str(x[0]).split(".")[0]) or not helper.is_float(str(x[1])):
                    valid = False
                    print("!!!Problem knot number({}) vector({})".format(self.output_alpha.index(x), x))
        for x in self.output_rgb:
            if x[4]:#if this is false, the user has selected less knots than the current x
                if not helper.is_int(str(x[0]).split(".")[0]) or not helper.is_float(str(x[1])) or not helper.is_float(str(x[2])) or not helper.is_float(str(x[3])):
                    valid = False
                    print("!!!Problem knot number({}) vector({})".format(self.output_rgb.index(x), x))
        if not helper.is_valid_colormap(self.output_alpha):
            valid = False
            print("!!!Problem with user alpha colormap. Please ensure the indexes begin and end with 0 and 255 respectively.")
        if not helper.is_valid_colormap(self.output_rgb):
            valid = False
            print("!!!Problem with user rgb colormap. Please ensure the indexes begin and end with 0 and 255 respectively.")
        if valid:
            #write_submission
            clear_output()
            print("successful handle submit, first map written")
            next_up = menu_tweaking_session1(self.output_alpha, self.output_rgb, self.select0.value, self.select1.value)

class menu_tweaking_session1():
    def __init__(self, init_map_alpha, init_map_rgb, alpha_range, rbg_range):
        #display colormap default at 701 if it exists
        #(self.indexes, self.alpha_knots, self.rbg_knots, self.dicts) = helper.get_colormaps(reader.srend_file)
        (self.indexes, self.dicts) = helper.get_colormaps(reader.srend_file)
        #this tuple contains a list of all start and end points for colormaps inside indexes
        # dicts holds all the vectors - recallable by map number as a string value ex. '799'
        self.sREND_COTAB_KEYS = helper.get_flag_value(reader.preprocessor_flags, "SREND_COTAB_KEYS")
        default_map = False
        self.cmap_a_indexes = []
        self.cmap_rgb_indexes = []

        alpha_indexes = list(map(lambda x : "num({})to({})".format(x[0][0], x[0][1]), self.indexes))
        rgb_indexes = list(map(lambda x : "num({})to({})".format(x[1][0], x[1][1]), self.indexes))
        #these create the lists of ranges which are predefined in select0 and 1

        self.alpha_range, self.rbg_range, self.alpha_colormap, self.rgb_colormap = [], [], [], []
        self.rgb_source, self.alpha_source = "", ""
        for x in range(0,len(self.indexes)):
            if self.indexes[x][0][0] == 701:
                default_map = True

        layout = "float 1.0 0.0 0.1 .4f vertical"
        self.colormap_r = slider_object("R", False, layout)
        self.colormap_b = slider_object("B", False, layout)
        self.colormap_g = slider_object("G", False, layout)
        self.colormap_a = slider_object("Alpha value", False, layout)

        layout = "int 255 0 1 vertical"
        self.colormap_i = slider_object("RGB Color index", False, layout)
        self.colormap_ai = slider_object("Alpha index", False, layout)
        #below are initializations for the sliders - alread linked to the corresponding text object
        # but not included in the .obj_data list. This way the slider can be display separately
        self.slider_i, self.slider_r, self.slider_g, self.slider_b = self.colormap_i.detach_slider(), self.colormap_r.detach_slider(), self.colormap_g.detach_slider(), self.colormap_b.detach_slider()
        self.slider_ai, self.slider_a = self.colormap_ai.detach_slider(), self.colormap_a.detach_slider()
        self.colormap_i_slds = wgts.HBox(children = [self.colormap_i.obj_data, self.colormap_ai.obj_data])
        self.colormap_rn_slds = wgts.HBox(children = [self.colormap_r.obj_data, self.colormap_a.obj_data])

        self.colormap_i.text.on_submit(self.set_user_knot)
        self.colormap_r.text.on_submit(self.set_user_knot)
        self.colormap_b.text.on_submit(self.set_user_knot)
        self.colormap_g.text.on_submit(self.set_user_knot)
        self.colormap_a.text.on_submit(self.set_user_knot)
        self.colormap_ai.text.on_submit(self.set_user_knot)


        self.select0 = wgts.Dropdown(options = alpha_indexes, description = 'Alpha presets:', description_tooltip = 'alpha')
        self.select1 = wgts.Dropdown(options = rgb_indexes, description = 'RGBA presets:')
        #these hold the start and end knot index numbers of all maps
        #self.select2 = wgts.Dropdown(options = [2,3,4,5,6,7,8,9,10], value = 2, description = 'Alpha total:', description_tooltip = 'alpha')
        #self.select3 = wgts.Dropdown(options = [2,3,4,5,6,7,8,9,10], value = 2, description = 'RGBA total:')
        #these are just for selecting a new size for the user color maps
        len_alpha, len_rgb = 0, 0
        for x in range(0,10):
            if init_map_alpha[x][2]:
                len_alpha += 1
            if init_map_rgb[x][4]:
                len_rgb += 1
        self.select4 = wgts.Dropdown(options = list(range(1, len_alpha + 1)), value = len_alpha, description = 'Alpha_knot #:', description_tooltip = 'alpha')
        self.select5 = wgts.Dropdown(options = list(range(1, len_rgb + 1)), value = len_rgb, description = 'RBG_knot #:', description_tooltip = 'rbg')
        #these are for selecting a user knot to aloter
        #self.select6 = wgts.Dropdown(options = [2,3,4,5,6,7,8,9,10], value = 10, description = 'Modify alpha knot:')
        #self.select7 = wgts.Dropdown(options = [2,3,4,5,6,7,8,9,10], value = 10, description = 'Modify rgb knot:')
        self.select0.observe(self.update_default_range, 'value')
        self.select1.observe(self.update_default_range, 'value')
        #self.select2.observe(self.update_user_range, 'value')
        #self.select3.observe(self.update_user_range, 'value')
        self.select4.observe(self.knot_select, 'value')
        self.select5.observe(self.knot_select, 'value')

        #the following is for building HTML code to display colormap as vector arrays
        self.rows0, self.rows1, self.rows2, self.rows3, self.user_rows0, self.user_rows1 = "", "", "", "", "", ""
        self.html_maps0 = ("<!DOCTYPE html>"
                            "<html lang = 'en'>"
                            "  <head><style type='text/css'>"
                            "  table{width: 100%;border: thin solid black;}"
                            "  th,td{color: black;border: thin solid black;}</style>"
                            "<script>"
                            "  var opy,iny,r,b,g;"
                            "  window.onload=function(){"
                            "    opy=document.getElementById('opacity').innerHTML;"
                            "    iny=document.getElementById('intensity').innerHTML;"
                            "    r=document.getElementById('r').innerHTML;"
                            "    b=document.getElementById('b').innerHTML;"
                            "    g=document.getElementById('g').innerHTML;"
                            "    document.getElementById('colour').style.backgroundColor = 'rgb(255, 99, 71)';"
                            "  };"
                            "</script></head>"
                            "  <body>"
                            "    <h3>Retrieved values from srend</h3>"
                            "    <p>This shows any range of knots already written in the srend.F90 file for reference</p>"
                            "    <table>"
                            "      <tr><th>Knot #</th><th>Alpha Index</th><th>Alpha</th></tr>")
        #our update fxn will add in rows from dictionary values
        self.html_maps1 = "</table><table><tr><th>Knot #</th><th>Color Index</th><th>R</th><th>G</th><th>B</th></tr>"
        self.html_maps2 = "</table></body></html>"
        self.html_user_maps0 = ("<!DOCTYPE html>"
                            "<html lang = 'en'>"
                            "  <head><style type='text/css'>"
                            "  table{width: 100%;border: thin solid black;}"
                            "  th,td{color: black;border: thin solid black;}</style>"
                            "<script>"
                            "  var opy,iny,r,b,g;"
                            "  window.onload=function(){"
                            "    opy=document.getElementById('opacity').innerHTML;"
                            "    iny=document.getElementById('intensity').innerHTML;"
                            "    r=document.getElementById('r').innerHTML;"
                            "    b=document.getElementById('b').innerHTML;"
                            "    g=document.getElementById('g').innerHTML;"
                            "    document.getElementById('colour').style.backgroundColor = 'rgb(255, 99, 71)';"
                            "  };"
                            "</script></head>"
                            "  <body>"
                            "    <h3>User colormap</h3>"
                            "    <p>These data are to be set by the user. The map size is selectable by dropdown for both alpha and rgba knots. Select which knot to alter with the 'Current knot' dropdown, then adjust with the sliders or use the text box. Copy and paste is encouraged. If the knot value is correct, press the 'Update Knot' button to set the custom value and move on.</p>"
                            "    <table>"
                            "      <tr><th>Knot #</th><th>Alpha Index</th><th>Alpha</th></tr>")
        self.html_user_maps1 = "</table><table><tr><th>Knot #</th><th>Color Index</th><th>R</th><th>G</th><th>B</th></tr>"
        self.html_user_maps2 = "</table></body></html>"

        self.exp0 = wgts.HTML(value = "<h1>Ending Color Map Menu</h1><p>Colormaps 790 up to 799 will be replaced with the user table below. Submission here will generate the maps for knots 711-789 as incremental progressions from the first colormap until the map defined below.</p>")

        self.exp1 = wgts.HTML(value = self.html_maps0 + self.rows0 + self.html_maps1 + self.rows1 + self.html_maps2)
        self.exp2 = wgts.HTML(value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2)
        #.format(self.colormap_r.text.value, self.colormap_g.text.value, self.colormap_b.text.value, self.colormap_a.text.value, self.colormap_ai.text.value))

        self.butt0 = wgts.Button(description = 'Copy complete alpha map', description_tooltip = "alpha", disabled = False, button_style = 'danger', icon = 'drink')
        self.butt1 = wgts.Button(description = 'Copy complete rgb map', disabled = False, button_style = 'danger', icon = 'drink')
        self.butt2 = wgts.Button(description = 'Alter alpha knot', description_tooltip = "alpha", disabled = False, button_style = 'danger', icon = 'drink')
        self.butt3 = wgts.Button(description = 'Alter rgb knot', disabled = False, button_style = 'danger', icon = 'drink')
        self.butt4 = wgts.Button(description = 'Accept Map', disabled = False, button_style = 'success', icon = 'drink')
        self.butt5 = wgts.Button(description = 'Display Maps', disabled = False, button_style = 'info', icon = 'drink')
        self.butt0.on_click(self.copy_default_map)
        self.butt1.on_click(self.copy_default_map)
        self.butt2.on_click(self.set_user_knot)
        self.butt3.on_click(self.set_user_knot)
        self.butt4.on_click(self.handle_butt4)
        self.butt5.on_click(self.display_maps)

        self.select_ranges = wgts.HBox(children = [wgts.VBox(children = [self.select0, self.butt0]), wgts.VBox(children = [self.select1, self.butt1])])
        self.user_knot_select = wgts.HBox(children = [self.select4, self.select5])
        self.sliders = wgts.HBox(children = [self.slider_ai, self.slider_a, self.slider_i, self.slider_r, self.slider_g, self.slider_b, self.butt2, self.butt3])
        self.current_knot = wgts.VBox(children = [self.colormap_i_slds, self.colormap_rn_slds, self.colormap_g.obj_data, self.colormap_b.obj_data])
        self.knot_index = 0
        self.output_rgb, self.original_rgb = [(x[0], x[1], x[2], x[3], x[4]) for x in init_map_rgb], [(x[0], x[1], x[2], x[3], x[4]) for x in init_map_rgb]
        self.output_alpha, self.original_alpha = [(x[0], x[1], x[2]) for x in init_map_alpha], [(x[0], x[1], x[2]) for x in init_map_alpha]
        self.colormap_dict  = {'alpha' : [], 'red' : [], 'green' : [], 'blue' : []}
        #self.ending = wgts.VBox(children = [self.colormap_end_r.obj_data, self.colormap_end_b.obj_data, self.colormap_end_g.obj_data, self.colormap_end_o.obj_data, self.colormap_end_i.obj_data, self.colormap_end_oi.obj_data])
        #find colormap
        #display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))
        self.select4.value, self.select5.value = 1, 1
        self.select0.value, self.select1.value = alpha_range, rbg_range
        print("These are your maps from the last menu, alter the knots or select a new map to set the final map values. Knots 711-789 will be generated as interpolations between the original and final maps")
        self.show_map(self.original_rgb)
        self.show_map(self.original_alpha)

    def display_maps(self, obj):
        print("Knots 711-789 will be generated as interpolations between the original and final maps")
        print("Original")
        self.show_map(self.original_alpha)
        print("New")
        self.show_map(self.output_alpha)
        print("Original")
        self.show_map(self.original_rgb)
        print("New")
        self.show_map(self.output_rgb)

    def show_map(self, cmap):
        #we need to enforce that there are at least 2 valid knots
        # this function is technically generic and the logic is
        # a dispatch algorithm
        i = 0
        if len(cmap[0]) == 5:
            for x in cmap:
                if x[4]:
                    i += 1
            if i > 1:
                self.rgb_colormap = helper.create_ppm_cmap(cmap, self.rgb_source)
                self.img_rgb = wgts.Image(value = self.rgb_colormap, format = 'jpg')
                display(self.img_rgb)
            else:
                print("RGB colormap too small")
        elif len(cmap[0]) == 3:
            for x in cmap:
                if x[2]:
                    i += 1
            if i > 1:
                self.alpha_colormap = helper.create_ppm_cmap(cmap, self.alpha_source)
                self.img_alpha = wgts.Image(value = self.alpha_colormap, format = 'jpg')
                display(self.img_alpha)
            else:
                print("Alpha colormap too small")
        else:
            print("invalid colormap({})".format(cmap))

    def knot_select(self, obj):
        if(obj.owner.description_tooltip) == 'alpha':
            #print("debugging, set knot vector: {}".format(self.output_alpha[self.select4.value - 1]))
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td></tr>"
            knot_num = 1
            self.user_rows0 = ""
            for x in self.output_alpha:
                if x[2]:
                    if knot_num == self.select4.value:
                        self.user_rows0 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1])
                        self.colormap_ai.update_all(x[0])
                        self.colormap_a.update_all(x[1])
                    else:
                        self.user_rows0 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1])
                knot_num += 1
            #self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2

        else:
            #rgb_vector = ((self.colormap_i.get_value()), (self.colormap_r.get_value()), (self.colormap_g.get_value()), (self.colormap_b.get_value()))
            #self.output_rgb[self.select5.value - 1] = rgb_vector
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>"
            knot_num = 1
            self.user_rows1 = ""
            for x in self.output_rgb:
                if x[4]:
                    if knot_num == self.select5.value:
                        self.user_rows1 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                        self.colormap_r.update_all(x[1])
                        self.colormap_g.update_all(x[2])
                        self.colormap_b.update_all(x[3])
                        self.colormap_i.update_all(x[0])
                    else:
                        self.user_rows1 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                knot_num += 1
        self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2
        clear_output()
        display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))

    def set_user_knot(self, obj):
        if ('alpha' in (obj.description)) or ('Alpha' in (obj.description)):
            #set user alpha knot for the current value being viewed - self.output_alpha @ self.select2.value
            #index_a = int(self.select0.options.index(self.select0.value))
            alpha_vector = (int(self.colormap_ai.get_value()), float(self.colormap_a.get_value()), True)
            self.output_alpha[self.select4.value - 1] = alpha_vector
            # take the list and create an html formatted lists
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td></tr>"
            #print("debugging, set knot vector: {}".format(self.output_alpha[self.select4.value - 1]))
            knot_num = 701
            self.user_rows0 = ""
            for x in self.output_alpha:
                if x[2]:
                    if knot_num == self.select4.value:
                        self.user_rows0 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1])
                    else:
                        self.user_rows0 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1])
                knot_num += 1

        else:
            rgb_vector = (int(self.colormap_i.get_value()), float(self.colormap_r.get_value()), float(self.colormap_g.get_value()), float(self.colormap_b.get_value()), True)
            self.output_rgb[self.select5.value - 1] = rgb_vector
            html_row = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>"
            knot_num = 701
            self.user_rows1 = ""
            for x in self.output_rgb:
                if x[4]:
                    if knot_num == self.select5.value:
                        self.user_rows1 += "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td></tr>".format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                    else:
                        self.user_rows1 += html_row.format(knot_num, str(x[0]).split('.')[0], x[1], x[2], x[3])
                knot_num += 1
        #this loop sets the html for exp1 to read out the relevant datas
        self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2
        clear_output()
        display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))
        self.display_maps(None)

    def copy_default_map(self, obj):
        #This function will set user knots to values from the srend table
        if(obj.description) == 'Copy complete alpha map':

            difference = max(self.select4.options) - len(self.alpha_colormap)
            if difference >= 0:
                #alpha_colormap is shorter than output_alpha or no index conflict
                for x in range(0, (len(self.alpha_colormap))):
                    print("debug: var0({}), var1({})".format(self.output_alpha[x], self.alpha_colormap[x]))
                    self.output_alpha[x] = (self.alpha_colormap[x][0] ,self.alpha_colormap[x][1], True)
                    #set each vector within self.output_alpha to the corresponding value in self.alpha_colormap
                    #print("debugging alpha_colormap: index({}) and vector({})".format(x, self.alpha_colormap[x]))
            else:
                #alpha_colormap is longer
                for x in range(0, max(self.select4.options)):
                    self.output_alpha[x] = (self.alpha_colormap[x][0] ,self.alpha_colormap[x][1], True)
                    #set each vector within self.output_alpha to the corresponding value in self.alpha_colormap
                    #print("debugging alpha_colormap: index({}) and vector({})".format(x, self.alpha_colormap[x]))

            self.user_rows0 = ""
            for x in range(0, 10): #max(self.select4.options)):
                #print("Debug, user row defined: {}, i{}, a{}".format((x + 1), self.output_alpha[x][0], self.output_alpha[x][1]))
                if self.output_alpha[x][2]:
                    self.user_rows0 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), str(self.output_alpha[x][0]).split('.')[0], self.output_alpha[x][1])
                    #print("debugging output true false: num({}) output_alpha@x({})".format(x, self.output_alpha[x]))
                    #self.user_rows1 += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), self.output_rgb[x][0], self.output_rgb[x][1], self.output_rgb[x][2], self.output_rgb[x][3])
                #else:
                    #print("debugging output true false: num({}) output_alpha@x({})".format(x, self.output_alpha[x]))
        else:
            #set each vector within self.output_rgb to the corresponding value in self.rgb_colormap
            difference = max(self.select5.options) - len(self.rgb_colormap)

            if difference >= 0:
                #output is longer than selected range or no conflict in indices will occur
                for x in range((len(self.rgb_colormap))):
                    self.output_rgb[x] = (self.rgb_colormap[x][0], self.rgb_colormap[x][1], self.rgb_colormap[x][2], self.rgb_colormap[x][3], True)
            else:
                #output is shorter than the selected range
                for x in range(max(self.select5.options)):
                    self.output_rgb[x] = (self.rgb_colormap[x][0], self.rgb_colormap[x][1], self.rgb_colormap[x][2], self.rgb_colormap[x][3], True)
                    #set each vector within self.output_alpha to the corresponding value in self.alpha_colormap
                    #print("debugging rgb_colormap: index({}) and vector({})".format(x, self.rgb_colormap[x]))
            self.user_rows1 = ""
            #print('!!!Debug output_rgb({})'.format(self.output_rgb))
            for x in range(0, 10): #max(self.select5.options)):
                #this loop must update the user_rows1 html to show the table in output_rgb
                #print("Debug, user row defined: {}, i{}, r{}, g{}, b{}".format((x + 1), str(self.output_rgb[x][0]).split('.')[0], self.output_rgb[x][1], self.output_rgb[x][2], self.output_rgb[x][3]))
                if self.output_rgb[x][4]:
                    self.user_rows1 += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), str(self.output_rgb[x][0]).split('.')[0], self.output_rgb[x][1], self.output_rgb[x][2], self.output_rgb[x][3])
                    #self.user_rows0 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format((x + 1), self.output_alpha[x][0], self.output_alpha[x][1])
                    #print("debugging output true false: num({}) output_rgb@x({})".format(x, self.output_rgb[x]))
                #else:
                    #print("debugging output true false: num({}) output_rgb@x({})".format(x, self.output_rgb[x]))
        self.exp2.value = self.html_user_maps0 + self.user_rows0 + self.html_user_maps1 + self.user_rows1 + self.html_user_maps2
        clear_output()
        display(self.exp0, self.select_ranges, self.exp1, self.exp2, self.user_knot_select, self.sliders, self.current_knot, wgts.HBox(children = [self.butt4, self.butt5]))

    def update_default_range(self, obj):
        #call update_maps with the location of the start and end indexes
        # and 2 dictionaries for the different values
        #print("Debug: passed in object to update colormap({})\nalso here are select keys({})".format(obj, self.select0.keys))
        index_a = int(self.select0.options.index(self.select0.value))
        index_rgb = int(self.select1.options.index(self.select1.value))
        start_a = self.indexes[index_a][0]
        start_rbg = self.indexes[index_rgb][1]
        #Use index for displaying which range of rgba or alpha knots to be altered
        if(obj.owner.description_tooltip) == 'alpha':
            self.alpha_source = "alpha-{}".format(self.select0.value)
            self.rows0 = ""
            #row2 as well needs to be handled
            self.alpha_colormap = []
            for x in range(start_a[0], (start_a[1] + 1)):
                #print("debugging alpha here is dict key: ({})\nstart({})\nmax({})".format(x, self.indexes[index_a][0][0], self.indexes[index_a][0][1]))
                #x is an dictionary index
                knot = self.dicts[0][str(x)]
                self.rows0 += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(x, str(knot[0]).split('.')[0], knot[1])
                self.alpha_colormap.append(knot)
        else:
            self.rgb_source = "rgb-{}".format(self.select1.value)
            self.rows1 = ""
            #add in script for rows3
            self.rgb_colormap = []
            for x in range(start_rbg[0], (start_rbg[1] + 1)):
                #print("debugging rgb here is dict key: ({})\nstart({})\nmax({})".format(x, self.indexes[index_a][0][0], self.indexes[index_a][0][1]))
                #x is an dictionary index
                knot = self.dicts[1][str(x)]
                self.rows1 += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(x, str(knot[0]).split('.')[0], knot[1], knot[2], knot[3])
                self.rgb_colormap.append(knot)
            #self.num_rgb_knots = len(self.rgb_colormap)
        self.exp1.value = self.html_maps0 + self.rows0 + self.html_maps1 + self.rows1 + self.html_maps2

    def handle_submit0(self, obj):
        print("successful submit: {}".format(reader.working_file))
        self.write_submission0()#data = helper.copy_between_ordered(reader.reading_file, "viewheightdeg(nView)", "eyeminusLBF(1,nView)", 0, (1 - self.order))

    def handle_butt4(self, obj):
        valid = True
        for x in self.output_alpha:
            if x[2]:#this entry in the array is a boolean value
                if not helper.is_int(str(x[0]).split(".")[0]) or not helper.is_float(str(x[1])):
                    valid = False
                    print("!!!Problem alpha knot number({}) vector({})".format(self.output_alpha.index(x), x))
        for x in self.output_rgb:
            if x[4]:#if this is false, the user has selected less knots than the current x
                if not helper.is_int(str(x[0]).split(".")[0]) or not helper.is_float(str(x[1])) or not helper.is_float(str(x[2])) or not helper.is_float(str(x[3])):
                    valid = False
                    print("!!!Problem rgb knot number({}) vector({})".format(self.output_rgb.index(x), x))
        if not helper.is_valid_colormap(self.output_alpha):
            valid = False
            print("!!!Problem with user alpha colormap. Please ensure the indexes begin and end with 0 and 255 respectively.")
        if not helper.is_valid_colormap(self.output_rgb):
            valid = False
            print("!!!Problem with user rgb colormap. Please ensure the indexes begin and end with 0 and 255 respectively.")
        if valid:
            #write_submission
            clear_output()
            print("successful handle submit, writing tables...")
            self.write_submission0()

    def write_submission0(self):
        #write the first half of srend.F90
        reader.working_file = "output/srend.f90"
        pwd = os.getcwd()
        #data = "!!!beginning generated colormap entry!!!\n"
        #helper.write_data(reader.working_file, data)
        #write the first colormap
        map_string = ""
        map_index, i, i_a, i_rgb = 701, 701, 0, 0
        for x in self.original_alpha:
            if x[2]:
                i_a += 1
        for x in self.original_rgb:
            if x[4]:
                i_rgb += 1
        for xx in range(0, 10):
            print("\nWriting knots ({}) to ({})".format(map_index, (map_index + (max(i_rgb, i_a)))))
            i = map_index
            for x in range(0, (i_a)):
                if self.output_alpha[x][2]:
                    #delta_ calculates the difference in the beggining and end map values and holds 10%
                    # this is calculated each time - it didnt seem worth it to store a large array of delta values
                    delta_ia = (xx * (int(self.output_alpha[x][0]) - int(self.original_alpha[x][0]))) / 9
                    color_index = str(min(255.0, self.original_alpha[x][0] + (delta_ia))).split('.')[0]
                    #forcing a maximum 255 as an integer value inside a string
                    delta_a = min(1.0, self.original_alpha[x][1] + (xx * (float(self.output_alpha[x][1]) - float(self.original_alpha[x][1]))) / 9)
                    alpha_val = "{0:.4f}".format(delta_a)
                    data = "      DATA alpha_knot({}) /'{} {}'/\n".format(i, color_index, (alpha_val))
                    #print(" _Alpha index({}) delta_color({}) delta_opacity({}) ".format(i, delta_ia, alpha_val))
                    #helper.write_data(reader.working_file, data)
                    map_string += data
                    i += 1
                else:
                    break
            i = map_index
            for x in range(0, (i_rgb)):
                if self.output_rgb[x][4]:
                    #delta_ calculates the difference in the beggining and end map values and holds 10%
                    # this is calculated each time - it didnt seem worth it to store a large array of delta values
                    delta_i = (xx * (int(self.output_rgb[x][0]) - int(self.original_rgb[x][0]))) / 9
                    color_index = min(225, delta_i)
                    delta_r = (self.original_rgb[x][1] + (xx * (float(self.output_rgb[x][1]) - float(self.original_rgb[x][1]))) / 9)
                    r = "{0:.4f}".format(min(1.0, delta_r))
                    delta_g = (self.original_rgb[x][2] + (xx * (float(self.output_rgb[x][2]) - float(self.original_rgb[x][2]))) / 9)
                    g = "{0:.4f}".format(min(1.0, delta_g))
                    delta_b = (self.original_rgb[x][3] + (xx * (float(self.output_rgb[x][3]) - float(self.original_rgb[x][3]))) / 9)
                    b = "{0:.4f}".format(min(1.0, delta_b))
                    #print(" _RGB index({}), deltas - r({}), g({}), b({})".format(i, delta_r, delta_g, delta_b))
                    #note this "{0:.4f}" is a method of stringification that allows precision control in floating point numbers
                    # it only works if every {} instance in the string defintion has a designation inside
                    data = "         DATA rgb_knot({}) /'{} {} {} {}'/\n".format(i, str(self.original_rgb[x][0] + delta_i).split('.')[0], (r), (g), (b))
                    #I added the values to this knot line without trying to designate a condition for the integer values
                    #helper.write_data(reader.working_file, data)
                    map_string += data
                    i += 1
                else:
                    break
            map_index += 10
        helper.clear_working_file(reader.working_file)
        part1, part2 = helper.write_tweaked_srend(reader.srend_file)
        data = "{}{}{}".format(part1, map_string, part2)
        helper.write_data(reader.working_file, data)

        print("Complete! Please review the output srend.F90 file with path: {}".format(reader.working_file))
        self.display_maps(None)
        #print("\n DEBUG: start_a({}),\nstart_rgb({}),\nend_a({}),\nend_rgb({})".format(self.original_alpha, self.original_rgb, self.output_alpha, self.output_rgb))
