/********************************************************************************
** Form generated from reading UI file 'design.ui'
**
** Created by: Qt User Interface Compiler version 5.12.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef TEST_H
#define TEST_H

#include <QtCore/QVariant>
#include <QtWebEngineWidgets/QWebEngineView>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_I23Cams
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout_3;
    QTabWidget *tabWidget;
    QWidget *maincams;
    QGridLayout *gridLayout_4;
    QVBoxLayout *verticalLayout;
    QWebEngineView *webEngineView;
    QWebEngineView *webEngineView_2;
    QWidget *extracams;
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout;
    QWebEngineView *webEngineView_4;
    QWebEngineView *webEngineView_6;
    QWebEngineView *webEngineView_5;
    QWebEngineView *webEngineView_3;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *I23Cams)
    {
        if (I23Cams->objectName().isEmpty())
            I23Cams->setObjectName(QString::fromUtf8("I23Cams"));
        I23Cams->resize(1151, 1156);
        I23Cams->setTabShape(QTabWidget::Rounded);
        centralwidget = new QWidget(I23Cams);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout_3 = new QGridLayout(centralwidget);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setSizeIncrement(QSize(1, 1));
        tabWidget->setTabPosition(QTabWidget::West);
        tabWidget->setTabShape(QTabWidget::Triangular);
        tabWidget->setElideMode(Qt::ElideNone);
        tabWidget->setTabBarAutoHide(false);
        maincams = new QWidget();
        maincams->setObjectName(QString::fromUtf8("maincams"));
        gridLayout_4 = new QGridLayout(maincams);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        webEngineView = new QWebEngineView(maincams);
        webEngineView->setObjectName(QString::fromUtf8("webEngineView"));
        webEngineView->setUrl(QUrl(QString::fromUtf8("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM6.mjpg.mjpg")));

        verticalLayout->addWidget(webEngineView);

        webEngineView_2 = new QWebEngineView(maincams);
        webEngineView_2->setObjectName(QString::fromUtf8("webEngineView_2"));
        webEngineView_2->setUrl(QUrl(QString::fromUtf8("http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM10.mjpg.mjpg")));

        verticalLayout->addWidget(webEngineView_2);


        gridLayout_4->addLayout(verticalLayout, 0, 0, 1, 1);

        tabWidget->addTab(maincams, QString());
        extracams = new QWidget();
        extracams->setObjectName(QString::fromUtf8("extracams"));
        gridLayout_2 = new QGridLayout(extracams);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        webEngineView_4 = new QWebEngineView(extracams);
        webEngineView_4->setObjectName(QString::fromUtf8("webEngineView_4"));
        webEngineView_4->setUrl(QUrl(QString::fromUtf8("http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM9.mjpg.mjpg")));

        gridLayout->addWidget(webEngineView_4, 1, 1, 1, 1);

        webEngineView_6 = new QWebEngineView(extracams);
        webEngineView_6->setObjectName(QString::fromUtf8("webEngineView_6"));
        webEngineView_6->setUrl(QUrl(QString::fromUtf8("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM7.mjpg.mjpg")));

        gridLayout->addWidget(webEngineView_6, 1, 0, 1, 1);

        webEngineView_5 = new QWebEngineView(extracams);
        webEngineView_5->setObjectName(QString::fromUtf8("webEngineView_5"));
        webEngineView_5->setUrl(QUrl(QString::fromUtf8("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM3.mjpg.mjpg")));

        gridLayout->addWidget(webEngineView_5, 0, 0, 1, 1);

        webEngineView_3 = new QWebEngineView(extracams);
        webEngineView_3->setObjectName(QString::fromUtf8("webEngineView_3"));
        webEngineView_3->setUrl(QUrl(QString::fromUtf8("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM5.mjpg.mjpg")));

        gridLayout->addWidget(webEngineView_3, 0, 1, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);

        tabWidget->addTab(extracams, QString());

        gridLayout_3->addWidget(tabWidget, 0, 0, 1, 1);

        I23Cams->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(I23Cams);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        statusbar->setAutoFillBackground(false);
        I23Cams->setStatusBar(statusbar);

        retranslateUi(I23Cams);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(I23Cams);
    } // setupUi

    void retranslateUi(QMainWindow *I23Cams)
    {
        I23Cams->setWindowTitle(QApplication::translate("I23Cams", "I23 Cam Viewer", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(maincams), QApplication::translate("I23Cams", "Main Cams", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(extracams), QApplication::translate("I23Cams", "Extra Cams", nullptr));
    } // retranslateUi

};

namespace Ui {
    class I23Cams: public Ui_I23Cams {};
} // namespace Ui

QT_END_NAMESPACE

#endif // TEST_H
