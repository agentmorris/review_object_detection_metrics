from setuptools import find_packages, setup

setup(
    name='object_detection_metrics',
    packages=find_packages(),
    version='0.1.0',
    description='Tools for computing object detection metrics',
    author='Rafael Padilla',
    license='MIT',
    install_requires=[
        'numpy',
        'pandas',
        'opencv-python',
        'matplotlib',
        'tqdm'
    ]    
)
