
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
    greeting0="\033[1;31m进行调试,该模型仅支持中文,目前模型时间限制:北京时间2020年7月17日下午2点19分,新模型等待更新)\033[0m"
    greeting1="\033[1;32m开始调试,确保您的ApiKey可用,国内访问请不要开启Vpn/梯子,若程序闪退为网络问题,请重启(国内网络波动较大,可能多次失败)\033[0m"
    greeting4="\033[1;32m请注意:如果程序报错或者异常退出请先检查自身网络情况,国内访问Api响应速度可能较慢,问题越难响应时间越长,若载入后直接退出请检查Api是否可用\033[0m"
    greeting2="\033[1;32mChatGpt尚处于开发阶段,请勿在问题中透露您的隐私信息！请不要询问有关于敏感话题信息,后果自负！\033[0m"
    greeting3="\033[1;33m测试作品非最终品质,开发者LJm/Kalcite\033[0m"
    greeting="\033[1;31m我是ChatGPT交流机器人,我可以回答您的大部分问题！如果您想退出,请输入:quit\033[0m"
    print()
    print('\033[1;31m正在使用：\033[0m',modelT,greeting0)
    print(greeting1)
    print(greeting4)
    print(greeting2)
    print(greeting3)
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
