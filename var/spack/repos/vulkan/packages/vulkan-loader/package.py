from spack import *

class VulkanLoader(CMakePackage):
    """This project provides the Khronos official Vulkan ICD desktop loader for Windows, Linux, and MacOS."""

    homepage = "https://github.com/KhronosGroup/Vulkan-Loader.git"
    git = "https://github.com/KhronosGroup/Vulkan-Loader.git"

    version('1.2.154', tag='v1.2.154')
    version('1.1.130', tag='v1.1.130')

    depends_on('vulkan-headers@1.2.154', when='@1.2.154')
    depends_on('vulkan-headers@1.1.130', when='@1.1.130')

    depends_on('libxcb')


