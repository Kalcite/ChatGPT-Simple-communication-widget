
import openai
import os
import win32gui, win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
os.system('')
#我们的程序只支持自定义对话参数，不支持自定义回复参数，除了必要的APIkey等其余的皆为对话参数（比如模型和token上限）
#注册的api_key
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
#读取参数
print("\n您现在正在使用ChatGPT精简小工具(通用版),请确保您正确输入所有信息!Ctrl+C结束会话")
ApiKey = input("请输入您的有效ApiKey(登录https://openai.com/api/获取):")
tp1 = "请从下列模型中选择你想使用的模型\n[text-ada-001]\n[text-babbage-001]\n[text-curie-001]\n[text-davinci-002]\n[text-davinci-003(推荐)]"
print(tp1)
model1 = input("请从上表中选择(复制粘贴到此处):")
print()
#请注意你的token值！这关系到你的账户额度，token数和字符呈正相关字符，一个英文字母或半角符号=1token，一个中文或全角符号=2token，下面设置的token指的是包括发送和输出的token
#davinci的token价格大概是¥0.14以前个token($0.02=1000token)每个人的账户在前18个月内预装了18美元(约900000个token)
#https://platform.openai.com/tokenizer 这是一个token计算器,可以估算你的对话价值(不会真的有人掐着手指头算余额吧不会吧)

tokentip1 = "如果你的问题足够复杂那么接受过多的字符将会大幅度增加你的token消耗量,\n一个英文字母或半角符号=1token,一个中文=2token\n"
print(tokentip1)
token1 = int(input("请输入token上限(推荐1~256)(数据类型为整数):"))
print()
tempsettip = "temperature值介于 0 和 2 之间。\n较高的值(如 0.8)将使输出更加随机，而较低的值(如 0.2)将使其更加集中和确定。\n"
print(tempsettip)
temperatureset = float(input("请输入你的temperature值数据类型为浮点数:"))

#关于以上参数在最下面的注释中均有说明，这里提供几个示例代码
#                关于示例请求
# curl https://api.openai.com/v1/completions \
#   -H 'Content-Type: application/json' \
#   -H 'Authorization: Bearer YOUR_API_KEY' \
#   -d '{
#   "model": "text-davinci-003",
#   "prompt": "Say this is a test",
#   "max_tokens": 7,
#   "temperature": 0
# }'
#                  关于参数
# {
#   "model": "text-davinci-003",
#   "prompt": "Say this is a test",
#   "max_tokens": 7,
#   "temperature": 0,
#   "top_p": 1,
#   "n": 1,
#   "stream": false,
#   "logprobs": null,
#   "stop": "\n"
# }
#               关于回复（响应）
# {
#   "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
#   "object": "text_completion",
#   "created": 1589478378,
#   "model": "text-davinci-003",
#   "choices": [
#     {
#       "text": "\n\nThis is indeed a test",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "length"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 5,
#     "completion_tokens": 7,
#     "total_tokens": 12
#   }
# }

#发送请求
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
    greeting0="尝试载入模型,达芬奇-3模型支持多种语言,数据库时间限制:2020年"
    greeting1="请确保您的ApiKey可用,国内访问请不要使用Vpn,程序闪退可能是一下几种情况:\n1.网络不佳,可以多试几次\n2.出入的ApiKey有误,获取ApiKey:https://openai.com/api\n3.选择的模型有误,目前支持的语言模型包括上面的五种,其他模型无法在此工具使用"
    greeting4="国内访问Api响应速度可能较慢,问题越难响应速度越慢,相应回答可能不够准确"
    greeting2="ChatGpt尚处于开发阶段,请勿在问题中透露您的隐私信息！请不要交流隐私或敏感话题"
    greeting3="Version:beta3,测试作品非最终品质,工具开发者:LJM/Kalcite"
    greeting="我是ChatGPT交流机器人,我可以回答您的问题！如果您想退出,请输入:quit"
    print()
    print('<ChatGPTHelper>正在使用:',modelT,greeting0)
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
            print(f"ChatGPT:{answer}")
            print()
 
        else:
            flag=False
            print()
            print("ChatGPT:感谢您的使用,已结束会话")   
           
ask_question()

# Request body：

# ===model===
# string
# Required
# ID of the model to use. You can use the List models API to see all of your available models, or see our Model overview for descriptions of them.

# ===prompt===
# string or array
# Optional
# Defaults to <|endoftext|>
# The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.

# Note that <|endoftext|> is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document.

# ===suffix===
# string
# Optional
# Defaults to null
# The suffix that comes after a completion of inserted text.

# ===max_tokens===
# integer
# Optional
# Defaults to 16
# The maximum number of tokens to generate in the completion.

# The token count of your prompt plus cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096).max_tokens

# ===temperature===
# number
# Optional
# Defaults to 1
# What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

# We generally recommend altering this or but not both.top_p

# ===top_p===
# number
# Optional
# Defaults to 1
# An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

# We generally recommend altering this or but not both.temperature

# ===n===
# integer
# Optional
# Defaults to 1
# How many completions to generate for each prompt.

# Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for and .max_tokensstop

# ===stream===
# boolean
# Optional
# Defaults to false
# Whether to stream back partial progress. If set, tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a message.data: [DONE]

# ===logprobs===
# integer
# Optional
# Defaults to null
# Include the log probabilities on the most likely tokens, as well the chosen tokens. For example, if is 5, the API will return a list of the 5 most likely tokens. The API will always return the of the sampled token, so there may be up to elements in the response.logprobslogprobslogproblogprobs+1

# The maximum value for is 5. If you need more than this, please contact us through our Help center and describe your use case.logprobs

# ===echo===
# boolean
# Optional
# Defaults to false
# Echo back the prompt in addition to the completion

# ===stop===
# string or array
# Optional
# Defaults to null
# Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.

# ===presence_penalty===
# number
# Optional
# Defaults to 0
# Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

# See more information about frequency and presence penalties.

# ===frequency_penalty===
# number
# Optional
# Defaults to 0
# Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

# See more information about frequency and presence penalties.

# ===best_of===
# integer
# Optional
# Defaults to 1
# Generates completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.best_of

# When used with , controls the number of candidate completions and specifies how many to return – must be greater than .nbest_ofnbest_ofn

# Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for and .max_tokensstop

# ===logit_bias===
# map
# Optional
# Defaults to null
# Modify the likelihood of specified tokens appearing in the completion.

# Accepts a json object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this tokenizer tool (which works for both GPT-2 and GPT-3) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

# As an example, you can pass to prevent the <|endoftext|> token from being generated.{"50256": -100}

# ===user===
# string
# Optional
# A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.