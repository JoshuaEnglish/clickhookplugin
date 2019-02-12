from setuptools import setup

setup(
    name='chplugin',
    version='0.1dev0',
    py_modules=['chplugin'],
    entry_points='''
        [clickhook.new_commands]
        show = chplugin:show

        [clickhook.run_commands]
        cmd = chplugin:hooked
    ''',
)
