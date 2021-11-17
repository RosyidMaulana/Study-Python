from PySide import QtCore, QtGui, QtWebKit

import sys, time



class TabDialog(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)



        self.penampungTab = []

        self.tambah = False



        self.inisialisasiTab()

        self.tambahTab()

        self.tabKeWindow()



    def inisialisasiTab(self):

        self.elemenTab = QtGui.QTabWidget(self)

        # self.elemenTab.addTab(GeneralTab(), "General")

        self.elemenTab.setMovable(True)

        self.elemenTab.tabCloseRequested.connect(self.tutup)



        self.tabButton = QtGui.QToolButton(self)

        self.tabButton.setText('+')

        font = self.tabButton.font()

        font.setBold(True)

        self.tabButton.setFont(font)

        self.elemenTab.setCornerWidget(self.tabButton, QtCore.Qt.TopLeftCorner)

        self.tabButton.clicked.connect(self.tambahTab)



    def tambahTab(self):

        self.penampungTab.append(Browser(parent=self))

        a = self.elemenTab.addTab(self.penampungTab[len(self.penampungTab) - 1], "No Internet Connection")

        self.elemenTab.setTabShape(QtGui.QTabWidget.Triangular)

        self.tambah = True



        if self.elemenTab.count() < 2:

            self.elemenTab.setTabsClosable(False)

        else:

            self.elemenTab.setTabsClosable(True)



        self.elemenTab.setCurrentIndex(self.elemenTab.count() - 1)



    def tabKeWindow(self):

        self.centralWidget = QtGui.QWidget(self)



        mainLayout = QtGui.QVBoxLayout(self.centralWidget)

        mainLayout.addWidget(self.elemenTab)

        mainLayout.setContentsMargins(0, 0, 0, 0)



        self.setCentralWidget(self.centralWidget)

        self.setWindowTitle("Mini WebBrowser -> mn-belajarpython.blogspot.co.id")



    def perintahTutup(self):

        if self.elemenTab.count() > 1:

            posisi = self.elemenTab.currentIndex()

            self.elemenTab.removeTab(posisi)

            if self.elemenTab.count() == 1:

                self.elemenTab.setTabsClosable(False)



    def tutup(self, i):

        self.elemenTab.removeTab(i)

        if self.elemenTab.count() < 2:

            self.elemenTab.setTabsClosable(False)



    def tabBukaLinkDariHistory(self, url):

        browser = Browser(parent=self, url=url)

        self.penampungTab.append(browser)

        a = self.elemenTab.addTab(self.penampungTab[len(self.penampungTab) - 1], "No Internet Connection")

        self.tambah = True



        if self.elemenTab.count() < 2:

            self.elemenTab.setTabsClosable(False)

        else:

            self.elemenTab.setTabsClosable(True)



        self.elemenTab.setCurrentIndex(self.elemenTab.count() - 1)



    def tabHistory(self):

        a = self.elemenTab.addTab(History(parent=self), "History")

        self.tambah = True



        self.elemenTab.setCurrentIndex(self.elemenTab.count() - 1)



        if self.elemenTab.count() < 2:

            self.elemenTab.setTabsClosable(False)

        else:

            self.elemenTab.setTabsClosable(True)



    def setJudul(self, teks, memori, tooltip):

        for i in range(self.elemenTab.count()):

            if self.elemenTab.widget(i).getPosisiMemory() == memori:

                self.elemenTab.setTabText(i, teks)

                self.elemenTab.setTabToolTip(i, tooltip)



    def closeEvent(self, event):

        self.destroy()





