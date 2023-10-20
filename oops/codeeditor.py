class Editor:
    name:str
    def __init__(self,name):
        self.name=name

    def spec(self):
        pass

class VsCode(Editor):
    def spec(self):
        print(f"{self.name}supports edit, debug, run, extension support")

    def __str__(self):
        return self.name

vobj=VsCode("Vscode")
vobj.spec()
print(vobj)