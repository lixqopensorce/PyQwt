patches = [('.array', '--- qwt-sources/include/qwt_autoscl.h.array\tTue Jun 17 19:42:24 2003\n+++ qwt-sources/include/qwt_autoscl.h\tTue Jun 17 19:42:24 2003\n@@ -111,6 +111,7 @@\n     const QwtScaleDiv &scaleDiv() const;\n \n     void adjust(double *arr, int n, int reset = 0);\n+    void adjust(const QwtArray<double> &x, int reset = 0);\n     void adjust(double x1, double x2, int reset = 0);\n \n     void build();\n--- qwt-sources/include/qwt_spline.h.array\tTue Jun 17 19:42:24 2003\n+++ qwt-sources/include/qwt_spline.h\tTue Jun 17 19:42:24 2003\n@@ -10,6 +10,7 @@\n #ifndef QWT_SPLINE_H\n #define QWT_SPLINE_H\n \n+#include "qwt_array.h"\n #include "qwt_global.h"\n \n /*!\n@@ -67,6 +68,8 @@\n \n     double value(double x) const;\n     int recalc(double *x, double *y, int n, int periodic = 0);\n+    int recalc(const QwtArray<double> &x, const QwtArray<double> &y,\n+        int periodic = 0);\n     void copyValues(int tf = 1);\n \n private:\n--- qwt-sources/src/qwt_autoscl.cpp.array\tTue Jun 17 19:42:24 2003\n+++ qwt-sources/src/qwt_autoscl.cpp\tTue Jun 17 19:42:24 2003\n@@ -115,6 +115,11 @@\n         build();\n }\n \n+void QwtAutoScale::adjust(const QwtArray<double> &x, int reset)\n+{\n+    adjust(x.data(), x.size(), reset);\n+}\n+\n \n /*!\n   \\brief Adjust the scale to include a specified interval\n--- qwt-sources/src/qwt_spline.cpp.array\tTue Jun 17 19:42:24 2003\n+++ qwt-sources/src/qwt_spline.cpp\tTue Jun 17 19:42:24 2003\n@@ -182,6 +182,15 @@\n     return rv;\n }\n \n+int QwtSpline::recalc(const QwtArray<double> &x, const QwtArray<double> &y,\n+    int periodic)\n+{\n+    int n = QMIN(x.size(), y.size());\n+    d_buffered = TRUE;\n+\n+    return recalc(x.data(), y.data(), n, periodic);\n+}\n+\n /*!\n   \\brief Determines the coefficients for a natural spline\n   \\return <dl>\n'), ('.canvas', '--- qwt-sources/include/qwt_plot_canvas.h.canvas\tTue Jun 17 19:42:24 2003\n+++ qwt-sources/include/qwt_plot_canvas.h\tTue Jun 17 19:42:24 2003\n@@ -7,6 +7,8 @@\n  * modify it under the terms of the Qwt License, Version 1.0\n  *****************************************************************************/\n \n+// vim: expandtab\n+\n #ifndef QWT_PLOT_CANVAS_H\n #define QWT_PLOT_CANVAS_H\n \n@@ -21,10 +23,9 @@\n   \\sa  QwtPlot \n */\n \n-class QWT_EXPORT QwtPlotCanvas : public QFrame\n+class QWT_EXPORT QwtCanvas : public QFrame\n {\n     Q_OBJECT\n-    friend class QwtPlot;\n public:\n     void enableOutline(bool tf);\n     bool outlineEnabled() const;\n@@ -58,17 +59,20 @@\n     void mouseMoved(const QMouseEvent &e);\n \n protected:\n-    QwtPlotCanvas(QwtPlot *);\n+    QwtCanvas(QWidget *);\n \n-    virtual void frameChanged();\n     virtual void drawContents(QPainter *);\n+    /*!\n+      Encapsulates the QwtCanvas::parent() specific code for drawContents().\n+     */\n+    virtual void drawContentsCallback(QPainter *) = 0;\n \n     virtual void mousePressEvent(QMouseEvent *e);\n     virtual void mouseReleaseEvent(QMouseEvent *e);\n     virtual void mouseMoveEvent(QMouseEvent *e);\n+    virtual void drawOutline(QPainter &p, const QColor &bg = Qt::white);\n \n private:    \n-    void drawOutline(QPainter &p);\n \n     bool d_outlineEnabled;\n     bool d_outlineActive;\n@@ -78,6 +82,20 @@\n     QPen d_pen;\n     QPoint d_entryPoint;\n     QPoint d_lastPoint;\n+};\n+\n+class QWT_EXPORT QwtPlotCanvas : public QwtCanvas\n+{\n+    Q_OBJECT\n+    friend class QwtPlot;\n+\n+protected:\n+    QwtPlotCanvas(QwtPlot *parent);\n+\n+    virtual void frameChanged();\n+    virtual void drawContentsCallback(QPainter *);\n+    virtual void drawOutline(QPainter &p, const QColor &bg = Qt::white);\n+\n };\n \n #endif\n--- qwt-sources/src/qwt_plot_canvas.cpp.canvas\tTue Jun 17 19:42:24 2003\n+++ qwt-sources/src/qwt_plot_canvas.cpp\tTue Jun 17 19:42:24 2003\n@@ -7,6 +7,8 @@\n  * modify it under the terms of the Qwt License, Version 1.0\n  *****************************************************************************/\n \n+// vim: expandtab\n+\n #include <qpainter.h>\n #include <qstyle.h>\n #include "qwt_painter.h"\n@@ -18,8 +20,8 @@\n \n //! Sets a cross cursor, and an invisible red outline\n \n-QwtPlotCanvas::QwtPlotCanvas(QwtPlot *plot):\n-    QFrame(plot, "canvas", WRepaintNoErase|WResizeNoErase),\n+QwtCanvas::QwtCanvas(QWidget *parent):\n+    QFrame(parent, "canvas", WRepaintNoErase|WResizeNoErase),\n     d_outlineEnabled(FALSE),\n     d_outlineActive(FALSE),\n     d_mousePressed(FALSE),\n@@ -29,19 +31,8 @@\n     setCursor(crossCursor);\n }\n \n-//! Requires layout updates of the parent plot\n-void QwtPlotCanvas::frameChanged()\n-{\n-    QFrame::frameChanged();\n-\n-    // frame changes change the size of the contents rect, what\n-    // is related to the axes. So we have to update the layout.\n-\n-    ((QwtPlot *)parent())->updateLayout();\n-}\n-\n //! Redraw the canvas\n-void QwtPlotCanvas::drawContents(QPainter *painter)\n+void QwtCanvas::drawContents(QPainter *painter)\n {\n     QwtPaintBuffer paintBuffer(this, \n         painter->clipRegion().boundingRect(), painter);\n@@ -49,7 +40,7 @@\n     QPainter *bufferedPainter = paintBuffer.painter();\n \n     bufferedPainter->save();\n-    ((QwtPlot *)parent())->drawCanvas(bufferedPainter);\n+    drawContentsCallback(bufferedPainter);\n     bufferedPainter->restore();\n \n     if ( d_outlineActive )\n@@ -70,7 +61,7 @@\n }\n \n //! mousePressEvent\n-void QwtPlotCanvas::mousePressEvent(QMouseEvent *e)\n+void QwtCanvas::mousePressEvent(QMouseEvent *e)\n {\n \n     if (d_outlineActive)\n@@ -103,7 +94,7 @@\n }\n \n //! mouseReleaseEvent\n-void QwtPlotCanvas::mouseReleaseEvent(QMouseEvent *e)\n+void QwtCanvas::mouseReleaseEvent(QMouseEvent *e)\n {\n     if (d_outlineActive)\n     {\n@@ -121,7 +112,7 @@\n }\n \n //! mouseMoveEvent\n-void QwtPlotCanvas::mouseMoveEvent(QMouseEvent *e)\n+void QwtCanvas::mouseMoveEvent(QMouseEvent *e)\n {\n     if (d_outlineActive)\n     {\n@@ -145,10 +136,10 @@\n   mark a selected region, etc.\n   \\param tf \\c TRUE (enabled) or \\c FALSE (disabled)\n   \\warning An outline style has to be specified.\n-  \\sa QwtPlotCanvas::setOutlineStyle()\n+  \\sa QwtCanvas::setOutlineStyle()\n */\n \n-void QwtPlotCanvas::enableOutline(bool tf)\n+void QwtCanvas::enableOutline(bool tf)\n {\n \n     //\n@@ -166,10 +157,10 @@\n \n /*!\n   \\return \\c TRUE if the outline feature is enabled\n-  \\sa QwtPlotCanvas::enableOutline\n+  \\sa QwtCanvas::enableOutline\n */\n \n-bool QwtPlotCanvas::outlineEnabled() const \n+bool QwtCanvas::outlineEnabled() const \n { \n     return d_outlineEnabled; \n }\n@@ -202,10 +193,10 @@\n   <dd>Similar to Qwt::Rect, but with an ellipse inside\n       a bounding rectangle.\n   </dl>\n-  \\sa QwtPlotCanvas::enableOutline(), QwtPlotCanvas::outlineStyle()\n+  \\sa QwtCanvas::enableOutline(), QwtCanvas::outlineStyle()\n */\n \n-void QwtPlotCanvas::setOutlineStyle(Qwt::Shape os)\n+void QwtCanvas::setOutlineStyle(Qwt::Shape os)\n {\n     if (d_outlineActive)\n     {\n@@ -224,9 +215,9 @@\n \n /*!\n   \\return the outline style\n-  \\sa QwtPlotCanvas::setOutlineStyle()\n+  \\sa QwtCanvas::setOutlineStyle()\n */\n-Qwt::Shape QwtPlotCanvas::outlineStyle() const \n+Qwt::Shape QwtCanvas::outlineStyle() const \n { \n     return d_outline; \n }\n@@ -234,20 +225,20 @@\n /*!\n   \\brief Specify a pen for the outline\n   \\param pen new pen\n-  \\sa QwtPlotCanvas::outlinePen\n+  \\sa QwtCanvas::outlinePen\n */\n \n-void QwtPlotCanvas::setOutlinePen(const QPen &pen)\n+void QwtCanvas::setOutlinePen(const QPen &pen)\n {\n     d_pen = pen;\n }\n \n /*!\n   \\return the pen used to draw outlines\n-  \\sa QwtPlotCanvas::setOutlinePen\n+  \\sa QwtCanvas::setOutlinePen\n */\n \n-const QPen& QwtPlotCanvas::outlinePen() const \n+const QPen& QwtCanvas::outlinePen() const \n { \n     return d_pen; \n }\n@@ -255,12 +246,10 @@\n /*!\n     draw an outline\n */\n-void QwtPlotCanvas::drawOutline(QPainter &p)\n+void QwtCanvas::drawOutline(QPainter &p, const QColor &bg)\n {\n     const QRect &r = contentsRect();\n \n-    QColor bg = ((QwtPlot *)parent())->canvasBackground();\n-\n     QPen pn = d_pen;\n     pn.setColor(QColor(0, (bg.pixel() ^ d_pen.color().pixel())));\n \n@@ -303,4 +292,32 @@\n         default:\n             break;\n     }\n+}\n+\n+QwtPlotCanvas::QwtPlotCanvas(QwtPlot *parent): QwtCanvas(parent) {}\n+ \n+//! Requires layout updates of the parent plot\n+void QwtPlotCanvas::frameChanged()\n+{\n+    QFrame::frameChanged();\n+\n+    // frame changes change the size of the contents rect, what\n+    // is related to the axes. So we have to update the layout.\n+\n+    ((QwtPlot *)parent())->updateLayout();\n+}\n+\n+void QwtPlotCanvas::drawContentsCallback(QPainter *painter)\n+{\n+    ((QwtPlot *)parent())->drawCanvas(painter);\n+}\n+\n+/*!\n+    draw an outline\n+*/\n+void QwtPlotCanvas::drawOutline(QPainter &p, const QColor &)\n+{\n+    QColor bg = ((QwtPlot *)parent())->canvasBackground();\n+\n+    QwtCanvas::drawOutline(p, bg);\n }\n'), ('.version', '--- qwt-sources/include/qwt_global.h.version\tTue Jun 17 19:42:24 2003\n+++ qwt-sources/include/qwt_global.h\tTue Jun 17 19:42:24 2003\n@@ -7,13 +7,15 @@\n  * modify it under the terms of the Qwt License, Version 1.0\n  *****************************************************************************/\n \n+// vim: expandtab\n+\n #ifndef QWT_GLOBAL_H\n #define QWT_GLOBAL_H\n \n #include <qmodules.h>\n #include <qglobal.h>\n \n-#define QWT_VERSION       042\n+#define QWT_VERSION       0x000402\n #define QWT_VERSION_STR   "0.4.2"\n \n //\n')]
