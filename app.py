# import requests
# import json
# import gradio as gr

# url="http://localhost:11434/api/generate"

# headers={

#     'Content-Type':'application/json'
# }

# history=[]

# def generate_response(prompt):
#     history.append(prompt)
#     final_prompt="\n".join(history)

#     data={
#         "model":"codeguru",
#         "prompt":final_prompt,
#         "stream":False
#     }

#     response=requests.post(url,headers=headers,data=json.dumps(data))

#     if response.status_code==200:
#         response=response.text
#         data=json.loads(response)
#         actual_response=data['response']
#         return actual_response
#     else:
#         print("error:",response.text)


# interface=gr.Interface(
#     fn=generate_response,
#     inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
#     outputs="text"
# )
# interface.launch()

# import requests
# import json
# import gradio as gr

# url = "http://localhost:11434/api/generate"
# headers = {'Content-Type': 'application/json'}
# history = []

# def generate_response(prompt):
#     history.append(prompt)
#     final_prompt = "\n".join(history)
#     data = {
#         "model": "codeguru",
#         "prompt": final_prompt,
#         "stream": False
#     }

#     try:
#         response = requests.post(url, headers=headers, data=json.dumps(data))
#         response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
#         data = response.json()
#         actual_response = data.get('response', 'No response field in JSON')
#         return actual_response
#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {e}"

# interface = gr.Interface(
#     fn=generate_response,
#     inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
#     outputs="text"
# )
# interface.launch()


import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codeguru",
        "prompt": final_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"API Response Status Code: {response.status_code}")
        print(f"API Response Text: {response.text}")
        
        if response.status_code == 200:
            data = response.json()  # use .json() instead of .loads(response.text)
            actual_response = data.get('response')
            if actual_response:
                print(f"Generated Response: {actual_response}")
                return actual_response
            else:
                return "No response found in API output."
        else:
            return f"Error: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
    outputs="text"
)

interface.launch()
