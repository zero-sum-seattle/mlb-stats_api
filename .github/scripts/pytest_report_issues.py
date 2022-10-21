import sys
import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def cronbot_post_uka(slack_webclient_token, channel_id, message):

    # WebClient instantiates a client that can call API methods
    client = WebClient(token=slack_webclient_token)

    try:
        # Call the conversations.list method using the WebClient
        client.chat_postMessage(
            channel=channel_id,
            text="Failed Build Test for mlbstatsapi",
            attachments=
            [
                {
                    "color": "#9733EE",
                    "blocks": [                       
                        {
                            "type": "context",
                            "elements": [
                                {
                                    "type": "mrkdwn",
                                    "text": f"```\n{message}\n```"
                                }
                            ]
                        },                       
                    ]
                }
            ]
        )

    except SlackApiError as e:
        print(f"Error: {e}")


def escape_ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[@-~]')
    return ansi_escape.sub('', line)

def generate_outputstring(from_list) -> str:
    testing_output = ""

    for output in from_list:

        output = escape_ansi(output)

        if len(output) > 78:
        
            if output[:10] == "==========":
                output = output.replace("=", "")
                # print ([*output])
                output = '{:=^78}'.format(output[:-2]) + '\r\n'
            
            elif output[-8] == "[" and output[-3] == "]":
                if output[-12:-8] != "    ":
                    output[-15] = '.'
                    output[-14] = '.'
                    output[-13] = '.' 
                    output[-12] = ' '
                    output[-11] = ' '
                    output[-10] = ' '
                    output[-9]  = ' '
                output = output[:72] + output[-8:]
            
            elif output[:10] == "collecting":
                output = ' '.join(output[16:].split()[-3:]) + '\r\n'           
                
            elif output.split()[0] in short_test_summary_info_types:
                output_listified = output.split()
                output = ' '.join(output_listified[:2]) 
                output += '\r\n'

                temp_string = ' ' * (len(output_listified[0]))
                for word in output_listified[2:]:
                    if len(temp_string) + 1 + len(word) <= 78:
                        temp_string+=" " + word
                    else:
                        if len(word) > 78 - len(output_listified[0]) + 1:
                            for char in word:
                                if len(temp_string) >= 78:
                                    temp_string += '\r\n'
                                    output += temp_string
                                    temp_string = ' ' * (len(output_listified[0]) + 1)
                                    temp_string += char
                                else:
                                    temp_string += " " + char
                        else:
                            temp_string += '\r\n'
                            output += temp_string
                            temp_string = ' ' * (len(output_listified[0]) + 1)
                            temp_string += word

                output += temp_string
                output += '\r\n'

            else:
                output = output[:75] + "...\r\n"

        testing_output+=output

    return testing_output


if __name__ == "__main__":
    channelid = sys.argv[1]
    token = sys.argv[2]
    
    output_list = []

    short_test_summary_info_types = ["FAILED", "ERROR", "SKIPPED", 
                                    "XFAILED", "XPASSED", "PASSED"]

    for line in sys.stdin:
        output_list.append(line)

    if "failed" in line or "errors" in line or "error" in line:
        cronbot_post_uka(token, channelid, generate_outputstring(output_list))