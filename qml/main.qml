import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material

Window {
    id: mainWindow
    width: 1000
    height: 580
    minimumWidth: 700
    minimumHeight: 500
    visible: true
    color: "#00000000"

    property int windowStatus: 0

    Rectangle {
        id: bg
        color: "#22272F"
        border.color: "#383e4c"
        border.width: 1
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        z: 1

        Rectangle {
            id: appContainer
            color: "#00000000"
            anchors.fill: parent
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0

            Rectangle {
                id: topBar
                height: 60
                color: "#1C2128"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0
                z: 2
            
                Item {
                    width: 800
                    height: parent.height

                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
    
                    Row {
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.verticalCenter: parent.verticalCenter
                        spacing: 10

                        Button {
                            id: jsonButton
                            width: 130
                            height: 50
                            anchors.verticalCenter: parent.verticalCenter 

                            text: "Участники"
                            onClicked: backend.openJsonFile()

                            property string buttonColor: "grey"
                            
                            background: Rectangle {
                                color: jsonButton.pressed ? "white" : (jsonButton.hovered ? "lightgray" :  jsonButton.buttonColor)
                                radius: 4
                            }
                        }

                        Button {
                            id: txtButton
                            width: 130
                            height: 50
                            anchors.verticalCenter: parent.verticalCenter

                            text: "Забеги"
                            onClicked: backend.openTxtFile()

                            property string buttonColor: "grey"

                            background: Rectangle {
                                color: txtButton.pressed ? "white" : (txtButton.hovered ? "lightgray" :  txtButton.buttonColor)
                                radius: 4
                            }
                        }

                        Button {
                            id: calculateButton
                            width: 130
                            height: 50
                            anchors.verticalCenter: parent.verticalCenter

                            text: "Расчитать"
                            onClicked: backend.calculateResult()

                            property string buttonColor: "grey"

                            background: Rectangle {
                                color: calculateButton.pressed ? "white" : (calculateButton.hovered ? "lightgray" :  calculateButton.buttonColor)
                                radius: 4
                            }
                        }

                        Button {
                            id: saveButton
                            width: 130
                            height: 50
                            anchors.verticalCenter: parent.verticalCenter

                            text: "Сохранить"
                            onClicked: backend.saveJsonFile()

                            property string buttonColor: "grey"

                            background: Rectangle {
                                color: saveButton.pressed ? "white" : (saveButton.hovered ? "lightgray" :  saveButton.buttonColor)
                                radius: 4
                            }
                        }

                        Button {
                            id: resetButton
                            width: 130
                            height: 50
                            anchors.verticalCenter: parent.verticalCenter

                            text: "Сбросить"
                            onClicked: backend.reset()

                            property string buttonColor: "grey"

                            background: Rectangle {
                                color: resetButton.pressed ? "white" : (resetButton.hovered ? "lightgray" :  resetButton.buttonColor)
                                radius: 4
                            }
                        }
                    }
                }
            }

            Rectangle {
                id: content
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: topBar.bottom
                anchors.bottom: parent.bottom
                z: 1

                Rectangle {
                    id: topMerg
                    color: bg.color
                    height: 20
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                }

                Rectangle {
                    id: bottomMerg
                    color: bg.color
                    height: 20
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    z: 4
                }


                Rectangle {
                    id: titleTable
                    visible: false
                    color: "#00000000"
                    width: 700
                    height: 40
                    anchors.bottomMargin: 0
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: topMerg.bottom
                    z: 4

                    Row {
                        anchors.fill: parent
                        height: 40

                        Rectangle {
                            width: 140
                            height: parent.height
                            color: "#2D333B"
                            border.color: "#454C56"
                            border.width: 1
                            Text {
                                anchors.centerIn: parent
                                text: "Занятое место"
                                color: "#ACBAC7"
                                font.bold: true
                            }
                        }
                        Rectangle {
                            width: 140
                            height: parent.height
                            color: "#2D333B"
                            border.color: "#454C56"
                            border.width: 1
                            Text {
                                anchors.centerIn: parent
                                text: "Нагрудный номер"
                                color: "#ACBAC7"
                                font.bold: true
                            }
                        }
                        Rectangle {
                            width: 140
                            height: parent.height
                            color: "#2D333B"
                            border.color: "#454C56"
                            border.width: 1
                            Text {
                                anchors.centerIn: parent
                                text: "Имя"
                                color: "#ACBAC7"
                                font.bold: true
                            }
                        }
                        Rectangle {
                            width: 140
                            height: parent.height
                            color: "#2D333B"
                            border.color: "#454C56"
                            border.width: 1
                            Text {
                                anchors.centerIn: parent
                                text: "Фамилия"
                                color: "#ACBAC7"
                                font.bold: true
                            }
                        }
                        Rectangle {
                            width: 140
                            height: parent.height
                            color: "#2D333B"
                            border.color: "#454C56"
                            border.width: 1
                            Text {
                                anchors.centerIn: parent
                                text: "Результат"
                                color: "#ACBAC7"
                                font.bold: true
                            }
                        }
                    }
                }

                Rectangle {
                    id: table
                    color: "#00000000"
                    width: 700
                    height: parent.height

                    anchors.bottomMargin: 0
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: titleTable.bottom
                    anchors.bottom: bottomMerg.top

                    ListView {
                        anchors.fill: parent
                        model: resultModel
                        width: 700
                        

                        delegate: Item {
                            width: parent ? parent.width : 700
                            height: 40
                            

                            Row {
                                anchors.fill: parent

                                Rectangle {
                                    width: 140
                                    height: parent.height
                                    color: "#2D333B"
                                    border.color: "#454C56"
                                    border.width: 1
                                    Text {
                                        anchors.centerIn: parent
                                        text: model.place
                                        color: "#ACBAC7"
                                    }
                                }
                                Rectangle {
                                    width: 140
                                    height: parent.height
                                    color: "#2D333B"
                                    border.color: "#454C56"
                                    border.width: 1
                                    Text {
                                        anchors.centerIn: parent
                                        text: model.number
                                        color: "#ACBAC7"
                                    }
                                }
                                Rectangle {
                                    width: 140
                                    height: parent.height
                                    color: "#2D333B"
                                    border.color: "#454C56"
                                    border.width: 1
                                    Text {
                                        anchors.centerIn: parent
                                        text: model.name
                                        color: "#ACBAC7"
                                    }
                                }
                                Rectangle {
                                    width: 140
                                    height: parent.height
                                    color: "#2D333B"
                                    border.color: "#454C56"
                                    border.width: 1
                                    Text {
                                        anchors.centerIn: parent
                                        text: model.surname
                                        color: "#ACBAC7"
                                    }
                                }
                                Rectangle {
                                    width: 140
                                    height: parent.height
                                    color: "#2D333B"
                                    border.color: "#454C56"
                                    border.width: 1
                                    Text {
                                        anchors.centerIn: parent
                                        text: model.result
                                        color: "#ACBAC7"
                                    }
                                }
                            }
                        }
                    }
                }        
            }
        }
    }

    Connections {
        target: backend

        function onMessage(message) {
            console.log("Сообщение: " + message)
        }

        function onJsonValid(jsonValid) {
            if (jsonValid == "valid") {
                jsonButton.buttonColor = "green"
                resetButton.buttonColor = "light blue"
            } else if (jsonValid == "error") {
                jsonButton.buttonColor = "red"
            } else {
                jsonButton.buttonColor = "gray"
            }
        }

        function onTxtValid(txtValid) {
            if (txtValid == "valid") {
                txtButton.buttonColor = "green"
                resetButton.buttonColor = "light blue"
            } else if (txtValid == "error") {
                txtButton.buttonColor = "red"
            } else {
                txtButton.buttonColor = "gray"
            }
        }

        function onIsCalculated(isCalculated) {
            if (isCalculated == "valid") {
                calculateButton.buttonColor = "green"
                titleTable.visible = true
            } else {
                calculateButton.buttonColor = "gray"
                titleTable.visible = false
            }
        }

        function onIsSaved(isSaved) {
            if (isSaved === "valid") {
                saveButton.buttonColor = "green"
            } else if (isSaved === "error") {
                saveButton.buttonColor = "red"
            } else {
                saveButton.buttonColor = "gray"
            }
        }

        function onIsReset(isReset) {
            if (isReset == "error") {
                resetButton.buttonColor = "green"
            } else {
                resetButton.buttonColor = "gray"
            }
        }
    }
}