
import openai
import os
os.system('')
 
#注册的api_key
helper1="<ChatGPTHelper>"
print(helper1,"\n\033[1;32m您现在正在使用ChatGPT精简小工具(通用版),请确保您正确输入所有信息!Ctrl+C结束会话\033[0m")
ApiKey=input("\033[1;32m请输入您的有效ApiKey(登录https://openai.com/api/获取):\033[0m")
tp1="\033[1;33m请从下列模型中选择你想使用的模型\n[text-ada-001]\n[text-babbage-001]\n[text-curie-001]\n[text-davinci-002]\n[text-davinci-003(推荐)]\033[0m"
print(helper1,tp1)
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
    greeting0="\033[1;31m尝试载入模型,达芬奇-3模型支持多种语言,数据库时间限制:北京时间2021年\033[0m"
    greeting1="\n\033[1;34m正在调试,确保您的ApiKey可用,国内访问请不要使用Vpn,程序闪退可能是一下几种情况:\n1.网络问题,一般重启可以解决(国内网络波动较大时,可能多次失败)\n2.出入的ApiKey有误,获取ApiKey:https://openai.com/api\n3.选择的模型有误,目前支持的语言模型包括上面的五种,其他模型无法在此工具使用\033[0m"
    greeting4="\033[1;32m国内访问Api响应速度可能较慢,问题越难响应速度越慢,相应回答可能不够准确\033[0m"
    greeting2="\033[1;32mChatGpt尚处于开发阶段,请勿在问题中透露您的隐私信息！请不要询问有关于敏感话题信息,后果自负！\033[0m"
    greeting3="\033[1;33mVersion:beta2,测试作品非最终品质,工具开发者:LJM/Kalcite\033[0m"
    greeting="\033[1;31m我是ChatGPT交流机器人,我可以回答您的问题！如果您想退出,请输入:quit\033[0m"
    print()
    print('\033[1;31m<ChatGPTHelper>正在使用:\033[0m',modelT,greeting0)
    print()
    print(helper1,greeting1)
    print()
    print(helper1,greeting4)
    print(helper1,greeting2)
    print(helper1,greeting3)
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
            print("\033[1;31mChatGPT:感谢您的使用,已结束会话\033[0m")   
           
ask_question()
