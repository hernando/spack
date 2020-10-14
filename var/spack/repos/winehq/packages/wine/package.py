from spack import *

class Wine(AutotoolsPackage):
    """Wine (originally an acronym for "Wine Is Not an Emulator") is a
    compatibility layer capable of running Windows applications on several
    POSIX-compliant operating systems, such as Linux, macOS, & BSD.

    Notes:
    - This recipe builds the 64 bit variant of Wine with D3D support.
    - The 32 bit variant is not available as it requires a 32 bit version of
      all dependencies. There are some challenges challenging as Spack provided
      compilers have multilib support disabled on purpose, a system provided
      compiler must be used instead. The question that remains is how to express
      that the compiler must the 32 bit option when compiling the dependencies.
    - A WoW64 build is the ideal one for audio applications, but this is even
      more challenging.

      More information about how to compile the 32 bit and WoW64 variants can
      be found here: https://wiki.winehq.org/Building_Wine
    """

    homepage = "http://www.winehq.org"
    url      = "https://dl.winehq.org/wine/source/5.x/wine-5.15.tar.xz"

    version('5.18', sha256='9001f488651a9beb83a1cddf230dc0e79c708847f2ffc7de5cc20469e265f342')
    version('5.15', sha256='3f267cfcd4775bfdeddb1b2a592b875291f5e2dccdebce55f9b2012f7c670915')
    version('5.0.1', sha256='3f267cfcd4775bfdeddb1b2a592b875291f5e2dccdebce55f9b2012f7c670915')

    build_directory = 'build'

    depends_on('alsa')
    depends_on('bison')
    depends_on('dbus')
    depends_on('flex')
    depends_on('fontconfig')
    depends_on('freetype')
    depends_on('gnutls')
    depends_on('libpng')
    depends_on('libusb')
    depends_on('libx11')
    depends_on('libxcomposite')
    depends_on('libxcursor')
    depends_on('libxi')
    depends_on('libxinerama')
    depends_on('libxslt')
    depends_on('mesa +osmesa ~glx ~llvm')
    depends_on('vkd3d')

    def configure_args(self):
        args = ["--disable-win16"]
        args.append("--enable-win64")
        return args

