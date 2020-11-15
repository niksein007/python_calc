from browser import document , alert, html

calculator = document['calculator']

#create div to display result
display = html.DIV('',id='display')

### a disctionary to hold all the buttons and their values
btns_dict = {"dot":".","zero":"0","one":"1","two":"2","three":"3",
"four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9",
"minus":"-","plus":"+","divide":"/","multiply":"*","equals":"=",
"cancle":"c","delete":"Del"} #make a string list of cal buttons

#put display first to aviod the btns showing as elements
output_list = [display] 


###creating the logic function
def logic(ev):
   """ compare the buttons """
   btn_value = ev.target.text## holds the content of the clicked btn
   symbols = '+-/*='## holds all possible math symbols
   len_symbols = len(symbols)
   count = 0
   msg1 = 'please enter an expression'


   if btn_value == 'c':
      display.text = ''

   elif btn_value == 'Del':
     display.text = display.text[:-1] ### slice off all chars except the last char

   elif btn_value == '=':
      if (display.text == '') or (display.text == msg1) \
      or (display.text == '*')  or (display.text == '-') \
      or (display.text == '/')  or (display.text == '+')   \
      :
         display.text = msg1
      else:
         sum_vals = eval(display.text)
         display.text = sum_vals
   else:
      for symbol in symbols:
         if (btn_value == symbol) and (symbol in display.text):
            pass
         else:
            count += 1
            if count == len_symbols:###update display after all symbol checks are done
               if display.text == msg1:
                  display.text = ''
               display.text += btn_value
           
###loop through the dict and bind to click event
### add them to the output_list
for key, value in btns_dict.items():
   button = html.BUTTON(value,id='btn_' + key )
   button.bind('click',logic)
   output_list.append(button)

### add buttons to calculator div which includes the display div
calculator <= output_list 
# document <= button