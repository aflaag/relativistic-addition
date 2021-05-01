# relativistic-addition
A Manim project for the relativistic addition of velocity.

# Requisites
- [Python 3.x](https://www.python.org/downloads/)
- pip (latest version)
```sh
# download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# install pip with get-pip.py
python get-pip.py
```
- Manim (latest version)
```sh
# install manim (updated 05/01/2021, it may change in the future)
pip install manim
```
- [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases)
- [LaTex](https://www.latex-project.org/get/) 

# Run
If you have every requisite listed above (on Windows, you must have everything added to `PATH`), by calling

```sh
manim video.py [SCENE NAME]
```

you should be able to generate every scene of the script.

**Note**: if you didn't clone the repository, you must put `video.py` into a folder, and execute the command above from inside this folder (Manim generates animations under the specified folder).
