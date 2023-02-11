
import openai
import os
import win32gui, win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
os.system('')

print("""
           .d88888b.             
         .8P"     "9bd888b.      
        .8P     .d8P"   `"988.   
     .8888   .d8P"    ,     98.  
   .8P" 88   8"    .d98b.    88  
  .8P   88   8 .d8P"   "98b. 88  
  88    88   8P"  `"8b.    "98.  
  88.   88   8       8"8b.    88 
   88    "98.8       8   88   "88
    `8b.    "98.,  .d8   88    88
    88 "98b.   .d8P" 8   88   d8"
    88    "98bP"    .8   88 .d8" 
    "8b     `    .d8P"   8888"   
     "88b.,   .d8P"     d8"      
       "9888P98b.     .d8"       
               "988888P"         
""")

print("\n\033[1;32m您现在正在使用ChatGPT精简小工具(通用版),请确保您正确输入所有信息!Ctrl+C结束会话\033[0m")
ApiKey = input("\033[1;32m请输入您的有效ApiKey(登录https://openai.com/api/获取):\033[0m")
tp1 = "\033[1;33m请从下列模型中选择你想使用的模型\n[text-ada-001]\n[text-babbage-001]\n[text-curie-001]\n[text-davinci-002]\n[text-davinci-003(推荐)]\033[0m"
print(tp1)
model1 = input("\033[1;32m请从上表中选择(复制粘贴到此处):\033[0m")
print()

tokentip1 = "\033[1;33m如果你的问题足够复杂那么接受过多的字符将会大幅度增加你的token消耗量,\n一个英文字母或半角符号=1token,一个中文=2token\n\033[0m"
print(tokentip1)
token1 = int(input("\033[1;32m请输入token上限(推荐1~256)(数据类型为整数):\033[0m"))
print()
tempsettip = "\033[1;33mtemperature值介于 0 和 2 之间。\n较高的值(如 0.8)将使输出更加随机，而较低的值(如 0.2)将使其更加集中和确定。\n\033[0m"
print(tempsettip)
temperatureset = float(input("\033[1;32m请输入你的temperature值数据类型为浮点数:\033[0m"))


openai.api_key = ApiKey
def get_answer(question):
    
    response = openai.Completion.create(
    model=model1,
    prompt=question,
    temperature=temperatureset, 
    max_tokens=token1 )    
    return response.choices[0].text
 
#接受回答
def ask_question():
    flag=True
    modelT=model1
    greeting0="\033[1;31m尝试载入模型,达芬奇-3模型支持多种语言,数据库时间限制:2020年\033[0m"
    greeting1="\n\033[1;34m请确保您的ApiKey可用,国内访问请不要使用Vpn,程序闪退可能是一下几种情况:\n1.网络不佳,可以多试几次\n2.出入的ApiKey有误,获取ApiKey:https://openai.com/api\n3.选择的模型有误,目前支持的语言模型包括上面的五种,其他模型无法在此工具使用\033[0m"
    greeting4="\033[1;32m国内访问Api响应速度可能较慢,问题越难响应速度越慢,相应回答可能不够准确\033[0m"
    greeting2="\033[1;32mChatGpt尚处于开发阶段,请勿在问题中透露您的隐私信息！请不要交流隐私或敏感话题\033[0m"
    greeting3="\033[1;33mVersion:beta3,测试作品非最终品质,工具开发者:LJM/Kalcite\033[0m"
    greeting="\033[1;31m我是ChatGPT交流机器人,我可以回答您的问题！如果您想退出,请输入:quit\033[0m"
    print()
    print('\033[1;31m<ChatGPTHelper>正在使用:\033[0m',modelT,greeting0)
    print()
    print(greeting1)
    print()
    print(greeting4)
    print(greeting2)
    print(greeting3)
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

