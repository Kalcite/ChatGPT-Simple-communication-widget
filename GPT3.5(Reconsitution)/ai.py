import openai
import os
import sys

#
# 参数详情：https://zhuanlan.zhihu.com/p/606573556
# 官方文档：
# https://platform.openai.com/docs/api-reference/chat/create?lang=python
# https://platform.openai.com/docs/guides/chat
# https://platform.openai.com/tokenizer

os.system('')
# 替换为自己的API Key
print("\n\033[1;34m 该版本为测试版，调试命令:clr,edit,dellog，作用大致分为清除[clr]/删除[dellog]log.txt，编辑/生成[edit]log.txt文件，该文件储存日志并初始化对话 \033[0m")
apikey_set = input("\n\033[1;32m 请输入Key： \033[0m")
openai.api_key = apikey_set
temperatureset = float(input("\n\033[1;32m 请输入temperature值，该值越大创造性越强数值为0~2的小数： \033[0m"))
print("\n\033[1;32m 关于监听(stream)：\n监听模式[stream = True]模式适用于在会话期间实时地逐步生成响应的情况。在该模式下，由于API必须一直等待下一个消息，因此可能看起来像在阻塞主线程。\n当非监听模式下[stream = False]时，Chat API将在单个请求中生成完整的响应。因此，使用该模式可能会在性能上产生一些优势。 \033[0m")

# Function to send a message to the OpenAI chatbot model and return its response
def send_message(message_log):
    # print(f'The message_log is {message_log}') # 输出发送的消息，调试用

    # 调用openai提供的ChatCompletion API获取chatgpt的应答
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 必要，模型名字
        messages=message_log,   # 必要，消息内容
        #temperature=temperatureset,        # 可选，默认为1，0~2，数值越高创造性越强
        # top_p = 0.5,           # 可选，默认为1，0~1，效果类似temperature，不建议都用
        # n = 3,                  # 可选，默认为1，chatgpt对一个提问生成多少个回答
        #stream = True        # 可选，默认False，设置为True和网页效果类似，需监听事件来解析
        # stop = '花',              # 可选，chatgpt遇到stop里的字符串时停止生成内容（且不返回应答？）
        # max_tokens=4048,        # 可选，默认无穷大，回复的最大长度，如果设置了，需要满足max_tokens+message_tokens<=4096
        # presence_penalty = 2,   # 可选，默认为0，-2~2，越大越允许跑题
        # frequency_penalty = 1.8,  # 可选，默认为0，-2~2，越大越不允许复读机
        # logit_bias = None,      # 可选，默认无，影响特定词汇的生成概率？
        # user = 'xy123',              # 可选，默认无，用户名       
    )

    print(response)

    # return response.choices[0].message.content
    return [choice.message.content for choice in response.choices]


# 将字典列表格式化存储
def save_log(message_log):
    with open('log.txt', 'w') as f:

        text = ''
        for message in message_log:
            text += f"{message['role']}:{message[r'content']}\n"
        
        f.write(text)


# 清除log.txt（调试用）
def clr(file_name):
    try:
        file_path = os.path.join(file_name)
        with open(file_path, 'w') as f:
            f.seek(0)
            f.truncate()
        print("File content cleared successfully!")
    except Exception as e:
        print("Failed to clear file content: {}".format(str(e)))

#删除log.txt（调试用）
def dellog(file_name):
    try:
        file_path = os.path.join(file_name)
        os.remove(file_path)
        print("File deleted successfully!")
    except Exception as e:
        print("Failed to delete file: {}".format(str(e)))

#查询账户工作单元
# def get_used_work_units(api_key):
#     openai.api_key = api_key
#     response = openai.Usage.list()
#     used_work_units = response['data'][0]['work_units']
#     return used_work_units
# 字符串转字典列表

def read_log(file_path):
    with open(file_path, 'r') as f:
        role, content, logs = '', '', []

        while True:
            line = f.readline()
            if not line:
                logs.append({'role':role, 'content':content})
                break
            if line.startswith('system:') or line.startswith('user:') or line.startswith('assistant:'):
                if content != '':
                    logs.append({'role':role, 'content':content})
                role = line[:line.find(':')]
                content = line[line.find(':')+1:]
            else:
                content += line

    # print('logs are ', logs) #输出字典列表，调试用
    return logs


# Main function that runs the chatbot
def main():
    AutoDelete = True
    # 启动后读取log文件作为初始化内容，没有则新建
    try:
        message_log = read_log('log.txt')
    except:
        message_log = [
            # {"role": "system", "content": "You are a helpful assistant."}
            {"role": "system", "content": "你是一只名为Kalcite的猫娘，说话时喜欢带喵~"}
        ]
    print("\033[1;32m 以下是初始化消息(可以理解为ai的自我暗示):\nInit message:\n \033[0m\n",message_log)
    # Start a loop that runs until the user types "QUIT"
    while True:

        # If this is not the first request, get the user's input and add it to the conversation history
        user_input = input("You: ")

        # If the user types "QUIT", end the loop and print a goodbye message
        if user_input == "quit":
            print("Goodbye!")
            save_log(message_log)
            break
        elif user_input == "edit":
            save_log(message_log)
            input("Edit your log file now\n")
            message_log = read_log('log.txt')
        elif user_input == "clr":
            save_log
            print("\033[1;33m 警告：继续操作将清除log.txt日志及配置文件（重新启动此程序会再次生成），如果你不知道此命令作用请不要尝试，操作结束后退出程序\n清除不代表删除，请在执行此命令后手动编辑或删除log.txt或使用dellog和edit命令，否则程序下次无法正常运行 \033[0m\n")
            if __name__ == '__main__':
                user_input = input("Enter 'y' to clear file content: ")
                if user_input.lower() == 'y':
                    clr('log.txt')
                    sys.exit(0)
                else:
                    print("Program stopped!")
                    sys.exit(0)
        elif user_input == "dellog":
            save_log
            print("\033[1;33m 警告：继续操作将删除log.txt日志及配置文件（重新启动此程序会再次生成），如果你不知道此命令作用请不要尝试，操作结束后退出程序 \033[0m\n")
            if __name__ == '__main__':
                user_input = input("Enter 'y' to clear file content: ")
                if user_input.lower() == 'y':
                    dellog('log.txt')
                    sys.exit(0)
                else:
                    print("Program stopped!")
                    sys.exit(0)
        # elif user_input == "unit":
        #     if __name__ == '__main__':
        #         api_key = apikey_set
        #         used_work_units = get_used_work_units(api_key)
        #         print("Used work units:", used_work_units)


        else:
            message_log.append({"role": "user", "content": user_input})


        responses = []
        try:
            # Send the conversation history to the chatbot and get its response
            responses = send_message(message_log)
        except openai.error.InvalidRequestError as e:
            print(e)
            save_log(message_log)
            input('Please edit your log file to continue chat!\n')
            message_log = read_log('log.txt')
            responses = send_message(message_log)
        except:  # openai.error.APIError, too many requests etc
            save_log(message_log)

        for response in responses:
            # Add the chatbot's response to the conversation history and print it to the console
            message_log.append({"role": "assistant", "content": response})
            print(f"AI assistant: {response}")


        if AutoDelete == True:
            if len(message_log) >= 4:
                message_log = [message_log[0]] + message_log[-2:]
                # 更好的策略？
                # 看下有没有压缩算法，概括算法？让chatgpt自己弄？

# Call the main function if this file is executed directly (not imported as a module)
if __name__ == "__main__":
    main()