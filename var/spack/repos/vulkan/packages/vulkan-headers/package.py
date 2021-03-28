from spack import *

class VulkanHeaders(CMakePackage):
    """This project provides the Khronos official Vulkan ICD desktop loader for Windows, Linux, and MacOS."""

    homepage = "https://github.com/KhronosGroup/Vulkan-Headers.git"
    git =  "https://github.com/KhronosGroup/Vulkan-Headers.git"

    version('1.2.172', tag='v1.2.172')
    version('1.1.130', tag='v1.1.130')

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set('VULKAN_HEADERS_INSTALL_DIR', self.prefix)

