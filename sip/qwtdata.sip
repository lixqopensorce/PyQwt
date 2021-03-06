// The SIP interface definition for
//      QwtData,
//      QwtArrayData.
//
// Copyright (C) 2001-2004 Gerard Vermeulen
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
// educational versions of Qt, PyQt and sip, PyQwt becomes a free plug-in
// for a non-free program.
//
// -- LICENSE --


class QwtData
{
%TypeHeaderCode
#include <qwt_data.h>
%End

public:
    QwtData();
    virtual QwtData *copy() const = 0;
    virtual size_t size() const = 0;
    virtual double x(size_t) const = 0;
    virtual double y(size_t) const = 0;
    virtual QwtDoubleRect boundingRect() const;
};

class QwtDoublePointData: QwtData
{
%TypeHeaderCode
#include <qwt_data.h>
%End

public:
    QwtDoublePointData(const QwtArray<QwtDoublePoint> &);
    virtual QwtData *copy() const;
    virtual size_t size() const;
    virtual double x(size_t) const;
    virtual double y(size_t) const;
    virtual QwtDoubleRect boundingRect() const;
};


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// End:
