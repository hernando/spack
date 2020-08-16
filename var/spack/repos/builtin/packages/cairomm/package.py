# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cairomm(AutotoolsPackage):
    """Cairomm is a C++ wrapper for the cairo graphics library."""

    homepage = "https://www.cairographics.org/cairomm/"
    url      = "https://cairographics.org/releases/cairomm-1.8.4.tar.gz"

    version('1.12.2', sha256='45c47fd4d0aa77464a75cdca011143fea3ef795c4753f6e860057da5fb8bd599')
    version('1.8.4', sha256='a28ec6d9af8f93d09076f32cd77de35f9d74a517def5dea12cb8cc2ce3a6c8f1')
    version('1.6.4', sha256='3cb2c898d0ceb94ad2deb722b50a3a6ee46abdda741ecd6e5a40517c85ecea4c')
    version('1.6.2', sha256='068edc1743d92ff1d102141ba7597ba02a47379f9cb97799b0c3310848b56eff')

    depends_on('cairo')
    depends_on('libsigcpp@2.0:2.9.3', when='@:1.12.2')
