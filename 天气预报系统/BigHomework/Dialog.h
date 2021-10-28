#ifndef DIALOG_H
#define DIALOG_H

#include <QMainWindow>

namespace Ui {
class Dialog;
}

class Dialog : public QMainWindow
{
    Q_OBJECT

public:
    explicit Dialog(QWidget *parent = nullptr);
    ~Dialog();

private slots:
    void on_comboBox2_currentIndexChanged(const QString &arg1);

private:
    Ui::Dialog *ui;
};

#endif // DIALOG_H
