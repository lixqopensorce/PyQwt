// The SIP interface definition for the Qwt module of PyQwt.
//
// Copyright (C) 2001-2005 Gerard Vermeulen
// Copyright (C) 2000 Mark Colclough
//
// This file is part of PyQwt.
//
// -- LICENSE --
//
// PyQwt is free software; you can redistribute it and/or modify it under the
// terms of the GNU General Public License as published by the Free Software
// Foundation; either version 2 of the License, or (at your option) any later
// version.
//
// PyQwt is distributed in the hope that it will be useful, but WITHOUT ANY
// WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
// FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
// details.
//
// You should have received a copy of the GNU General Public License along with
// PyQwt; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
// Suite 330, Boston, MA 02111-1307, USA.
//
// In addition, as a special exception, Gerard Vermeulen gives permission to
// link PyQwt dynamically with commercial, non-commercial or educational
// versions of Qt, PyQt and sip, and distribute PyQwt in this form, provided
// that equally powerful versions of Qt, PyQt and sip have been released under
// the terms of the GNU General Public License.
//
// If PyQwt is dynamically linked with commercial, non-commercial or
// educational versions of Qt, PyQt and sip, PyQwt becomes a free plug-in for
// a non-free program.
//
// -- LICENSE --


%Module _qwt 0

%Include features.sip
%Include timelines.sip
%Include types.sip

%Import qt/qtmod.sip

%ModuleHeaderCode
#include <qwt_python.h>
%End

%PostInitialisationCode
#ifdef HAS_NUMARRAY
    qwt_import_libnumarray();
#endif
#ifdef HAS_NUMERIC
    qwt_import_array();
#endif
%End

// Automagically generated files
%Include QwtArrayDouble.sip
%Include QwtArrayLong.sip
%If (QWT_4_2_0 - QWT_4_3_0)
%Include QwtArrayQwtDiMap.sip
%End // (QWT_4_2_0 - QWT_4_3_0)
%Include QwtArrayQwtDoublePoint.sip
%Include QwtArrayQwtKeyPattern.sip
%Include QwtArrayQwtMousePattern.sip
%If (QWT_4_3_0 -)
%Include QwtArrayQwtScaleMap.sip
%End // (QWT_4_3_0 -)

// Provide "static PyObject *sipSubClass___QwtObject__(const QObject *sipCpp)".
%Include qwtobject.sip

// Normal include files
%Include qwt.sip
%Include qwtanalogclock.sip
%Include qwtarray.sip
%Include qwtarrowbutton.sip
%Include qwtautoscale.sip
%Include qwtcompass.sip
%Include qwtcompassrose.sip
%Include qwtcounter.sip
%Include qwtcurve.sip
%Include qwtcurvedict.sip
// FIXME: subclassing from QwtData in Python is dangerous
// %Include qwtdata.sip
%Include qwtdblrange.sip
%Include qwtdoubleinterval.sip
%Include qwtdial.sip
%Include qwtdialneedle.sip
%Include qwtdimap.sip
%Include qwtdoublerect.sip
%Include qwtdyngridlayout.sip
%Include qwteventpattern.sip
%Include qwtglobal.sip
%Include qwtgrid.sip
%Include qwtknob.sip
%Include qwtlayoutmetrics.sip
%Include qwtlegend.sip
%Include qwtlegendbutton.sip
%Include qwtlegenditem.sip
%Include qwtlegendlabel.sip
%Include qwtmarker.sip
%Include qwtmarkerdict.sip
%Include qwtmath.sip
%Include qwtpicker.sip
%Include qwtpickermachine.sip
%Include qwtplot.sip
%Include qwtplotcanvas.sip
%Include qwtplotcurve.sip
%Include qwtplotgrid.sip
%Include qwtplotitem.sip
%Include qwtplotlayout.sip
%Include qwtplotmarker.sip
%Include qwtplotpicker.sip
%Include qwtplotzoomer.sip
%Include qwtpaintbuffer.sip
%Include qwtpainter.sip
%Include qwtplotprintfilter.sip
%Include qwtpushbutton.sip
%Include qwtrect.sip
%Include qwtscale.sip
%Include qwtscalediv.sip
%Include qwtscaledraw.sip
%Include qwtscaleif.sip
%Include qwtsliderbase.sip
%Include qwtslider.sip
%Include qwtspline.sip
%Include qwtsymbol.sip
%Include qwttext.sip
%Include qwtthermo.sip
%Include qwtvaluelist.sip
%Include qwtvaluestack.sip
%Include qwtwheel.sip

// Image support
%Include qwtqimage.sip

// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// End:
