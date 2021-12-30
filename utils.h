#ifndef UTILS_H
#define UTILS_H
#include <QtWidgets>

class Utils
{
public:
    Utils();
    static void warn(QWidget *parent,QString title,QString text);
};

#endif // UTILS_H
