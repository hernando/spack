from spack import *

class Vkd3d(AutotoolsPackage):

    homepage = "http://www.winehq.org/Vkd3d"
    url      = "https://dl.winehq.org/vkd3d/source/vkd3d-1.2.tar.xz"

    version('1.2', sha256='b04b030fcbf0f2dacc933c76c74b449bffef1fc1a18d50254ef1ad3e380df96b')

    depends_on('vulkan-headers')
    depends_on('vulkan-loader')
    depends_on('spirv-tools@2020.3', when='@1.2')
