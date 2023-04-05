from json import loads,dumps
class Db:
    def __init__(self) -> None:
        with open("db.json") as f:
            data=f.read()
        if data:
            self.data= loads(data)
        else :
            self.data={}
    def save(self):
        with open("db.json",'w') as f:
            data = dumps(self.data,indent=4)
            f.write(data)
            
    def add_user(self,chat_id,name,user_name):
        self.data.setdefault(chat_id,{
            "Name": name,
            "User name": user_name,
            "Like":0,
            "Dislike":0,
            
            
        })
           
            
        
        
        self.save()
        
    
    def increase_like(self,chat_id):
        self.data[chat_id]["Like"]+=1
        
        self.save()
    
    def increase_dislike(self,chat_id):
        self.data[chat_id]["Dislike"]+=1
        self.save()
    
    def stat(self,chat_id):
        
        return f'<b>Like:</b>{self.data[chat_id]["Like"]}\n<b>Dislike:</b>{self.data[chat_id]["Dislike"]}'
