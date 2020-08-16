from spack import *


class Calf(AutotoolsPackage):

    homepage = "https://calf-studio-gear.org/"
    url = "https://github.com/calf-studio-gear/calf/archive/0.90.3.zip"

    version('0.90.3',     sha256='431a3f80d7f43628a0616aa95afab0792d8f2edd04f1d0825f2732bc8295e42b')
    version('0.90.2',     sha256='6cc90dd6f115a0f8a02af998200a996578140c6e5aad52fbf6df17c186db22c0')
    version('0.90.1',     sha256='9a1f3fed55f1b07f1ca69a59210de07fb9910662ab3c624e40d1c1ba047bc5d5')
    version('0.90.0',     sha256='2e83f37bafb569e5f3d18957e3bdabdd64d45d435d8614bee514007ffb4ef73c')
    version('0.0.60pre5', sha256='ef251d8f9afe1fdbcc04780eb4fed1f6a4cb2db8d9a3c94611deae8580b3ea66')
    version('0.0.60pre4', sha256='7114e2e7527353d2d4c50af7dabbb88578b25c75d79d535b89560f3d3e401df1')
    version('0.0.60pre3', sha256='79dba7c03dfa8bdac00773d563f219b9618cc30cb771afe5689a1107da1ad511')
    version('0.0.60pre2', sha256='63d3f4b6ce72c440e57f76475c1cdc914a9a6c3ad9a49dedec4b48db05b9cdcc')
    version('0.0.60pre1', sha256='ede2a2cad07df94663ed74124bb5b4bd7222b7d4764cce1a85a41c8b8e08d6b9')
    version('0.0.60',     sha256='f901ba65d995d87bdc29702bcc4fcfc25f5bf142c4c8ab7dcf0e9b4bbc987a9e')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('fluidsynth')
    depends_on('gtkplus@:2.24.32')
    depends_on('cairo@1.17.2:')
    depends_on('lv2')

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        return ['--enable-sse', '--enable-experimental']

