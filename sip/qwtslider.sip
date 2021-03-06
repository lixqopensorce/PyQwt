// The SIP interface definition for QwtSlider.
//
// Copyright (C) 2001-2004 Gerard Vermeulen
// Copyright (C) 2000 Mark Colclough
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


class QwtSlider: QwtSliderBase, QwtScaleIf
{
%TypeHeaderCode
#include <qwt_slider.h>
%End

public:
    enum ScalePos {
	None,
	Left,
	Right,
	Top,
	Bottom,
    };
    enum BGSTYLE {
	BgTrough = 0x1,
	BgSlot = 0x2,
	BgBoth = 0x3,
    };  

    QwtSlider(QWidget * /TransferThis/, const char * = 0, 
	      Qt::Orientation = Qt::Horizontal, ScalePos = None,
	      BGSTYLE = BgTrough);
	
    virtual void setOrientation(Qt::Orientation);

    void setBgStyle(BGSTYLE);
    BGSTYLE bgStyle() const;

    void setScalePos(ScalePos);
    ScalePos scalePos() const;

    void setScalePosition(ScalePos);
    ScalePos scalePosition() const;

    int thumbLength() const;
    int thumbWidth() const;
    int borderWidth() const;

    void setThumbLength(int);
    void setThumbWidth(int);
    void setBorderWidth(int);
    void setMargins(int, int);

    virtual QSize sizeHint() const;
    virtual QSize minimumSizeHint() const;
    virtual QSizePolicy sizePolicy() const;
	
protected:
    virtual double getValue(const QPoint &);
    virtual void getScrollMode(const QPoint &, int & /Out/, int & /Out/);
    void draw(QPainter *, const QRect &);
    virtual void drawSlider(QPainter *, const QRect &);
    virtual void drawThumb(QPainter *, const QRect &, int);
    virtual void resizeEvent(QResizeEvent *);
    virtual void paintEvent(QPaintEvent *);
    virtual void valueChange();
    virtual void rangeChange();
    virtual void scaleChange();
    virtual void fontChange(const QFont &);
    void layoutSlider(bool = 1);
    int xyPosition(double) const;
};

// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// End:
