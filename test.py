from browser import document , alert
    
document <= "Hello mark!"

def hello(ev):
   alert("Hello !")

document["button_alert"].bind("click", hello)