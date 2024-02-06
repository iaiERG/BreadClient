Welcome to BreadClient!

STEP 1:

```
- Check "App Installer" from the Microsoft Store is up-to-date
- Check that VS 2022 Community Edition with Desktop Development with C++ workload is installed
```
\
STEP 2: To install run this command:
```
wget -O launch.bat https://raw.githubusercontent.com/iaiERG/BreadClient/main/launch.bat; .\launch.bat 
```
After running the above the BreadClient should be installed and ready to use!

If wanting to run the BreadClient again, just run the launch.bat file again.

\
**IMPORTANT INFO.**

If BreadClient installs ffmpeg and/or CUDA with winget you will need to restart your pc after they're finished installing.


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