from spack import *

class SpirvHeaders(CMakePackage):
    """Machine-readable files for the SPIR-V Registry"""

    homepage = "https://github.com/KhronosGroup/Spirv-Headers.git"
    git =  "https://github.com/KhronosGroup/Spirv-Headers.git"

    version('1.5.3', tag='1.5.3')

