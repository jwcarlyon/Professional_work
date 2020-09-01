import importlib_resources #this reqired (pip install importlib_resources) command in my windows terminal
import os#This libray allows us to access the filesystem and read/write information!
import ipywidgets as wgts
import array # this is for making colorbars! cause wgts can't hack it!
from PIL import Image

def clear_working_file(file):
    #this will reference/create our working file - and erase it's contents if it exists
    pwd = os.getcwd()
    key=open(pwd+'/'+file,"w+")
    key.truncate(0)
    key.close()

def new_file_plus(file, new_file, beg_end, line2add):
    pwd = os.getcwd()

    if(os.path.isfile(pwd + '/' + file)):
        lines = ''
        valid = False
        if len(beg_end) < 2:
            #this is some logic which will make a new file and not add anything
            with open('{}/{}'.format(pwd, new_file), 'w') as key:
                key.write(line2add)
        else:
            with open(pwd + '/' + file, 'r') as key:
                line = key.readline()
                while line:
                    if(not(comment_bool(line)) and ("define " + beg_end[0] in line.strip())):
                        lines += line
                        valid = True
                        break
                    lines += line
                    line = key.readline()
                #this first loop copies the original file until the beggining line (beg_end[0])
            if not valid:
                return "new_file_plus(file({}), new_file({}), beg_end({}), line2add({})) failed beginning line".format(file, new_file, beg_end, line2add)
            valid = False
            with open('{}/output/{}'.format(pwd, new_file), 'w+') as key:
                #this loop is writing to a folder called output and a file specified in the function call
                for x in lines:
                    key.write(x)
                #now everything is copied to the new file
                key.write(line2add) #insert line here!
                lines = '' # this must be here or the first half gets written twice
            #now a carbon copy of the first loop, with a slight change
            with open(pwd + '/' + file, 'r') as key:
                line = key.readline()
                while line:
                    #this loop does not begin copying until it finds the end (beg_end[1])
                    line = key.readline()
                    if(not(comment_bool(line)) and ("define "+beg_end[1] in line.strip())):
                        lines += line
                        valid = True
                        while line:
                            line = key.readline()
                            lines += line
                            #this loops simply copies the rest of the file
            if not valid:
                return "new_file_plus(file({}), new_file({}), beg_end({}), line2add({})) failed end line".format(file, new_file, beg_end, line2add)

            with open('{}/output/{}'.format(pwd, new_file), 'a+') as key:
                #this loop is writing to a folder called output and a file specified in the function call
                for x in lines:
                    key.write(x)
    else:
        print("!!!new_file_plus.given file: {}. Could not be found - new_file({}) failed".format(file, new_file))

def get_flag_value(file, flag):
    #this fxn returns the value of a defined flag 29OCT2019
    pwd = os.getcwd()
    if(os.path.isfile(pwd + '/' + file)):
        with open(pwd + '/' + file, 'r') as key:
                line = key.readline()
                while line:
                    if(not(comment_bool(line)) and ("define "+flag in line.strip())):
                        for x in line.split():
                            if(len(flag) == len(x)):
                                if len(line.split()) > 3:
                                    ls = line.split()[2:]
                                    result = " ".join(ls)
                                    return result
                                return line.split()[-1]
                        #(len(line.split()[1])==(len(flag))))
                        # ^this is the original method to find flags,
                        # it is now a loop to catch errors like '# define ...'
                        # instead of '#define ...' with no spaces. 10Jan2020
                    line = key.readline()
                return("!!!flag not found")
                #write("#define "+flag+"\n")
    else:
        #print("Function get_flag_value(...) could not find file: "+file)
        return "!!!none found"

def get_comments(file, flag):
    #this fxn parses the file for a flag definition - the first definition -
    # then records and returns any comments immediately after that definition
    # if the next line is not a comment it will return an error string beginning
    # with '!!!!...' this is easily searchable if written to a file and
    # if it is being displayed to the user, the specified flag can be checked
    # for the exact problem or discrepancy 27Nov2019
    pwd = os.getcwd()
    if(os.path.isfile(pwd + '/' + file)):
        with open(pwd + '/' + file, 'r') as key:
                line = key.readline()
                while line:
                    if (not comment_bool(line)) and ("define " + flag in line):
                        # and (len(line.split()[1])==(len(flag))):
                        #flag in question found - are there comments?!
                        for x in line.split():
                            if(len(flag)==len(x)):
                                comment=""
                                line = key.readline()
                                while line:
                                    if (not comment_bool(line)) and (not(len(comment)>1)):
                                        return "!!!!Comments not found for flag: "+flag
                                    elif not comment_bool(line):
                                        return comment
                                    else:
                                        #this line adds the entire line, except the first word with whitespace
                                        comment += ((" ".join(line.split()[1:]))+"<br>")
                                        line = key.readline()
                    line = key.readline()
                return "!!!!Comments not found for flag: "+flag
    return "!!!!Comments not found for: "+flag+" and file is absent: "+file

