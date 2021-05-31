# relativistic-addition
A presentation about the relativistic addition of velocities

# Requisites
- [Python 3.x](https://www.python.org/downloads/)
- [Manim](https://github.com/3b1b/manim) (the code works on version 0.6.0)
- [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases)
- [LaTeX](https://www.latex-project.org/get/) 

# Running
If you have every requisite listed above (on Windows, you must have everything added to `PATH`), by calling

```sh
manim src/video.py [SCENE NAME]
```

you should be able to generate every scene of the script one by one, or if you prefer

```sh
manim src/video.py -a
```

allows you to create every scene with one command.

The script of the video was made by using MiKTeX (and the VSCode LaTeX extension), and you can find the PDF file in the root of the repo as well.

# Other resources
You can find a [Desmos link](https://www.desmos.com/calculator/fa2rrfpa6x) in the first line of `src/video.py`, showing some of the graphs exaplained in detail in the presentation. Furthermore, you can check the whole [PowerPoint presentation](https://drive.google.com/file/d/11DevQtEEt29_GwlbLjNF7ROIAOxwsKuw/view?usp=sharing).
