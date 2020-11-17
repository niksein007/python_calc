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

### this holds the content to be evaluated
eval_string = ''



### a disctionary to hold all the buttons and their values
btns_dict = {"dot":["&middot;",'.'],"zero":["0",'0'],"one":["1",'1'],
"two":["2",'2'],"three":["3",'3'],"four":["4",'4'],"five":["5",'5'],
"six":["6",'6'],"seven":["7",'7'],"eight":["8",'8'],"nine":["9",'9'],
"minus":["&minus;",'-'],"plus":["&plus;",'+'],"divide":["&divide;",'/'],
"multiply":["&times;",'*'],"equals":["&equals;",'='],
"cancel":["C",'c'],"delete":["Del",'delete']} 

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
   global eval_string
   btn_value = ev.target.value### holds the value attr of the clicked btn
   btn_text = ev.target.text ### holds the text content of the btns
   symbols = '+-/*='## holds all possible math symbols
   len_symbols = len(symbols)
   count = 0
   msg1 = 'invalid input!'


   if btn_value == 'c':
      inputs.text = ''
      eval_string = ''
      result.text = '0'

   elif btn_value == '.' and inputs.text == '' and eval_string == '':
      inputs.text = '0.'
      eval_string = '0.'

   elif (btn_value == '.') and (btn_text in inputs.text) \
   and (btn_value in eval_string) :
      pass

   elif btn_value == 'delete':
      if inputs.text == msg1 or inputs.text == '0.' or eval_string == '0.':
         inputs.text = ''
         eval_string = ''
      else:
         inputs.text = inputs.text[:-1] ### slice off all chars except the last char
         eval_string = eval_string[:-1] ### same as above but for eval_string

   elif btn_value == '=':
      if (eval_string != '') and (eval_string[-1] in symbols)\
      or (inputs.text == msg1):
         inputs.text = msg1
         eval_string = ''
       ### ensure no multiple equals sign  
      elif btn_text in inputs.text or eval_string == '':
         pass
      else:
         sum_vals = eval(eval_string)
         result.text = sum_vals
         inputs.text += btn_value 
         eval_string = str(sum_vals) ### to ensure cal can be done after initial sumation
   else:
      for symbol in symbols:
         ### ensure symbols dont start the expression
         if (btn_value == symbol) and (inputs.text =='') \
         and (eval_string == '') :
            pass
            ### ensure no err msg 
         elif (btn_value == symbol) and (inputs.text == msg1):
            pass   
      ### check that symbols dont repeat 
         elif (btn_value == symbol) and (eval_string[-1] == symbol) :
            pass
         ### only happens if the last char is a symbol =>change the symbol
         elif (btn_value == symbol) and (eval_string[-1] in symbols) \
         and (eval_string[-1] != symbol):
            inputs_list = list(inputs.text)
            inputs_list[-1] = btn_text
            inputs.text = ''.join(inputs_list)###join converts to string
### repeat for eval_string
            eval_list = list(eval_string)
            eval_list[-1] = symbol
            eval_string = ''.join(eval_list)

            ### create a proper display
         elif (result.text != '0') and (btn_value in symbols):
            inputs.text = result.text + btn_text
            eval_string = result.text + btn_value
            result.text = '0'
         elif (result.text != '0') and (btn_value not in symbols):
            inputs.text = btn_text
            eval_string = btn_value
            result.text = '0'
         else:
            count += 1
###update display after all symbol checks are done i.e symbol doesnt repeat
            if count == len_symbols:
               if inputs.text == msg1:
                  inputs.text = ''
               inputs.text += btn_text
               eval_string += btn_value

   # print(eval_string)
           
###loop through the dict and bind to click event
### add them to the output_list
for key, value in btns_dict.items():

   button = html.BUTTON(value[0], id='btn_' + key, value=value[1])
   button.bind('click',logic)
   button.bind('mousedown',mousedown)
   button.bind('mouseup',mouseup)

   output_list.append(button)

### add buttons to calculator div which includes the display div
calculator <= output_list 