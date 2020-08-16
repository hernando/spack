from spack import *

class Taglib(CMakePackage):

    homepage = "http://taglib.org"
    url = "https://taglib.org/releases/taglib-1.11.1.tar.gz"

    generator='Ninja'

    version("1.11.1", sha256="b6d1a5a610aae6ff39d93de5efd0fdc787aa9e9dc1e7026fa4c961b26563526b")

    depends_on('cmake@3.0:', type='build')
    depends_on('ninja', type='build')

    def cmake_args(self):
        return [self.define('BUILD_SHARED_LIBS', 'ON')]
