from browser import document , alert, html

calculator = document['calculator']

display = html.DIV('',id='display')#create div to display result
list = '0123456789-+/*=c' #make a string list of cal buttons
button_list = [display] #put display first to aviod the btns showing as elements


###creating the logic function
firstvals = []
secondvals = []
def logic(ev):
   """ compare the buttons """
   global firstvals
   global secondvals
   btn_value = ev.target.text## holds the content of the clicked btn
   symbols = '+-/*'## holds all possible math symbols
   len_symbols = len(symbols)
   count = 0 ###used to prevent duplication when iteration is run


   if btn_value == 'c':
      display.text = ''
      firstvals = []
      secondvals = []

   elif btn_value == '=':
      sum_vals = eval(display.text)
      display.text = sum_vals
   else:
      for symbol in symbols:
         if symbol in display.text:
            display.text += btn_value
            secondvals.append(btn_value)
         else:
            count += 1
            if count == len_symbols:
               display.text += btn_value
               firstvals.append(btn_value)
            
   print(f'first {firstvals}')
   print(f'second {secondvals}')
   print(count)



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