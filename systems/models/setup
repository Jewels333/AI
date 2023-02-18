class self:
    class brith:
        def activate():
            brithdata = {
                "name":"",
                "brithdate":""
            }
            modeldata = {
                "assist":"",
                "env":""
            }
            
fp = 'systems\models\setup'
envp = 'systems\models\{env}'
ex = 'systems\models\model'
f = open(ex)
modelData = f.read()

    

class portal:
    def setup():
        query = input('Welcome to the Model Portal.\nStart Setup?')
        if query == 'Y':
            #link: @brithdata
            name = input('Enter Model Name: ')
            brithdate = input('Enter Model Brithdate: ')
            #link: @data
            assist = input('Enter Assist: ')
            env = input('Enter Enviroment (fp): ')
            parent = input('Enter Parent Account: ')
            query = input('Model Settings:\nModel Name: {name}\nModel Brithdate: {brithdate}\nModel Assist: {assist}\n Model Env. : {env}\nModel Parent: {parent}\n Set up Model? (Y/N)')
            if query == 'Y':
                model = open(envp + '\model', 'x')
                assistFile = open(envp + '\assist', 'x')
                model = open(envp + '\model')

                model.write(modelData)
                
                
            else:
                pass
        else:
            print('Aborted')

class assist:
    class connect:
        def open():
            pass
        def edit():
            pass
        def run():
            pass

self.brith.activate()
portal().setup()