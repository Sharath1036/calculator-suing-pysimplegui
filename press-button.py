 if button is 'AC':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif button is 'DEL':
        Equal = Equal[:-1]
        form.FindElement('input').Update(Equal)
    elif len(Equal) == 16 :
        pass
    elif str(button) in '1234567890+-().':
        Equal += str(button)
        form.FindElement('input').Update(Equal) 
    elif button is 'x':
        Equal += '*'
        form.FindElement('input').Update(Equal)
    elif button is '÷':
        Equal += '/'
        form.FindElement('input').Update(Equal)
    elif button is 'MOD':
        Equal += '%'
        form.FindElement('input').Update(Equal)
 
 
