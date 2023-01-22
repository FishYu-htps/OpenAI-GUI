# OpenAI-GUI

This is a graphical user interface (GUI) for interacting with various OpenAI models. With this GUI, you can easily run various language and machine learning models, such as GPT-3 and DALL-E, without needing to use the command line.

The program works. If you encounter problems running it or have other bug reports or features that you wish to see implemented, please fork the project and submit a pull request and/or file an [issue](https://github.com/MaxSSD/OpenAI-GUI/issues) on this project.

# TBD
1. Voice prompt on press or voice command.
2. Button binds for functionality (Enter, Esc, Delete)
3. Embeddings text input from https://beta.openai.com/docs/guides/embeddings/what-are-embeddings
4. Write to class

# Screenshots & Videos
openaigui.py

![Capture](https://user-images.githubusercontent.com/86234226/213918445-3d478d7e-00e6-4994-b887-2a90762be7ca.PNG)

![Capture1](https://user-images.githubusercontent.com/86234226/213918705-efe4739b-257c-4415-9125-89de45d35aa2.PNG)

![Dall-E Picture of grey cat smoking a cigar](https://user-images.githubusercontent.com/86234226/211488407-69a46796-f3b5-4796-9caa-33a4a8d005eb.PNG)

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites
In order to use this GUI, you will need to have a valid OpenAI API key. You can sign up for a free API key at the [OpenAI website](https://beta.openai.com/account/api-keys).

You will also need to have Python 3 installed on your machine. You can download Python 3 from the official [Python website](https://www.python.org/downloads/).

# Installation
To install the GUI, first clone the repository to your local machine:

```
git clone https://github.com/MaxSSD/OpenAI-GUI.git
```
Next, navigate to the root directory of the project and install the required dependencies:
```
cd OpenAI-GUI
pip install -r requirements.txt
```
# Usage
To run the GUI, simply enter the following command:
```
python openaigui.py
```
The GUI will then open in a new window. You can select the desired OpenAI model from the dropdown menu and enter your input in the text box. When you are ready, click the "Run" button to send your input to the model and view the results.

# Keyboard Shortcuts
| Key Combo                 | Effect                                             |
| ------------------------- | -------------------------------------------------- |
| Enter                     | Speak                                              |
| Esc                       | Quit                                               |
| Delete                    | Delete text                                        |


# Use ase
OpenAI based model GUI tool which displays a desktop prompt window for OpenAI GPT3

## Example/test command
1. Give 10 ideas for python automation implementations.
2. Review this code: "..."
3. Summarize this text: "..."

# Developer Information
## Known Working Versions of Dependencies for openaipysgui.py
* logging==0.5.1.2
* PySimpleGUI==4.60.4
* openai==0.16.0
* Pillow==9.2.0

## Developing a New Component
* File an issue on GitHub if you need help fitting your OpenAI-GUI into our component system; we would be happy to collaborate. We welcome contributions to this project! If you have an idea for a new feature or bug fix, please open a new issue and let us know.

# License
Source code of OpenAI-GUI is licensed under the [MIT License](https://github.com/MaxSSD/OpenAI-GUI/blob/main/LICENSE).
Some dependencies of this application are under the GPL license. When packaged with these dependencies, OpenAI-GUI may also be under the terms of this GPL license.
