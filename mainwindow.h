#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QStringListModel>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:

    void on_btn_reload_clicked();

    void on_btn_create_clicked();

private:
    Ui::MainWindow *ui;
    QStringListModel *hosts;
    QList<QString> readfile(QString filename);
    void reload();
};
#endif // MAINWINDOW_H
