from browser import document , alert, html

calculator = document['calculator']

display = html.DIV('',id='display')#create div to display result
list = ['.','0','1','2','3','4','5','6','7','8','9','-','+','/','*','=','c','Del'] #make a string list of cal buttons
button_list = [display] #put display first to aviod the btns showing as elements


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
           
  



### creating the calculate  function
def calculate (ev):
   """ calculations """
   logic(ev)


for item in list:
   button = html.BUTTON(item,id=item)
   button.bind('click',logic)
   button_list.append(button)

### add buttons to calculator div which includes the display div
calculator <= button_list 
# document <= button