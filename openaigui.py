import logging
import PySimpleGUI as sg
import openai
from openai import OpenAI
import os
import sys
import requests
from api_key import key
from imgnsound import icon

# @https://beta.client.com/docs/engines/gpt-3

client = OpenAI(api_key="12345678")
#api_base_url = ""
#api_base_url = ""


default_system_prompt_in="You are a helpful assistant."
system_prompt_in=default_system_prompt_in
logger = logging.getLogger()
logging.basicConfig(filename='log.txt', level=logging.INFO)

# max_tokens_list = (256, 8000)
max_tokens_list = [128,256, 3999, 7999]
models = ("sakura-13B-0.9","text-davinci-003", "text-davinci-002",
          "text-curie-001", "text-babbage-001", "text-ada-001")
size_list = ("256x256", "512x512", "1024x1024")
extra_query = {
    'do_sample': False,
    'num_beams': 1,
    'repetition_penalty': 1.0,
}
# Defines the modules() and openAi() functions which are used to select the engine and generate a response.


def modules(engines):
    return engines if engines in models else ValueError(f"Invalid engine: {engines}. Must be one of {models}")


def select_max_tokens(max_tokens):
    return max_tokens if max_tokens in max_tokens_list else ValueError(f"Invalid max_tokens: {max_tokens}. Must be one of {max_tokens_list}")



def openAi(prompt_in, engines, max_tokens):
    result=""
    sg.popup_quick_message('Responding...')
    user_prompt_in="""[Input]"""
    user_prompt_in = user_prompt_in.replace("[Input]", prompt_in)
    try:
        for completion in client.chat.completions.create(model="", messages=[
            {
                "role": "system",
                "content": f"{system_prompt_in}",
                "role": "user",
                "content": f"{user_prompt_in}"
            }
        ], temperature=0.1,
        top_p=0.3,
        max_tokens=select_max_tokens(max_tokens),
        frequency_penalty=0.0,
        seed=-1,
        extra_query=extra_query,
        stream=True):
            
            if completion.choices[0].finish_reason:
                print("\nfinish reason is", completion.choices[0].finish_reason)
                with open('answers.txt', 'a+',encoding='UTF-8') as f:
                    f.write(str(result))
                    f.write("\r\n")
            elif completion.choices[0].delta.content:
                print(completion.choices[0].delta.content, end="")
                result=result+str(completion.choices[0].delta.content)
    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")    


def testOpenAI():
    sg.popup_quick_message('Responding...')
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "If you recived the token, reply OK"}])
        print(response.choices[0].message.content)
        print("The server connected")
    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")


def make_window(theme):
    sg.theme(theme)
    
    # GUI layout.
    layout = [
        [sg.Text("OpenAIGUI",  expand_x=True, justification="center",
                 font=("Helvetica", 13), relief=sg.RELIEF_RIDGE)],
        [sg.TabGroup([[
            sg.Tab("OpenAI", [
                [sg.Text("Choose model:"), sg.Combo(
                    models, default_value=models[0], key="-ENGINES-", readonly=True)],
                [sg.Text("Choose max token"), sg.Combo(
                    max_tokens_list, default_value=max_tokens_list[0], key="-MAXTOKENS-", readonly=True)],
                    [sg.Text("API Url:"),sg.Input("http://192.168.1.157:8080",key='-APIURL-')],
                [sg.Text("User Prompt:",
                         font=('_ 13'))],
                [sg.Pane([sg.Column([[sg.Multiline(key="prompt", size=(77, 20), expand_x=True, expand_y=True, enter_submits=True, focus=True)]]),
                          sg.Column([[sg.Multiline(size=(60, 15), key="-OUTPUT-", font=("Arial", 9), expand_x=True, expand_y=True, write_only=True,
                                                   reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]])], expand_x=True, expand_y=True)],
                [sg.Button("Answer", bind_return_key=True), sg.Button('Open file'), sg.Button("Clear"), sg.Button("Quit"), sg.Button("Test")]]),
            sg.Tab("System Prompt", [
                [sg.Text("System Prompt:")],
                [sg.Pane([sg.Column([[sg.Multiline(f"{default_system_prompt_in}",key="-system_prompt-", size=(77, 20), expand_x=True, expand_y=True, enter_submits=True, focus=True)]], expand_x=True, expand_y=True)])],
                ]),
			sg.Tab("Theme", [
                [sg.Text("Choose theme:")],
                [sg.Listbox(values=sg.theme_list(), size=(
                    20, 12), key="-THEME LISTBOX-", enable_events=True)],
                [sg.Button("Set Theme")]]),
            sg.Tab("About", [
                [sg.Text(
                    "text-davinci-003 - Upgraded davinci-002. GPT3 chatbot model.")],
                [sg.Text(
                    "text-davinci-002 - Code review, complex intent, cause and effect, summarization for audience")],
                [sg.Text(
                    "code-davinci-edit-001 - Edit endpoint is particularly useful for editing code.")],
                [sg.Text(
                    "text-curie-001 - Language translation, complex classification, text sentiment, summarization")],
                [sg.Text(
                    "text-babbage-001 - Moderate classification, semantic search classification")],
                [sg.Text(
                    "text-ada-001 - Parsing text, simple classification, address correction, keywords")]
							]
					)
					]], key="-TAB GROUP-", expand_x=True, expand_y=True),
         sg.Sizegrip()]]
    # Gui window and layout sizing.
    window = sg.Window('OpenAI GUI', layout, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, icon=icon, finalize=True)
    window.set_min_size(window.size)
    return window


# GUI window that runs the main() function to interact with wthe user.
def main():
    window = make_window(sg.theme())
    # Event loop.
    while True:
        event, values = window.read(timeout=None)
        if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Exit':
            break
        if values is not None:
            engines = values['-ENGINES-']
        if values is not None:
            max_tokens = values['-MAXTOKENS-']
        if values is not None:
            api_base_url=values['-APIURL-']
            client.base_url=api_base_url+"/v1"
        if values is not None:
            system_prompt_in=values['-system_prompt-']
        if event == 'Answer':
            prompt_in = values['prompt'].rstrip()
            window['prompt'].update(prompt_in)
            window['-OUTPUT-'].update('')
            openAi(prompt_in, engines, max_tokens)
        elif event == 'Test':
            window['-OUTPUT-'].update('')
            testOpenAI()
        elif event == 'Open file':
            os.startfile('answers.txt', 'open')
        elif event == 'Clear':
            window['prompt'].update('')
            window["-OUTPUT-"].update('')
        elif event == "Set Theme":
            theme_chosen = values['-THEME LISTBOX-'][0]
            window.close()
            window = make_window(theme_chosen)
            sg.user_settings_set_entry('-theme-', theme_chosen)
            sg.popup(f"Chosen Theme: {str(theme_chosen)}", keep_on_top=True)

        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(
            ), location=window.current_location(), keep_on_top=True, non_blocking=True)

    window.close()
    sys.exit(0)


if __name__ == '__main__':
    sg.theme(sg.user_settings_get_entry('-theme-', 'dark green 7'))
    main()
