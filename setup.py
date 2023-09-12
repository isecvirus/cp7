from cx_Freeze import setup, Executable

setup(
    name="cpd",
    version="1.0.0",
    description="Cisco password type 7 decipher",
    executables=[Executable("cpd.py")],
)