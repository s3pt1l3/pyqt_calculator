from rpn import reverse_polish_notation


def push_number(ui, button):
    if ui.cleared:
        ui.lineEdit.setText('0')
        if button.text() != "=" and button.text() != "C" and button.text() != "←" and button.text() != '+' \
                and button.text() != '-' and button.text() != '(' and button.text() != ')' and button.text() != '×'\
                and button.text() != '÷' and button.text() != '.':
            if button.text() == '-':
                ui.li = ''
                ui.cleared = False
                ui.li += button.text()
                ui.lineEdit.setText(ui.li)
            elif button.text() in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                ui.li = ''
                ui.cleared = False
                ui.li += button.text()
                ui.lineEdit.setText(ui.li)
                for i in ui.li:
                    print(i)
            else:
                ui.li += button.text()
                for i in ui.li:
                    print(i)

    else:
        if button.text() != "=" and button.text() != "C" and button.text() != "←":
            ui.li += button.text()
            ui.lineEdit.setText(ui.li)
            print(ui.li)
        elif button.text() == 'C':
            ui.li += ''
            ui.lineEdit.clear()
            ui.lineEdit.setText('0')
            ui.cleared = True

        elif button.text() == '←':
            ui.li = ui.li[0:-1]
            ui.lineEdit.setText(ui.li)
            if ui.li == '':
                ui.lineEdit.setText('0')
        elif button.text() == '=':
            result = reverse_polish_notation(ui.li)
            ui.lineEdit.setText(str(result))
            ui.cleared = True