class Browser(QtGui.QMainWindow):

    def __init__(self, parent=None, url=''):

        QtGui.QMainWindow.__init__(self)

        self.parent = parent

        self.resize(800, 600)

        self.centralwidget = QtGui.QWidget(self)



        self.default_url = "https://google.co.id"

        self.urlTab = url

        self.penampungHistory = []



        self.layout()

        self.buatToolbar()

        self.buatKolomCari()

        self.windowBrowser()

        self.browse()



    def layout(self):

        self.layoutUtama = QtGui.QHBoxLayout(self.centralwidget)

        self.layoutUtama.setContentsMargins(0, 0, 0, 0)



        self.frame = QtGui.QFrame(self.centralwidget)

        self.layoutBrowser = QtGui.QVBoxLayout(self.frame)

        self.layoutBrowser.setSpacing(0)



    def setValueProgressbar(self, pos):

        self.progressBar.setValue(pos)

        self.tombolReload.setIcon(self.style().standardIcon(QtGui.QStyle.SP_BrowserStop))

        self.progressBar.setVisible(True)



        self.tombolMaju.setEnabled(self.webBrowser.history().canGoForward())

        self.tombolKembali.setEnabled(self.webBrowser.history().canGoBack())



    def buatToolbar(self):

        self.layoutToolbar = QtGui.QHBoxLayout()



        self.kolomUrl = QtGui.QLineEdit(self.frame)

        self.kolomUrl.returnPressed.connect(self.browse)



        self.tombolKembali = QtGui.QAction(self.style().standardIcon(QtGui.QStyle.SP_ArrowBack), 'kembali', self.frame)

        self.tombolKembali.triggered.connect(self.perintahKembali)

        self.tombolKembali.setEnabled(False)

        self.tombolMaju = QtGui.QAction(self.style().standardIcon(QtGui.QStyle.SP_ArrowForward), 'maju', self.frame)

        self.tombolMaju.triggered.connect(self.perintahMaju)

        self.tombolMaju.setEnabled(False)

        self.tombolReload = QtGui.QAction(self.style().standardIcon(QtGui.QStyle.SP_BrowserReload), 'muat ulang',

                                          self.frame)

        self.tombolReload.triggered.connect(self.perintahReload)



        bar = QtGui.QToolBar()



        bar.addAction(self.tombolKembali)

        bar.addAction(self.tombolMaju)

        bar.addAction(self.tombolReload)



        self.tombolGo = QtGui.QPushButton(text='Go')

        self.tombolGo.clicked.connect(self.browse)



        self.layoutToolbar.addWidget(bar)

        self.layoutToolbar.addWidget(self.kolomUrl)

        self.layoutToolbar.addWidget(self.tombolGo)

        self.layoutToolbar.setContentsMargins(0, 0, 0, 0)

        self.layoutBrowser.setContentsMargins(0, 0, 0, 0)

        self.layoutBrowser.addLayout(self.layoutToolbar)



        self.menuTabBaru = QtGui.QAction(self, text='Tab Baru')

        self.menuTabBaru.triggered.connect(self.parent.tambahTab)

        self.menuTutupTab = QtGui.QAction(self, text='Tutup Tab')

        self.menuTutupTab.triggered.connect(self.parent.perintahTutup)

        self.menuHistory = QtGui.QAction(self, text='History')

        self.menuHistory.triggered.connect(self.parent.tabHistory)

        self.menuCetak = QtGui.QAction(self, text='Cetak')

        self.menuCetak.triggered.connect(self.perintahCetak)

        self.menuCari = QtGui.QAction(self, text='Cari')

        self.menuCari.triggered.connect(self.perintahBukaPencarian)

        self.menuWeb = QtGui.QAction(self, text='Web')

        self.menuWeb.triggered.connect(self.perintahWeb)

        self.menuAbout = QtGui.QAction(self, text='About')

        self.menuAbout.triggered.connect(self.tentang)

        self.menuAboutQt = QtGui.QAction(self, text='About Qt')

        self.menuAboutQt.triggered.connect(self.tentangQt)

        self.menuExit = QtGui.QAction(self, text='Exit')

        self.menuExit.triggered.connect(self.parent.close)



        self.menu = QtGui.QMenu(self)

        self.menu.addAction(self.menuTabBaru)

        self.menu.addAction(self.menuTutupTab)

        self.menu.addSeparator()

        self.menu.addAction(self.menuHistory)

        self.menu.addAction(self.menuCetak)

        self.menu.addAction(self.menuCari)

        self.menu.addSeparator()

        self.menu.addAction(self.menuAbout)

        self.menu.addAction(self.menuAboutQt)

        self.menu.addAction(self.menuWeb)

        self.menu.addAction(self.menuExit)



        self.buttonShow = QtGui.QPushButton(self)

        self.buttonShow.setText("")

        self.buttonShow.setMenu(self.menu)

        self.buttonShow.setFlat(True)



        self.layoutToolbar.addWidget(self.buttonShow)

        self.layoutToolbar.addWidget(self.buttonShow)



        self.progressBar = QtGui.QProgressBar()

        self.layoutBrowser.addWidget(self.progressBar)

        self.progressBar.setVisible(False)



    def tentang(self):

        QtGui.QMessageBox.information(self, "Tentang aplikasi",

                                      self.tr("Aplikasi ini merupakan sebuah apliakasi sederhana. "

                                              "Namun, saya rasa aplikasi ini sudah cukup bagus. "

                                              "dari segi design. karena, didukung oleh modul yang "

                                              "cukup lengkap dari PySide. sehingga saya hanya "

                                              "menggunakannya saja\n"

                                              "\nnah gimana ? menarikkan ? yuk kunjungi :  "

                                              "mn-belajarpython.blogspot.co.id untuk tutorial "

                                              "menarik lainnya..."))



    def tentangQt(self):

        QtGui.QMessageBox.aboutQt(self)



    def perintahCetak(self):

        infoPrinter = QtGui.QPrinterInfo()

        printer = QtGui.QPrinter(infoPrinter)

        self.webBrowser.print(printer)



    def windowBrowser(self):

        self.webBrowser = QtWebKit.QWebView()



        self.layoutBrowser.addWidget(self.webBrowser)

        self.layoutUtama.addWidget(self.frame)

        self.setCentralWidget(self.centralwidget)



    def buatKolomCari(self):

        layoutKolomCari = QtGui.QHBoxLayout(self)



        self.teks = QtGui.QLabel(self, text='Kata kunci : ')

        layoutKolomCari.addWidget(self.teks)



        self.tombolNext = QtGui.QPushButton(self, text='Next')

        self.tombolPrevious = QtGui.QPushButton(self, text='Previous')

        self.tombolTutup = QtGui.QPushButton(self, text='X')



        self.tombolTutup.clicked.connect(self.perintahTutupPencarian)

        self.tombolNext.clicked.connect(self.cariNext)

        self.tombolPrevious.clicked.connect(self.cariPrevious)



        self.tombolPrevious.setFlat(True)

        self.tombolNext.setFlat(True)



        self.tombolPrevious.setFixedSize(60, 20)

        self.tombolNext.setFixedSize(45, 20)

        self.tombolTutup.setFixedSize(20, 25)



        self.kolomCari = QtGui.QLineEdit(self)

        self.kolomCari.editingFinished.connect(self.cariNext)

        layoutKolomCari.addWidget(self.kolomCari)

        self.kolomCari.setFixedSize(200, 20)



        layoutKolomCari.addWidget(self.tombolNext)

        layoutKolomCari.addWidget(self.tombolPrevious)

        layoutKolomCari.addWidget(self.tombolTutup)



        layoutKolomCari.setAlignment(self.teks, QtCore.Qt.AlignRight)



        self.layoutBrowser.addLayout(layoutKolomCari)

        self.setVisiblePencari(False)



    def perintahTutupPencarian(self):

        self.setVisiblePencari(False)



    def perintahBukaPencarian(self):

        self.setVisiblePencari(True)

        self.kolomCari.setFocus()



    def cariPrevious(self):

        teks = self.kolomCari.text()

        gtw = QtWebKit.QWebPage.FindBackward

        self.webBrowser.findText(teks, gtw)



    def cariNext(self):

        teks = self.kolomCari.text()

        self.webBrowser.findText(teks)



    def setVisiblePencari(self, argumen):

        self.tombolPrevious.setVisible(argumen)

        self.tombolNext.setVisible(argumen)

        self.kolomCari.setVisible(argumen)

        self.teks.setVisible(argumen)

        self.tombolTutup.setVisible(argumen)



    def perintahWeb(self):

        self.webBrowser.load(QtCore.QUrl('http://mn-belajarpython.blogspot.co.id'))



    def browse(self):

        url = 'https://google.co.id'

        if self.urlTab:

            url = self.urlTab

            self.urlTab = ''

        elif self.kolomUrl.text():

            try:

                url = self.kolomUrl.text()

                url = url.lower()

                penampungUrl = []



                for i in url:

                    penampungUrl.append(i)



                if penampungUrl[0] != 'h' and penampungUrl[1] != 't' and penampungUrl[2] != 't' and penampungUrl[

                    3] != 'p' and penampungUrl[3] != 's' and penampungUrl[3] != '/' and penampungUrl[3] != '/':

                    if penampungUrl[0] == 'w' and penampungUrl[1] == 'w' and penampungUrl[2] == 'w' and penampungUrl[

                        3] == '.':

                        url = 'https://' + url

                    else:

                        urlPengganti = ''

                        for i in url:

                            if i != ' ':

                                urlPengganti += i

                            else:

                                urlPengganti += '+'

                            url = "https://www.google.co.id/search?espv=2&q=" + urlPengganti

            except:

                urlPengganti = ''

                for i in url:

                    if i != ' ':

                        urlPengganti += i

                    else:

                        urlPengganti += '+'

                    url = "https://www.google.co.id/search?espv=2&q=" + urlPengganti



        self.webBrowser.load(QtCore.QUrl(url))



        self.tombolMaju.setEnabled(self.webBrowser.history().canGoForward())

        self.tombolKembali.setEnabled(self.webBrowser.history().canGoBack())



        self.webBrowser.iconChanged.connect(self.kirimIcon)

        self.webBrowser.urlChanged.connect(self.setKolomUrl)

        self.webBrowser.loadProgress.connect(self.setValueProgressbar)

        self.webBrowser.loadFinished.connect(self.selesaiMemuat)

        self.webBrowser.titleChanged.connect(self.kirimJudul)



        self.webBrowser.show()



    def selesaiMemuat(self):

        self.tombolReload.setIcon(self.style().standardIcon(QtGui.QStyle.SP_BrowserReload))

        self.progressBar.setVisible(False)



    def perintahKembali(self):

        self.webBrowser.back()



    def perintahMaju(self):

        self.webBrowser.forward()



    def perintahReload(self):

        self.webBrowser.reload()



    def setKolomUrl(self):

        self.kolomUrl.setText(self.webBrowser.url().toString())



        jam = time.strftime("%H:%M", time.localtime())

        url = self.webBrowser.url().toString()



        self.penampungHistory.append([jam, url])



    def getPosisiMemory(self):

        return (str(self))



    def kirimJudul(self):

        judul = self.webBrowser.title()

        tab = self.parent

        memori = self.getPosisiMemory()

        toolTip = judul



        self.penampungHistory[len(self.penampungHistory) - 1].insert(1, judul)



        judulBaru = ''



        if len(judul) > 10:

            for i in range(len(judul)):

                judulBaru += judul[i]

                if i > 9:

                    judul = judulBaru + '...'

                    break



        tab.setJudul(judul, memori, toolTip)



    def closeEvent(self, event):

        self.destroy()





