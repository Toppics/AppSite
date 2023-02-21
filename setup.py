from cx_Freeze import setup, Executable

options = {
    'build_exe': {    
        'build_exe': './/build',
        'packages':["os","sys","shutil","time","random","string","webbrowser","tkinter","PIL","resizeimage"],
        'include_files': ["favicon.ico","AppSite.png",".needs"],
        'include_msvcr': True,
    },
}

setup(
    name = "AppSite",
    options = options,
    version = "1.1.1",
    description = 'AppSite.ile-segal.com',
    executables = [Executable(script="AppSite 1.1.1.py", copyright= "Copyright © 2021 Ile-segal.com", icon = "favicon.ico", base= "Win32GUI")]
)