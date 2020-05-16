from rpn import reverse_polish_notation


def push_number(ui, button):
    if ui.cleared:
        ui.lineEdit.setText('0')
        if button.text() not in '=C←().':
            if button.text() == '-':
                ui.li = '0'
                ui.cleared = False
                ui.li += button.text()
                ui.li_output = ui.li[1:]
                ui.lineEdit.setText(ui.li_output)
                ui.minus = True
            elif button.text() in "1234567890":
                ui.li = ''
                ui.li_output = ''
                ui.cleared = False
                ui.li += button.text()
                ui.li_output += button.text()
                ui.lineEdit.setText(ui.li_output)
            else:
                ui.li += button.text()
                ui.li_output += button.text()

    else:
        if button.text() != "=" and button.text() != "C" and button.text() != "←" and button.text() != "-":
            ui.li += button.text()
            if ui.minus:
                ui.li_output = ui.li[1:]
                ui.lineEdit.setText(ui.li_output)
            else:
                ui.li_output += button.text()
                ui.lineEdit.setText(ui.li_output)
        elif button.text() == 'C':
            ui.li += ''
            ui.lineEdit.clear()
            ui.lineEdit.setText('0')
            ui.cleared = True
            ui.minus = False

        elif button.text() == '←':
            ui.li = ui.li[0:-1]
            ui.li_output = ui.li_output[0:-1]
            ui.lineEdit.setText(ui.li_output)
            if ui.li == '':
                ui.lineEdit.setText('0')
                ui.minus = False
        elif button.text() == '-':
            if ui.li[-1] == '(':
                ui.li += '0-'
                ui.li_output += '-'
                ui.lineEdit.setText(ui.li_output)
            else:
                ui.li += '0-'
                ui.li_output += '-'
                ui.lineEdit.setText(ui.li_output)

        elif button.text() == '=':
            if ui.li[-1] in '+-:×÷':
                pass
            elif len(ui.li) == 2 and ui.li[-1] in '()':
                pass
            else:
                result = reverse_polish_notation(ui.li)
                ui.lineEdit.setText(str(result))
                ui.cleared = True
