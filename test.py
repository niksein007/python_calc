from browser import document , alert, html
### getting access to the calculator div using its id
calculator = document['calculator']

###creating an inputs pane
inputs = html.DIV('',id='inputs')

###creating a results pane
result = html.DIV('0',id='result')

#create div to display result
display = html.DIV('',id='display')

display <= inputs
display <= result


### a disctionary to hold all the buttons and their values
btns_dict = {"dot":".","zero":"0","one":"1","two":"2","three":"3",
"four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9",
"minus":"-","plus":"+","divide":"/","multiply":"*","equals":"=",
"cancle":"C","delete":"Del"} #make a string list of cal buttons

#put display first to aviod the btns showing as elements
output_list = [display] 

###mousedown function
def mousedown(ev):
   """change colour on click"""
   btn = ev.target
   btn.style.backgroundColor = 'gray'

###mouseup function
def mouseup(ev):
   """change colour on unclick"""
   btn = ev.target
   btn.style.backgroundColor = 'black'

###creating the logic function
def logic(ev):
   """ compare the buttons """
   btn_value = ev.target.text## holds the content of the clicked btn
   symbols = '+-/*='## holds all possible math symbols
   len_symbols = len(symbols)
   count = 0
   msg1 = 'please enter a valid input'


   if btn_value == 'C':
      inputs.text = ''
      result.text = '0'

   elif btn_value == 'Del':
      if inputs.text == msg1:
         inputs.text = '0'
      else:
         inputs.text = inputs.text[:-1] ### slice off all chars except the last char

   elif btn_value == '=':
      if (inputs.text[-1] in symbols) or (inputs.text == msg1):
         inputs.text = msg1
      else:
         sum_vals = eval(inputs.text)
         result.text = sum_vals
         inputs.text += btn_value 
   else:
      for symbol in symbols:
         ### ensure symbols dont start the expression
         if (btn_value == symbol) and (inputs.text =='') :
            pass
            ### ensure no err msg 
         elif (btn_value == symbol) and (inputs.text == msg1):
            pass   
      ### check that symbols dont repeat 
         elif (btn_value == symbol) and (inputs.text[-1] == symbol):
            pass
         ### only happens if the last char is a symbol
         elif (btn_value == symbol) and (inputs.text[-1] in symbols) \
         and (inputs.text[-1] != symbol):
            inputs_list = list(inputs.text)
            inputs_list[-1] = symbol
            inputs.text = ''.join(inputs_list)###join converts to string
            ### create a proper display
         elif (result.text != '0') and (btn_value in symbols):
            inputs.text = result.text + btn_value
            result.text = '0'
         elif (result.text != '0') and (btn_value not in symbols):
            inputs.text = btn_value
            result.text = '0'
         else:
            count += 1
###update display after all symbol checks are done i.e symbol doesnt repeat
            if count == len_symbols:
               if inputs.text == msg1:
                  inputs.text = ''
               inputs.text += btn_value
           
###loop through the dict and bind to click event
### add them to the output_list
for key, value in btns_dict.items():
   button = html.BUTTON(value,id='btn_' + key )
   button.bind('click',logic)
   button.bind('mousedown',mousedown)
   button.bind('mouseup',mouseup)

   output_list.append(button)

### add buttons to calculator div which includes the display div
calculator <= output_list 
# document <= button