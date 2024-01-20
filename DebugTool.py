""" ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀
⣿⣩⣿⣉⣉⣉⠉⠉⠉⠉⠉⠉⠙⣷⣄⠀
⠀⠀⢈⡟⢸⡟⣷⠀⠀⠀⠀⠀⡾⠋⠀⠀
⠀⠀⣾⣵⠟⠀⣿⠛⠛⠛⠛⢻⡇⠀⠀⠀
⠀⠀⠈⠁⠀⠀⣿⠛⠛⠛⠛⠛⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠸⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⢻⡄⠀
⠀⠀⠀⠀⠀⠀⢀⡟ JakeR⠈⣷⠀
⠀⠀⠀⠀⢀⡾⠃IlloomAI⢹⡆
⠀⠀⠀⠀⢠⡾⢁⡴⠒⠒⠒⠒⠲⣦⠘⣧
⠀⠀⠀⢠⡟⢠⡟⠁AISDK⣿⠀⣿
⠀⠀⠀⣿⢀⡟⠀  BUG  ⣿⠀⣿
⠀⠀⢰⡇⢸⣇Remover⢀⣿⠀⣿
⠀⠀⠈⢧⣀⣉⣉⣉⣉⣉⣉⣉⣉⣁⣠⡟
⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀ """
import subprocess
import platform
import GPUtil



def GetBestAccelerator():
    """
    Finds and returns the best AI Accelerator in the system
    This is usually the most powerful GPUs however I anticipate AI
    accelerators will be large soon.
    :return: best attached AI Accelerator i.e. NVIDIA, RTX 3090, 24GB VRAM
    """

    match len(GPUtil.getGPUs()):
        case 0:
            print("No GPUs found, only the CPU is available.")
            return {"name": None,
                    "manufacturer": None,
                    "vram": 0,
                    "score": -9999}
        case 1:
            gpu = GPUtil.getGPUs()[0]
            # print(f"""VRAM: {gpu.memoryTotal} MB\nManufacturer: {gpu.name.split()[0]}\nCard: {gpu.name}""")
            return {"name": gpu.name, "manufacturer": gpu.name.split()[0], "vram": gpu.memoryTotal, "score": "-1"}
        case _:
            print("Multiple GPUs found, finding best GPU.")
            scoring = {"NVIDIA": 1000000, "AMD": 500000}
            gpu_scores = []
            for gpu in GPUtil.getGPUs():
                gpu_scores.append({"name": gpu.name,
                                   "manufacturer": gpu.name.split()[0],
                                   "vram": gpu.memoryTotal,
                                   "score": scoring.get(gpu.name.split()[0], 0) + gpu.memoryTotal})
            gpu_scores = sorted(gpu_scores, key=lambda x: x['score'], reverse=True)
            print(f"✓ - Found best GPU as {gpu_scores[0]['name']} (VRAM - {gpu_scores[0]['vram']})")
            return gpu_scores[0]



def _check_rocm_installed():
    """
    Check if ROCm is installed on linux.
    :return:
    """
    try:
        subprocess.run(["pip", "show", "roccl"], check=True)
        return True
    except FileNotFoundError:
        return False


def _check_rocm_support(GPU):
    """
    Checks if ROCm is supported
    :return:
    """

    '''Windows only code, we do not support ROCm on windows due to pytorch not working
    ROCmCards = {"6600", "6600 XT", "6650 XT", "6700", "6700 XT", "6750", "6800", "6800 XT", "6900 XT",
                "6950 XT", "7600", "7900 XT", "7900 XTX", "VII", "W5500", "W6600", "W6800", "W7800", "W7900"}

    print("Checking your card supports ROCm...")
    if any(card in GPU['name'] for card in ROCmCards):
        print(f"✓ Your card {GPU['name']}, appears to support ROCm on wid!")
    else:
        print(f"""✗ Your card {GPU['name']} does not appear to support ROCm
Check https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html to confirm
if your card does support ROCm, please contact Jake.""")'''

    os_name = platform.system()
    if os_name == "Windows":
        print("✗ - AI SDK does not support windows at this time as pytorch does not support ROCm on windows.")
    elif os_name == "Darwin":
        print("😂 - MAC USER FOUND, LAUGH!")
    else:
        print("✓ - AI SDK supports linux; checking card compatability.")
        ROCm_Cards = ["W7900", "W6800", "V620", "VII", "7900 XTX", "7900 XT"]
        if any(card in GPU['name'] for card in ROCm_Cards):
            print(f"✓ Your card {GPU['name']}, appears to support ROCm on linux!")
            return True
        else:
            print(f"""✗ Your card {GPU['name']} does not appear to support ROCm on Linux.
    Check https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html to confirm
    if your card does support ROCm, please contact Jake.""")
    return False


if __name__ == '__main__':
    print("You are running AISDK Debug Tool as the main file, checking your system works.")
