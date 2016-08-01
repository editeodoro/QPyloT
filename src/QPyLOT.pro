#-------------------------------------------------
#
# Project created by QtCreator 2015-10-29T11:22:42
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = QPyLOT
TEMPLATE = app


SOURCES += main.cpp\
        qpylotwindow.cpp

HEADERS  += qpylotwindow.h

FORMS    += UIs/plot1d_window.ui\
            UIs/start_window.ui\
            UIs/plot1d_tabw.ui\
            UIs/plot1d.ui \
            UIs/axes_tabw.ui

DISTFILES += \
    main.py

