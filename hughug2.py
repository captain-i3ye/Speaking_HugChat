from hugchat import hugchat
from hugchat.login import Login
from gtts import gTTS
# from io import BytesIO
import os
import playsound
#import time

class hugC:

    def __init__(self) -> None:
        self.user = "user_name"
        self.passwd = "password"
        self.cookie_dir_path = './cookies_snapshot'

        self.sign = Login(self.user, self.passwd)
        try:
            self.cookies = self.sign.loadCookiesFromDir(self.cookie_dir_path)
        except:
            self.cookies = self.sign.login()
            self.sign.saveCookiesToDir(self.cookie_dir_path)
        
        self.chatbot = hugchat.ChatBot(cookies=self.cookies.get_dict())

        id = self.chatbot.new_conversation()
        self.chatbot.change_conversation(id)

        self.chatbot.switch_llm(1)

    def chat(self, query: str) -> str:
        result = self.chatbot.query(query, stream=False)
        # result = str(result)
        return result
    
    def chatInfo(self) -> str:
        self.info = self.chatbot.get_conversation_info()
        print(self.info.id, self.info.title, self.info.model, self.info.system_prompt, self.info.history)
    
    def delChat(self):
        print("Chat deleted\n")
        self.chatbot.delete_all_conversations()

def speakResult(text: str):
    tts = gTTS(text=text, lang='en')

    au_filename = "out.mp3"
    tts.save(au_filename)
    playsound.playsound(au_filename)
    os.remove('./' + au_filename)
