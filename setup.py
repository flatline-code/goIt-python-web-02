from setuptools import setup, find_namespace_packages


setup(
      name='bot_assistant',
      version='1.0',
      description='Adding contact information of user',
      url='https://github.com/flatline-code/amigos-project',
      author='Amigos',
      author_email='info@amigos.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['bot-assistant = amigos_project:main']}
      )
