from setuptools import find_packages, setup

package_name = 'projet_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'Flask', 'rospy', ],
    zip_safe=True,
    maintainer='thogms',
    maintainer_email='thogms@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'publisher_temperature = projet_pkg.publisher_temperature:main',
		'publisher_luminosity = projet_pkg.publisher_luminosity:main',
		'publisher_time = projet_pkg.publisher_time:main',
		'publisher_presenceInt = projet_pkg.publisher_presenceInt:main',
		'publisher_presenceOut = projet_pkg.publisher_presenceOut:main',
		
		'controle_temperature = projet_pkg.controle_temperature:main',
		'controle_luminosity = projet_pkg.controle_luminosity:main',
		'controle_time = projet_pkg.controle_volet:main',
		'controle_presenceInt = projet_pkg.controle_alarme:main',
		'controle_presenceOut = projet_pkg.controle_buzzer:main',
		
		'client_bp = projet_pkg.client_bp:main',
		'service_bp = projet_pkg.service_bp:main',
		
		'info_web = projet_pkg.info_web:main',
		
        ],
    },
)
