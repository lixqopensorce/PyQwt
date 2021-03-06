// The SIP interface definition for
//      QwtEventPattern,
//      MousePattern,
//      KeyPattern.
//
// Copyright (C) 2001-2004 Gerard Vermeulen
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
// educational versions of Qt, PyQt and sip, PyQwt becomes a free plug-in
// for a non-free program.
//
// -- LICENSE --


class QwtEventPattern
{
%TypeHeaderCode
#include <qevent.h>
#include <qwt_event_pattern.h>
%End

public:
    enum MousePatternCode {
        MouseSelect1,
        MouseSelect2,
        MouseSelect3,
        MouseSelect4,
        MouseSelect5,
        MouseSelect6,
        MousePatternCount,
    };

    enum KeyPatternCode {
        KeySelect1,
        KeySelect2,
        KeyAbort,
        KeyLeft,
        KeyRight,
        KeyUp,
        KeyDown,
        KeyRedo,
        KeyUndo,
        KeyHome,
        KeyPatternCount,
    };

    class MousePattern
    {
    public:
        MousePattern(int = Qt::NoButton, int = Qt::NoButton);
    };

    class KeyPattern
    {
    public:
        KeyPattern(int = 0, int = Qt::NoButton);
    };

public: // recalled, because sip seems to have lost its memory
    QwtEventPattern();
    virtual ~QwtEventPattern();

    void initMousePattern(int);
    void initKeyPattern();

    void setMousePattern(uint, int, int = Qt::NoButton);
    void setKeyPattern(uint, int, int = Qt::NoButton);

    void setMousePattern(const QwtArray<QwtEventPattern::MousePattern> &);
    void setKeyPattern(const QwtArray<QwtEventPattern::KeyPattern> &);

    // dead code: const QwtArray<MousePattern> &mousePattern() const;
    // dead code: const QwtArray<KeyPattern> &keyPattern() const;

    QwtArray<QwtEventPattern::MousePattern> &mousePattern();
    QwtArray<QwtEventPattern::KeyPattern> &keyPattern();

    bool mouseMatch(uint, const QMouseEvent *) const;
    bool keyMatch(uint, const QKeyEvent *) const;

protected:
    virtual bool mouseMatch(const MousePattern &, const QMouseEvent *) const;
    virtual bool keyMatch(const KeyPattern &, const QKeyEvent *) const;
};


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// End:
