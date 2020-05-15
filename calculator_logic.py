def push_number(ui, button):
    if ui.cleared:
        if button.text() != "=" and button.text() != "C" and button.text() != "←":
            if button.text() in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                ui.li.clear()
                ui.cleared = False
                ui.li.append(button.text())
                ui.lineEdit.setText(ui.li[0])
                for i in ui.li:
                    print(i)
            else:

                ui.li.append(button.text())
                for i in ui.li:
                    print(i)

    else:
        if button.text() != "=" and button.text() != "C" and button.text() != "←":
            ui.li[0] += button.text()
            ui.lineEdit.setText(ui.li[0])
            print(ui.li)
