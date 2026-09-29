# PyInstaller build for the standalone FSOC app.
#   pip install pyinstaller
#   pyinstaller fsoc_app.spec
# Output: dist/FSOC_Tracker/FSOC_Tracker(.exe)  - ship the whole folder.
from PyInstaller.utils.hooks import collect_submodules

a = Analysis(
    ["launcher.py"],
    pathex=["."],
    datas=[("web/dist", "web/dist"), ("beacon_yolo.pt", ".")],
    hiddenimports=[
        'uvicorn',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        'engineio.async_drivers.asgi',
        'server.app',
        'server.__main__',
    ] + collect_submodules("websockets"),
    # torch/ultralytics are optional (YOLO); excluding them keeps the app small.
    excludes=["torch", "torchvision", "ultralytics", "matplotlib", "PyQt5", "tkinter"],
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="FSOC_Tracker", console=True)
coll = COLLECT(exe, a.binaries, a.datas, name="FSOC_Tracker")