def get_colormaps(file):
    #returns a raw string of all DATA declarations in srend.f90
    pwd = os.getcwd()
    if(os.path.isfile(pwd + '/' + file)):
        with open(pwd + '/' + file, 'r') as key:
            marker = "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
            end = "! ---- end: hardcoded section"
            rgb_vectors = []
            opacities = []
            indexes = []
            line = key.readline()
            while line:
                if(comment_bool(line) and (marker in line.strip())):
                    recording_rgb, recording_a = False, False
                    begin_a, map_num_a = 0, 0
                    begin_rgb, map_num_rgb = 0, 0
                    rgb_dict, a_dict = {}, {}
                    while not(end in line):
                        if(not(comment_bool(line)) and ("DATA " in line)):
                            #results.append(line)
                            if "alpha_knot" in line:
                                map_num_a = int((line.split("(")[1]).split(")")[0])

                                intensity_vector = [float(line.split("'")[1].split()[0]), float(line.split("'")[1].split()[1])]
                                opacities.append((map_num_a, intensity_vector))
                                a_dict[str(map_num_a)] = intensity_vector
                                if "rgb_knot" in line:
                                    map_num_rgb = int((line.split("(")[2]).split(")")[0])
                                    color_vector = list(map(float,line.split("'")[3].split()))
                                    rgb_vectors.append((map_num_rgb, color_vector))
                                    rgb_dict[str(map_num_rgb)] = color_vector
                                    if not recording_rgb:
                                        recording_rgb = True
                                        #  This condition means we must update begin.
                                        #rgb_dict[str(map_num_rgb)] = color_vector
                                        begin_rgb = map_num_rgb
                                        #rgb_dict[str(begin_rgb)] = ((len(rgb_vectors) - (map_num_rgb - begin_rgb) - 1), (len(rgb_vectors) - 1))#start and end color_vector indexes

                                if not recording_a:
                                    recording_a = True
                                    position = len(opacities) - 1
                                    #a_dict[str(begin_a)] = (position - (map_num_a - begin_a)), (position))
                                    begin_a = map_num_a
                                    #this line links the map number to it's array location as an integer
                                    # means that we begin counting an interval here
                            elif "rgb_knot" in line:
                                map_num_rgb = int((line.split("(")[1]).split(")")[0])
                                color_vector = list(map(float, line.split("'")[1].split()))
                                rgb_vectors.append((map_num_rgb, color_vector))
                                rgb_dict[str(map_num_rgb)] = color_vector
                                if not recording_rgb:
                                    rgb_dict[str(map_num_rgb)] = color_vector
                                    begin_rgb = map_num_rgb
                                    recording_rgb = True
                                    #rgb_dict[str(begin_rgb)] = ((len(rgb_vectors) - (map_num_rgb - begin_rgb) - 1), (len(rgb_vectors) - 1))#start and end color_vector indexes

                        else:
                            #here we have read a comment - end our ranges
                            if recording_a or recording_rgb:
                                recording_a, recording_rgb = False, False
                                gather = ((begin_a, map_num_a, (len(opacities) - (map_num_a - begin_a))),
                                        (begin_rgb, map_num_rgb, (len(rgb_vectors) - (map_num_rgb - begin_rgb))))
                                indexes.append(gather)
                                #rgb_dict[str(begin_rgb)] = ((len(rgb_vectors) - (map_num_rgb - begin_rgb) - 1), (len(rgb_vectors) - 1))#start and end color_vector indexes
                                #a_dict[str(begin_a)] = ((len(opacities)-(map_num_a - begin_a) - 1), (len(opacities) - 1))
                                #this clause must index both alpha and rgb knots separately
                        line = key.readline()
                    #data = "!!!debugging please ignore this from get_colormap. opacities ({})".format(str(opacities))
                    #write_data("practice/rerendered_run.f", data)
                    return (indexes, (a_dict, rgb_dict))


                line = key.readline()
            return ["!!!No colormap found for file: {}".format(file)]
    return ["!!!No file found {}".format(file)]
    #!!!Final return value is a 3tuple of lists

