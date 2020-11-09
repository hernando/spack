from spack import *

class Qjackctl(AutotoolsPackage):

    homepage = "https://qjackctl.sourceforge.io/qjackctl-downloads.html#Downloads"
    url = "https://download.sourceforge.net/qjackctl/qjackctl-0.6.2.tar.gz"

    version('0.6.2', sha256="1ec77d0e8edac1b4d60a32a08d2f4329f90571801920cb48c6147e0eae6f50e6")

    depends_on("qt@5.12: +dbus +opengl")
    depends_on("alsa")
    depends_on("jack +dbus", type=("build", "link", "run"))
