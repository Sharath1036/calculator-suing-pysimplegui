elif button is '=':
        # Error Case
        for i in List_Op_Error :  
            if '*' is Equal[0] or '/' is Equal[0] or ')' is Equal[0]  or i is Equal[-1]:   # Check Error Case
                Answer = "Error Operation" 
                break
            elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                Answer = "Error Operation" 
                break
            elif '(' in Equal :
                if ')' not in Equal :
                    Answer = "Error Operation" 
                    break   
            elif '(' not in Equal:
                if ')' in Equal:
                    Answer = "Error Operation" 
                    break
    
