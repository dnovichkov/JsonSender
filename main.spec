# -*- mode: python -*-

# work-around for https://github.com/pyinstaller/pyinstaller/issues/4064
# import distutils
# if distutils.distutils_path.endswith('__init__.py'):
#     distutils.distutils_path = os.path.dirname(distutils.distutils_path)



import os
import shutil

dist_dir_name = 'dist'
shutil.rmtree(dist_dir_name)

import datetime
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')


block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[
             ('README.md', '.'),
             ('request__2022-05-31 11-35-56_.json', '.'),
             ('simple_request.json', '.'),
             ],
             hiddenimports=['win32timezone', 'logging', 'uvicorn.logging'],
             hookspath=['pyinstaller_hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')


archive_filename = 'dist_' + current_datetime
dist_dir_name += '/main'
shutil.make_archive(archive_filename, 'zip', dist_dir_name)


