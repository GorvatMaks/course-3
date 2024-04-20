import json 
def rFile():

    with open("m2/TestRuffier/reminf.json", "r")as file:
        file_len = json.load(file)
    
    return file_len

def wFile(slovn):
    with open("m2/TestRuffier/reminf.json", "w")as file:
        json.dump(slovn,file,ensure_ascii=False,indent=4)