def create_ppm_cmap(vectorlist, output_ppm):
    #print("Debug!! Runnig create ppm filename({})".format(output_ppm))
    #print("Debug!! Runnig create ppm vectors({})".format)
    i_rgb, i_a, i_knot = 0, 0, 0
    nw_ls = []
    debug_data = ""

    for x in range(len(vectorlist)):
        if len(vectorlist[x]) == 3 and vectorlist[x][2]:
            i_a += 1
            nw_ls.append(tuple([vectorlist[x][0], vectorlist[x][1], vectorlist[x][1], vectorlist[x][1]]))
            #if len(vectorlist[-x]) == 3 and vectorlist[-x][2]:
            #nw_ls.append(tuple([vectorlist[-x][0], vectorlist[-x][1], vectorlist[-x][1], vectorlist[-x][1]]))
            #print("!!!alpha knot: ({})".format(x))
        if len(vectorlist[x]) == 5 and vectorlist[x][4]:
            i_rgb += 1
            nw_ls.append(tuple([vectorlist[x][0], vectorlist[x][1], vectorlist[x][2], vectorlist[x][3]]))
            #if len(vectorlist[-x]) == 5 and vectorlist[-x][4]:
            #nw_ls.append(tuple([vectorlist[-x][0], vectorlist[-x][1], vectorlist[-x][2], vectorlist[-x][3]]))
            #print("!!!rgb knot: ({})".format(x))
    vectorlist = nw_ls
    i = max(i_rgb, i_a)
    #i now holds the number of knots
    if i < 3:
        return "Colormap too small, 3 or more knots please: {}".format(vectorlist)

    width = 1024
    height = 128
    maxval = 255.0
    row_width, row_value = int(width / 200), 0#max(int(width * 0.01),1), 0
    ppm_header = 'P6 {} {} {}\n'.format(width, height, int(maxval))
    #f'P6 {width} {height} {maxval}\n'

    # PPM image data
    image = array.array('B', [0, 0, 0] * width * height)
    #Haha not white... x000 is black...

    rectangles = int(width / row_width)
    rec_per_knot = int(rectangles / (i - 1)) #64 / 9 is 7.xxxx
    extra = (rectangles % (i - 1)) #64 mod 9 is 8
    delta_knot = ((vectorlist[1][1] - vectorlist[0][1]), (vectorlist[1][2] - vectorlist[0][2]), (vectorlist[1][3] - vectorlist[0][3]))
    knot_delta = ((delta_knot[0] / rec_per_knot), (delta_knot[1] / rec_per_knot), (delta_knot[2] / rec_per_knot))

    knot = []
    #print("Entering loop: rectanges({}), rec_per_knot({}), extra({}), delta_knot({})".format(rectangles, rec_per_knot, extra, delta_knot))
    for _x in range(3):
        knot.append((vectorlist[i_knot][_x + 1]))

    advance = True #advance means a new knot needs to be rendered
    for z in range(rectangles):
        if (rec_per_knot == -1) or (z == (rectangles - 1)):
            #This is the beginning of a new rectangle and knot
            # color++. This condition leads to a new knot and a 0 delta_knot

            advance = True #this condition prevents delta from being added to a new knot
            i_knot += 1
            knot = [vectorlist[i_knot][1], vectorlist[i_knot][2], vectorlist[i_knot][3]]
            #print("!!!Dbug: knot({}), index({}), rectangle({})".format(knot, i_knot, z))
            if(vectorlist[i_knot][1] == float('nan')) or (vectorlist[i_knot][2] == float('nan')) or (vectorlist[i_knot][3] == float('nan')):
                print("Advance called at the end of knots, knot({}), index({}), rectangle({})".format(knot, i_knot, z))

            rec_per_knot = int(rectangles / (i - 1))
            if extra > 0:
                rec_per_knot += 1
                extra -= 1
            #now delta_knot needs to be set
            if i_knot == i - 1:
                #!!! I think this may need to be just (i_knot == i)...
                delta_knot = (0.0, 0.0, 0.0)
                #print("Reached end of knots, this is wrong: rectangle({}), index({}), knot({}), delta({})".format(z, i_knot, knot, knot_delta))
            else:
                delta_knot = ((vectorlist[i_knot + 1][1] - vectorlist[i_knot][1]), (vectorlist[i_knot + 1][2] - vectorlist[i_knot][2]), (vectorlist[i_knot + 1][3] - vectorlist[i_knot][3]))
            #this final statement resets the delta used in rectangle to rectangle
            knot_delta = ((delta_knot[0] / rec_per_knot), (delta_knot[1] / rec_per_knot), (delta_knot[2] / rec_per_knot))
        #rectangle++, z is also a count of rectangle progress
        debug_data += "Rectangle({}), knot({}) delta_knot({}), advance({})\n".format(z, knot, delta_knot, advance)

        if advance:
            advance = False
            #NOTE this logic does not change the knots - only references them.
            # the rgb values created in this case are used for a single rectangle

            if (knot[0] < .55 and knot[0] > .5) and (knot[1] < .55 and knot[1] > .5) and (knot[2] < .55 and knot[2] > .5):
                r, g, b = 0.0, 0.0, 0.0 # an anti grey solution
            elif (knot[0] < .5 and knot[0] > .45) and (knot[1] < .5 and knot[1] > .45) and (knot[2] < .5 and knot[2] > .45):
                r, g, b = 1.0, 1.0, 1.0
            elif (knot[0] < .1) and (knot[1] < .1) and (knot[2] < .1):
                r, g, b = 0.55, 0.55, 0.55 # a grey solution
            else:
                r, g, b =(1.0 - knot[0]), (1.0 - knot[1]), (1.0 - knot[2])

        else:
            knot = [(knot[0] + knot_delta[0]), (knot[1] + knot_delta[1]), (knot[2] + knot_delta[2])]
            r, g, b = min(1.0, knot[0]), min(1.0, knot[1]),  min(1.0, knot[2])

        if (r > 1.0)  or (g > 1.0) or (b > 1.0) or (r == float("NaN"))  or (g == float("NaN")) or (b == float("NaN")):
            print("Over added a knot or index overrun, this is wrong. r({}), g({}), b({}), knot_delta({}), knot_num({}), rectangle({})".format(r, g, b, knot_delta, i_knot, z))
            #knot[_x] = 1.0
        #there currently 1024/16 = 64 rectangles
        #we are going to go through the rectangles one by one
        #but there 2 to 10 knots
        #z + 1 represents the rectangle out of (width / row_width) total
        for y in range(height):#y is basically every row by number
            for x in range(row_value, (row_value + row_width)):
                #x is the current pixel number within the row
                # don't add stuff here - it's not efficient at all
                index = 3 * (y * width + x)
                #the stride is 3
                image[index] = int(r * maxval)
                image[index + 1] = int(g * maxval)
                image[index + 2] = int(b * maxval)
                #this loop writes all the pixels in a row of rectangles
        rec_per_knot -= 1
        row_value += row_width


    # Save the PPM image as a binary file - this is necessary to pass the info to
    # the Render_tool. Otherwise the datatype will be bytearray instead of bytes...
    # there must be a fix for this but I am out of time
    #pwd = os.getcwd()
    with open('output/debug.txt', 'w') as f:
        f.write(debug_data)

    with open('output/{}.ppm'.format(output_ppm), 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)
    #converting to jpg
    im = Image.open('output/{}.ppm'.format(output_ppm))
    im.save('output/{}.jpg'.format(output_ppm))

    with open('output/{}.jpg'.format(output_ppm), 'rb') as f:
        data = f.read()
        return data

