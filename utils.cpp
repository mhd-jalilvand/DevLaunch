#include "utils.h"
#include <QMessageBox>

Utils::Utils()
{

}

 void Utils::warn(QWidget *parent,QString title,QString text){
    QMessageBox::warning(
        parent,
        title,
        text);
}
