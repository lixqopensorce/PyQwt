"""pyqt_distutils.command.run_moc

Implements the PyQtDistutils 'run_moc' command.
"""
#
# Copyright (C) 2003-2004 Gerard Vermeulen
#
# This file is part of PyQwt
#
# PyQwt is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PyQwt is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PyQwt; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In addition, as a special exception, Gerard Vermeulen gives permission to
# link PyQwt dynamically with commercial, non-commercial or educational
# versions of Qt, PyQt and sip, and distribute PyQwt in this form, provided
# that equally powerful versions of Qt, PyQt and sip have been released under
# the terms of the GNU General Public License.
#
# If PyQwt is dynamically linked with commercial, non-commercial or educational
# versions of Qt, PyQt and sip, PyQwt becomes a free plug-in for a non-free
# program.


from os.path import basename, join, splitext
from distutils.core import Command
from pyqt_distutils.configure import get_config

class run_moc(Command):

    description = "Run moc (Qt's Meta Object Compiler)."

    user_options = [
        ('build-temp', 't',
         "directory to put temporary build by-products"),
        ('force', 'f',
         "forcibly build everything (ignore file timestamps)"),
        ('moc-program=', 'm',
         "specify moc (Meta Object Compiler)"),
        ]

    def initialize_options(self):
        self.extensions = None
        self.build_temp = None
        self.force = None
        self.moc_program = None

    # initialize_options()

    def finalize_options(self):
        self.set_undefined_options('build',
                                   ('build_temp', 'build_temp'),
                                   ('force', 'force'))
        self.extensions = self.distribution.ext_modules
        if not self.moc_program:
            self.moc_program = get_config('qt').get('make').get('MOC')
        # FIXME
        assert self.moc_program

    # finalize_options()

    def run_moc(self, source, target):
        """Run moc.
        """
        self.spawn([self.moc_program, source, '-o', target])

    # run_moc()

    def run(self):
        if not self.distribution.has_moc_sources():
	    return
        for ext in self.extensions:
            if ext.moc_sources:
                moc_temp = join(self.build_temp, 'moc', ext.path)
                self.mkpath(moc_temp)
                for source in ext.moc_sources:
                    root, _ = splitext(basename(source))
                    target = join(moc_temp, 'moc_%s.cpp' % root)
                    if target not in ext.sources:
                        ext.sources.append(target)
                    self.make_file(
                        [source], target, self.run_moc, (source, target))

    # run()

# class run_moc

# Local Variables: ***
# mode: python ***
# End: ***
