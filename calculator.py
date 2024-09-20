# defining the function for Button 2  
def button_2_is_Clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  
  
# defining the function for Button 3  
def button_3_is_Clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
  
# defining the function for Button 4  
def button_4_is_Clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  
  
# defining the function for Button 5  
def button_5_is_Clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
  
# defining the function for Button 6  
def button_6_is_Clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)  
  
# defining the function for Button 7  
def button_7_is_Clicked():  
    global var  
    var = var + "7"  
    the_data.set(var)  
  
# defining the function for Button 8  
def button_8_is_Clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  
# defining the function for Button 9  
def button_9_is_Clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  
  
# defining the function for Button 0  
def button_0_is_Clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  
  
# defining the function for Button +  
def button_Add_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
  
# defining the function for Button -  
def button_Sub_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
  
# defining the function for Button *  
def button_Mul_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)  
  
# defining the function for Button /  
def button_Div_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)  
  
# defining the function for Button =  
def button_Equal_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
  
# defining the function for Button C  
def button_C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
  
# defining the function to display result  
def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  