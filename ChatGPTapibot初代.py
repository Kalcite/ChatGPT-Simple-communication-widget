
import openai
import os
os.system('')
 
#注册的api_key
ApiKey=input("\033[1;32m请输入您的有效ApiKey(登录https://openai.com/api/获取):\033[0m")
openai.api_key = ApiKey
def get_answer(question):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.5, 
    max_tokens=1024 )    
    return response.choices[0].text
 
def ask_question():
    flag=True
    greeting="\033[1;31m我是ChatGPT交流机器人,我可以回答您的大部分问题！如果您想退出,请输入:quit\033[0m"
    print()
    print(greeting)
    print()
    while(flag==True):
        question = input()
        if(question!='quit'):
            answer=get_answer(question)
            answer = answer[2:]
            print()
            print(f"\033[1;31mChatGPT:{answer}\033[0m")
            print()
 
        else:
            flag=False
            print()
            print("\033[1;31mChatGPT:感谢您的使用,完整功能请访问官网\033[0m")   
           
ask_question()
