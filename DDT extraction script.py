import os
import pathlib
import subprocess

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable) + '\\'
elif __file__:
    application_path = os.path.dirname(__file__) + '\\'

tools = ["tools\\TextureExtractor.exe", "tools\\TextureCompiler.exe"]
folders = ["1 - originals\\", "2 - to edit\\", "3 - edited\\"]
tool = ""
in_d = ""
out_d =  ""
compressing = False

for d in folders:
    if not os.path.exists(application_path + d):
        pathlib.Path(application_path + d).mkdir(parents=True, exist_ok=True)
        print("Created folder: " + application_path + d)
    d.join((application_path,d))

for t in tools:
    if not os.path.isfile(application_path + t):
        print("tools not found, tools are in the game folder..\nPlease make a copy of the folder, here.\nPress enter to quit...")
        input()
        sys.exit()()
    t.join((application_path, t))

while(1):
    choose = input("\nType e for extracting \nType c for compressing \nAnything else to exit...\n")
    if choose == "c":
        tool = tools[1]
        in_d = folders[1]
        out_d = folders[2]
        compressing = True
    elif choose == "e":
        tool = tools[0]
        in_d = folders[0]
        out_d = folders[1]
        compressing = False
    else:
        sys.exit()()

    for d in folders:
        if not os.path.exists(d):
            pathlib.Path(d).mkdir(parents=True, exist_ok=True)
            print("Created folder: " + d)

    for t in tools:
        if not os.path.isfile(t):
            print("tools not found, tools are in the game folder..\nPlease make a copy of the folder, here.\nPress enter to quit...")
            input()
            sys.exit()()

    for filename in os.listdir(in_d):
        f = os.path.join(in_d, filename)
        if os.path.isfile(f):
            in_f = in_d + filename
            out_f = out_d + filename[:-3]
            if compressing:
                out_f += 'ddt'
            else:
                out_f += 'tga'
            if not compressing and os.path.isfile(out_f):
                print("Skipping " + f)
                continue
            subprocess.call([tool,'-i',in_f,'-o',out_f])
    print()