def comment_bool(string):
    if(len(string.strip()) > 1):
        if ("c " in string.strip()[:2]) or ("C " in string.strip()[:2]) or (string.strip()[0] == "!"):
            return True
        else:
            return False
    elif len(string.strip()) > 0:
        if string.strip()[0] == "C" or string.strip()[0] == "c" or string.strip()[0] == "!":
            return True
    return False

def arg_line_bool(arg, line):
    for x in line.split():
        if(len(arg) == len(x)):
            return True
    return False

def is_int(string):
#this function will return true if a string is a number with no decimal or alphabetic garbage!
# UPDATE now this function will allow variable names and parenthesis along with any mathematical logic
# which will likely come up. 14Mar2020

#in the event of a TypeError: argument of type *not string* is not iterable - make sure
# this function always gets a string and not a number
    if(("*" in string) or ("/" in string) or ("+" in string)) and not('.' in string):
        valid = True
        #removed_parens = (string.replace('(','')).replace(')','')
        #for x in (removed_parens.split("*")):
        #    #print(x)
        #    if (len(x) > 0) and (not is_int(x)):
        #        for xx in x:
        #            if not xx.isalpha():
        #                valid = False
        return valid

    else:
        removed_parens = (string.replace('(','')).replace(')','')
        try:
            int(removed_parens)
            return True
        except ValueError:
            #print("debug: removed({})".format(removed_parens))
            if (len(removed_parens) > 0) and (removed_parens[0].isalpha()) and (removed_parens[0] != '!'):
                return True
            return False

