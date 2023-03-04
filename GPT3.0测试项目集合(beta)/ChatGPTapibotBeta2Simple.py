
import openai
import os
os.system('')
 
#注册的api_key

ApiKey=input("\033[1;32m请输入您的有效ApiKey(登录https://openai.com/api/获取):\033[0m")
tp1="\033[1;33m请从下列模型中选择你想使用的模型\n[text-ada-001]\n[text-babbage-001]\n[text-curie-001]\n[text-davinci-002]\n[text-davinci-003(推荐)]\033[0m"
print(tp1)
model1=input("\033[1;32m请从上表中选择(复制粘贴到此处):\033[0m")


openai.api_key = ApiKey
def get_answer(question):
    
    response = openai.Completion.create(
    model=model1,
    prompt=question,
    temperature=0.5, 
    max_tokens=1024 )    
    return response.choices[0].text
 
def ask_question():
    flag=True
    modelT=model1
    greeting0="\033[1;31m数据库时间限制:北京时间2021年\033[0m"

    print()
    print('\033[1;31m<ChatGPTHelper>正在使用:\033[0m',modelT,greeting0)
    print()
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
            print("\033[1;31mChatGPT:感谢您的使用,已结束会话\033[0m")   
           
ask_question()
