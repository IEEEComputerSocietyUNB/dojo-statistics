const {app, BrowserWindow, ipcMain} = require('electron')

const path = require('path')
const url = require('url')

let win

function createWindow(name) {

    if(win) win = null

    win = new BrowserWindow({
        title: '',
        backgroundColor: '#5cab7d'
    })

    win.maximize()

    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }))

    win.webContents.openDevTools()

    win.on('closed', () => {
        win = null
    })
}

app.on('ready', () => createWindow('main'))

app.on('window-all-closed', () => {
    if(process.platform !== 'darwin')
        app.quit()
})

app.on('activate', () => {
    if(win.main === null)
        createWindow('main')
})
