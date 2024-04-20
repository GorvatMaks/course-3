def rFile():
    rdickt = dict()

    with open("m2/TestRuffier/reminf.json", "r")as file:
        file_len = len(file.read())
        file.seek(0)
        
        key = ""
        value = ""
        is_key = True
        is_qouted = True
        
        for i in range(file_len):
            read = file.read(1).strip()
            
            if read == '"':
              pass  
            elif read == '{' or read == '}':
              pass  
            
            elif read == ":":
                is_key = False
            
            elif read == ",":
                rdickt[key] = value
                is_key = True
                key = ""
                value = ""

            else:
                if is_key:
                    key += read
                else:
                    value += read
        rdickt[key] = value
    
    print(rdickt)
    return rdickt

rFile()