def is_float(string):
    #this fxn is meant to return true only on floating point data types.
    # amended to include statements with parenthesis and multiplication symbols 5Feb2020
    # further amended to include division 8Mar2020
    if("*" in string):
        valid = True
        removed_parens = (string.replace('(','')).replace(')','')
        #print(removed_parens)
        for x in (removed_parens.split("*")):
            #print(x)
            if (len(x) > 0) and (not is_float(x)):
                valid=False
        return valid
    elif("/" in string):
        valid = True
        removed_parens = (string.replace('(','')).replace(')','')
        #print(removed_parens)
        for x in (removed_parens.split("/")):
            #print(x)
            if not is_float(x):
                valid = False
        return valid
    else:
        removed_parens = (string.replace('(','')).replace(')','')
        try:
            float(removed_parens)
            return True
        except ValueError:
            if (len(removed_parens) > 0) and (removed_parens[0].isalpha()) and (removed_parens[0] == '!'):
                return True
            return False

def is_line_defined(file, string):
    #this function simply returns true
    # if there is a copy of the phrase: 'string' in an uncommented line
    pwd = os.getcwd()
    if(os.path.isfile(pwd + '/' + file)):
        with open(pwd + '/' + file, 'r') as key:
                line = key.readline()
                while line:
                    if not comment_bool(line):
                        if string in line:
                            return True
                    line = key.readline()
                return False
    else:
        print("Function get_flag_value(file {}) could not find file.".format(file))
        return False

def is_valid_colormap(map_array):
    c_map = []
    prev = -1
    valid = True
    for x in range(len(map_array)):
        if len(map_array[x]) == 3 and map_array[x][2]:
            c_map.append(tuple(map_array[x]))
            if prev > int(map_array[x][0]):
                print("Alpha array must have increasing index values, please adjust before continuing.\nKnots examined: prev({}) current({})".format(prev, map_array[x][0]))
                return False
            prev = int(map_array[x][0])
        if len(map_array[x]) == 5 and map_array[x][4]:
            c_map.append(tuple(map_array[x]))
            if prev > int(map_array[x][0]):
                print("RGB array must have increasing index values, please adjust before continuing.\nKnots examined: prev({}) current({})".format(prev, map_array[x][0]))
                return False
            prev = int(map_array[x][0])
    #print("Debug, cmap: {}\n".format(c_map))
    if len(c_map) < 2:
        valid = False
    elif(int(c_map[0][0]) != 0) or (int(c_map[-1][0]) != 255):
        valid = False
    return valid

def copy_until_from(file, end, start=""):
    #This function parses a file looking for a place to stop.
    #if no value is given for start then the function will copy everything
    #flag is a reqired value, this value is where the parsing stops and This
    # value will not be returned in the final value - which is a multiline string
    # No need to specify the define portion '#define...' only enter the exact
    # name of the flag/variable you want to target 27Nov2019
    final = ""
    line = ""
    pwd = os.getcwd()
    #print(file+' and '+flag+' also '+start)
    if len(start) > 1:
        if(os.path.isfile(pwd + '/' + file)):
            with open(pwd + '/' + file, 'r') as key:
                line = key.readline()
                while(line):
                    #this loop finds the starting point
                    # ignores the rest of the file
                    #if (line[0] != 'c') and ('define ' + start in line):
                    if (not(comment_bool(line)) and (("#define {}".format(start) in line) or ("{} = ".format(start) in line))):
                        #at this point the line has our start flag
                        for x in line.split():
                            if(len(start) == len(x)):
                                #start copying
                                line = key.readline()
                                while(line):
                                #this loop saves everything until the
                                # end point. result will exclude start and end flags
                                    if (not(comment_bool(line)) and (("#define {}".format(end) in line) or ("{} = ".format(end) in line))):
                                    #if (line[0] != 'c') and ('define ' + end in line):
                                        #at this point the end is found
                                        for y in line.split():
                                            if(len(end) == len(y)):
                                                return final
                                    final += line
                                    line = key.readline()
                                return "!!!!Failed copy_until_from!!!!\nEnd not found: "+end
                        line = key.readline()
                        #this line prevents an endless loop - for example:
                        # when a start flag "isBoB8" is given, The algorithm will
                        # first find "isBoB" but this line will eliminate the false
                        # positive - if(len(start)==len(x)): - by following the for
                        # loop with a readline, the program will continue the search
                        # 18Feb2020
                    else:
                        line = key.readline()
                return "!!!!Failed copy_until_from!!!!\nStart not found: "+start
        return "!!!!Failed copy_until_from!!!!\nFile not found: "+file
    else:#this logic implies we start from the beginning and copy over everything
        if(os.path.isfile(pwd + '/' + file)):
            with open(pwd + '/' + file, 'r') as key:
                line = key.readline()
                while(line):
                    if (line[0] != 'c') and (end in line):
                        # and (len(line.split()[1])==(len(end))):
                        for x in line.split():
                            if(len(end) == len(x)):
                                return final
                    final += line
                    line = key.readline()
                return "!!!!Failed copy_until_from!!!!\nNo start, End not found: "+end
        return "!!!!Failed copy_until_from!!!!\nFile not found: "+file

