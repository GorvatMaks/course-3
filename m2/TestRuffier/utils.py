def rFile():
    rdickt = dict()

    with open("m2/TestRuffier/reminf.json", "r")as file:
        file_len = len(file.read())
        file.seek(0)
        for i in range(file_len):
            read = file.read(1)
            if read == '"':
              pass  
            elif read == ":":
                pass
    return rdickt
rFile()