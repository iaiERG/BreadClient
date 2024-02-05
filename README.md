Welcome to BreadClient!

STEP 1: To install first run this command:
```
wget -O launch.bat https://raw.githubusercontent.com/iaiERG/BreadClient/main/launch.bat; .\launch.bat 
```
STEP 2: Next after you see the prompt to follow step 2, do the below:
```
- Launch Anaconda Prompt (Miniconda3)
- type "cd BreadClient"
- type "conda env update -p %UserProfile%\BreadClient\venv --file env.yml"
- type "launch.bat"
```
After running the above the BreadClient should be installed and ready to use!

If wanting to run the BreadClient again, just run the launch.bat file again.

STEP 3: If prompted to update the BreadClient with NVIDIA dependencies, run the below:
```
- Launch Anaconda Prompt (Miniconda3)
- type "cd BreadClient"
- type "conda env update -p %UserProfile%\BreadClient\venv --file .\IlluminationSDK\environment.yml"
- type "launch.bat"
```

**IMPORTANT INFO.**

If BreadClient fails to run winget, you will need to update your "App Installer" from the Microsoft Store.

If BreadClient installs ffmpeg and/or CUDA with winget you will need to restart your pc after they're finished installing.

If BreadClient fails to install NVIDIA dependencies, you will need to install VS 2022 Community Edition with Desktop Development with C++ workload


\
\
\
Full debug path (Order of installing important):
```
- Install BreadClient, run once and login, then close
- Install VS 2022 Community Edition with Desktop Development with C++ workload
- Update App Installer from Microsoft Store
- winget install FFmpeg -e
- winget install --id=Nvidia.CUDA -e
- Restart PC
- Relaunch BreadClient
```