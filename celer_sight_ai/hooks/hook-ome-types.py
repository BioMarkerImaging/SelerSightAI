from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('ome_types', include_py_files=True)