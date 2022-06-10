else :
            Answer = str("%0.7f" %(eval(Equal)))                         
            if '.0' in Answer:
                Answer = str(int(float(Answer)))                         
        form.FindElement('input').Update(Answer)                         
        Equal = Answer

    elif button is 'Quit'  or button is None:                            
        break