class History(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self)

        self.parent = parent

        self.centralWidget = QtGui.QWidget(self)

        self.layout = QtGui.QHBoxLayout(self.centralWidget)

        self.buatWindow()

        self.setCentralWidget(self.centralWidget)



    def klikTabel(self, baris, kolom):

        self.tablewidget.selectRow(baris)

        data = self.tablewidget.item(baris, 2).text()

        self.parent.tabBukaLinkDariHistory(data)



    def klik(self, baris, kolom):

        self.tablewidget.selectRow(baris)



    def updateTabel(self):

        for i in range(self.tablewidget.rowCount()):

            self.tablewidget.removeRow(0)

        for i in range(len(self.data)):



            try:

                jam = self.data[i][0]

                nama = self.data[i][1]

                url = self.data[i][3]

            except:

                try:

                    jam = self.data[i][0]

                    nama = self.data[i][1]

                    url = self.data[i][2]

                except:

                    pass



            self.tablewidget.insertRow(i)

            jam = QtGui.QTableWidgetItem(jam)

            nama = QtGui.QTableWidgetItem(nama)

            url = QtGui.QTableWidgetItem(str(url))



            jam.setFlags(jam.flags() ^ QtCore.Qt.ItemIsEditable)

            nama.setFlags(nama.flags() ^ QtCore.Qt.ItemIsEditable)

            url.setFlags(url.flags() ^ QtCore.Qt.ItemIsEditable)



            self.tablewidget.setItem(i, 0, jam)

            self.tablewidget.setItem(i, 1, nama)

            self.tablewidget.setItem(i, 2, url)



    def buatWindow(self):

        title = ['Waktu', 'Nama', 'Alamat']

        self.data = []



        for i in range(len(self.parent.penampungTab)):

            self.data += self.parent.penampungTab[i].penampungHistory



        # besarnya kolom

        colcnt = len(title)

        rowcnt = len(self.data)



        self.tablewidget = QtGui.QTableWidget(rowcnt, colcnt, self)



        self.connect(self.tablewidget, QtCore.SIGNAL('cellDoubleClicked(int, int)'), self.klikTabel)

        self.connect(self.tablewidget, QtCore.SIGNAL('cellPressed(int, int)'), self.klik)



        # judul vertikal

        vheader = QtGui.QHeaderView(QtCore.Qt.Orientation.Vertical)

        vheader.setResizeMode(QtGui.QHeaderView.ResizeToContents)

        self.tablewidget.setVerticalHeader(vheader)



        # judul horizontal

        hheader = QtGui.QHeaderView(QtCore.Qt.Orientation.Horizontal)

        hheader.setResizeMode(QtGui.QHeaderView.ResizeToContents)

        self.tablewidget.setHorizontalHeader(hheader)

        self.tablewidget.setHorizontalHeaderLabels(title)



        self.updateTabel()



        self.layout.addWidget(self.tablewidget)



    def getPosisiMemory(self):

        return (str(self))



    def closeEvent(self, event):

        self.destroy()



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    main = TabDialog()

    main.show()

    sys.exit(app.exec_())