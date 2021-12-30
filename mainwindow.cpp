#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFile>
#include <QDebug>
#include <QListView>
#include <QRegularExpression>
#include <QtWidgets>
#include <QStringListModel>
#include "utils.h"
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    hosts = new QStringListModel(this);
    ui->listItems->setModel(hosts);

    reload();

}

MainWindow::~MainWindow()
{
    delete ui;
}

QList<QString> MainWindow::readfile(QString filename){
    QFile file(filename);
    if(!file.exists()){
        qDebug() << "NO existe el archivo "<<filename;
    }else{
        qDebug() << filename<<" encontrado...";
    }
    QString line;
    QList<QString> mySites;
    QRegularExpression re("#MLS");

    if (file.open(QIODevice::ReadOnly | QIODevice::Text)){
        QTextStream stream(&file);
        while (!stream.atEnd()){
            line = stream.readLine();
            if(re.match(line).hasMatch()){
               mySites.append(line);
            }
        }
    }
    file.close();
    return mySites;

}

/**
 * @brief MainWindow::reload
 * Reload data from config files
 */
void MainWindow::reload(){
    hosts->setStringList(readfile("/etc/hosts"));
}



void MainWindow::on_btn_reload_clicked()
{
    reload();
}


void MainWindow::on_btn_create_clicked()
{
    QFile f("/etc/hosts");
    if (f.open(QIODevice::WriteOnly | QIODevice::Append)) {
      QTextStream out{&f};
      out << Qt::endl << "Xubuntu #MLS" << Qt::endl;
       qDebug() <<" writing...";
    }else {
        Utils::warn(this,tr("Permision denied!"),tr("Could not open file"));
         qDebug()<< "no write ...";
      }
}


