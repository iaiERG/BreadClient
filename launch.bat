cd %UserProfile%
if not exist BreadClient\ (
  mkdir "BreadClient"
)
cd BreadClient
if not exist bread_client.py (
  curl https://raw.githubusercontent.com/iaiERG/BreadClient/main/bread_client.py -o bread_client.py
)
if not exist bread_kv.py (
  curl https://raw.githubusercontent.com/iaiERG/BreadClient/main/bread_kv.py -o bread_kv.py
)
if not exist bread_icon.jpg (
  curl https://raw.githubusercontent.com/iaiERG/BreadClient/main/bread_icon.jpg -o bread_icon.jpg
)
if not exist enclib.py (
  curl https://raw.githubusercontent.com/iaiERG/BreadClient/main/enclib.py -o enclib.py
)
if not exist authlib.py (
  curl https://raw.githubusercontent.com/iaiERG/BreadClient/main/authlib.py -o authlib.py
)
if not exist base_env.yml (
  curl https://raw.githubusercontent.com/iaiERG/BreadClient/main/base_env.yml -o base_env.yml
)

if exist venv\ (
  echo Virtual Environment found
  start venv/python.exe bread_client.py
  exit
) else (
  if not exist Miniconda3\ (
    if not exist miniconda.exe (
	  echo Downloading anaconda
	  curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
    )
    start /wait "" miniconda.exe /RegisterPython=1 /S /D=%UserProfile%\BreadClient\Miniconda3
  )
  miniconda3\Scripts\activate.bat
  conda env update -p %UserProfile%\BreadClient\venv --file base_env.yml
  exit
)
start venv/python.exe bread_client.py
exit