def copy_after(file, flag):
    #this fxn is exactly lik copy_until_from but will record the entire file
    # after and not including the specified flag value. No need to specify the
    # define portion '#define...' only enter the exact name of the flag/variable
    # you want to target
    pwd = os.getcwd()
    final = ""
    if(os.path.isfile(pwd + '/' + file)):
        with open(pwd + '/' + file, 'r') as key:
            line = key.readline()
            while(line):
                if (line[0] != 'c') and ("define "+flag in line):
                    #and (len(line.split()[1])==(len(flag))):
                    for x in line.split():
                        if(len(flag)==len(x)):
                            line = key.readline()
                            while(line):#this loop saves everything until the
                                # end point. result will exclude start flag
                                final += line
                                line = key.readline()
                            return final
                line = key.readline()
            return "!!!!Failed copy_after!!!!\nflag not found: "+flag
    return "!!!!Failed copy_after!!!!\nfile not found: "+file

def write_tweaked_srend(file):
    #print("!!!Debug, data({})".format(data))
    first_half, sec_half = "", ""
    pwd = os.getcwd()
    if(os.path.isfile(pwd + '/' + file)):
        if not(os.path.isdir(pwd + '/output')):
            os.mkdir(pwd + '/output')
        with open(pwd + '/' + file, 'r') as key:
            line = key.readline()
            #print("!!!Debug first loop entered")
            while(line):
                #this loop finds the ending point
                first_half += line
                #print("\n!!!examine line({})".format(line))
                if ((comment_bool(line)) and ("BEGIN 10 TWEAKING COLOR TABLES" in line)):# and arg_line_bool("TWEAKING COLOR TABLES", line)):
                    #this eliminates any false positives while remaining flexible in finding stuff - hopefully
                    line = key.readline()
                    while comment_bool(line):
                        first_half += line
                        line = key.readline()
                    #return first_half
                    #print("\n!!!examine lines({})".format(first_half))
                    #with open(pwd + '/output/srend.f90','w') as key:
                        #print(sec_half)
                    #    key.write(first_half)
                    break
                line = key.readline()
        #write the middle
        #with open(pwd + '/output/srend.f90','a') as key:
        #    key.write(data)
        #Now get the second half
        with open(pwd + '/' + file, 'r') as key:
            line = key.readline()
            #print("!!!Debug first loop entered")
            while(line):
                #this loop finds the start
                #print("\n!!!examine line({})".format(line))
                if((comment_bool(line)) and ("END 10 TWEAKING COLOR" in line)):# and arg_line_bool("TWEAKING COLOR TABLES", line)):
                    #this eliminates any false positives while remaining flexible in finding stuff - hopefully
                    while(line):
                        sec_half += line
                        line = key.readline()
                    #return first_half
                    #with open(pwd + '/output/srend.f90','a') as key:
                    #print(sec_half)
                    #    key.write(sec_half)
                    break
                line = key.readline()

        return (first_half, sec_half)
    else:
        raise OSError([file])

def write_data(file, data):
    #this fxn adds to the last line of our file like write flag
    # the difference is this fxn does not add any extra lines or
    # define keywords "#define...". I intended to use this when
    # I have just written a flag and would like to copy everything
    # between that flag and the next variable/flag of interest.
    # 27Nov2019
    pwd = os.getcwd()
    if(os.path.isfile(pwd + '/' + file)):
        with open(pwd + '/' + file,'a') as key:
            #'a' for append - will not erase a files contents
            key.write(data)
    else:
        print("Function write_data({}, {}) could not find file".format(file, data))
