def push_number(ui, button):
    if ui.cleared:
        ui.lineEdit.setText('0')
        ui.li = '0'
        if button.text() not in '=C←)':
            if button.text() in "1234567890-(":
                ui.li = ''
                ui.cleared = False
                ui.li += button.text()
                ui.lineEdit.setText(ui.li)
            else:
                ui.li += button.text()
                ui.cleared = False
                ui.lineEdit.setText(ui.li)
    else:
        if button.text() != "=" and button.text() != "C" and button.text() != "←" and button.text() != ".":
            if button.text() not in '1234567890-' and ui.li[-1] == '(':
                pass
            elif button.text() in '+×÷-':
                if ui.li[-1] not in '+-×÷.':
                    ui.li += button.text()
                    ui.lineEdit.setText(ui.li)
            elif button.text() in '()' and ui.li[-1] == '.':
                pass
            elif button.text() == '(' and ui.li[-1] not in '+-×÷':
                pass
            else:
                if ui.li[0] == '0' and ui.li[-1] in '+×÷-':
                    ui.li += button.text()
                    ui.li = ui.li.replace('×', '*')
                    ui.li = ui.li.replace('÷', '/')
                    try:
                        ui.li = str(eval(ui.li))
                        ui.lineEdit.setText(ui.li)
                    except ZeroDivisionError:
                        ui.lineEdit.setText('Error: division by zero')
                        ui.li = '0'
                        ui.cleared = True
                else:
                    ui.li += button.text()
                    ui.lineEdit.setText(ui.li)
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
                ui.cleared = True
        elif button.text() == '.':
            if ui.li[-1] not in '+-×÷().':
                ui.li += button.text()
                ui.lineEdit.setText(ui.li)
        elif button.text() == '=':
            if ui.li[-1] in '+-×÷':
                pass
            elif len(ui.li) == 2 and ui.li[-1] in '()':
                pass
            else:
                if '.' in ui.li:
                    ui.li2 = ui.li
                    ui.li = ui.li.replace('+', ' ')
                    ui.li = ui.li.replace('-', ' ')
                    ui.li = ui.li.replace('×', ' ')
                    ui.li = ui.li.replace('÷', ' ')
                    for i in ui.li.split():
                        if i.count('.') > 1:
                            ui.li = 'Error: too much dots in one number'
                            ui.lineEdit.setText(ui.li)
                            ui.cleared = True
                            ui.dots = True
                            break
                    if not ui.dots:
                        ui.li = ui.li2
                        try:
                            ui.li = ui.li.replace('×', '*')
                            ui.li = ui.li.replace('÷', '/')
                            result = eval(ui.li)
                            ui.lineEdit.setText(str(result))
                            ui.li = str(result)
                        except ZeroDivisionError:
                            ui.lineEdit.setText('Error: division by zero')
                            ui.li = str(result)
                else:
                    try:
                        ui.li = ui.li.replace('×', '*')
                        ui.li = ui.li.replace('÷', '/')
                        result = eval(ui.li)
                        ui.lineEdit.setText(str(result))
                        ui.li = str(result)
                    except ZeroDivisionError:
                        ui.lineEdit.setText('Error: division by zero')
                        ui.li = '0'
                        ui.cleared = True
