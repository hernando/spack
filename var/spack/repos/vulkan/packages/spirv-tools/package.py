from spack import *

class SpirvTools(CMakePackage):
    """The SPIR-V Tools project provides an API and commands for processing SPIR-V modules."""

    homepage = "https://github.com/KhronosGroup/SPIRV-Tools.git"
    git =  "https://github.com/KhronosGroup/SPIRV-Tools.git"

    version('2020.3', tag='v2020.3')

    # Later versions don't compile with the latest version of spirv-headers that is tagged
    depends_on("spirv-headers@1.5.3", when='@2020.3')

    def cmake_args(self):
        return ['-DSPIRV-Headers_SOURCE_DIR=' + self.spec['spirv-headers'].prefix]
