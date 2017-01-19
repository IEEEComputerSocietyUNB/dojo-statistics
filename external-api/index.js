const router = require('../index')

const fs = require('fs')
const readline = require('readline')
const google = require('googleapis')
const googleAuth = require('google-auth-library')

const SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
const TOKEN_DIR = (process.env.HOME || process.env.HOMEPATH ||
    process.env.USERPROFILE) + '/.credentials/';
const TOKEN_PATH = TOKEN_DIR + 'sheets.googleapis.com-nodejs-quickstart.json';

fs.readFile('client_secret.json', function processClientSecrets(err, content) {
    if(err) {
        console.error('Error loading client secret file:', err)
        return
    }

    authorize(JSON.parse(content), retrieveData)
})

function authorize(credentials, callback)
{
    let clientSecret = credentials.installed.client_secret
    let clientId = credentials.installed.client_id
    let redirectUrl = credentials.installed.redirect_uris[0]

    let auth = new googleAuth()
    let oauth2Client = new auth.OAuth2(clientId, clientSecret, redirectUrl)

    fs.readFile(TOKEN_PATH, (err, token) => {
        if(err) getNewToken(oauth2Client, callback)
        else {
            oauth2Client.credentials = JSON.parse(token)
            callback(oauth2Client)
        }
    })
}

function getNewToken(oauth2Client, callback)
{
    let authUrl = oauth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES
    })
    console.log('Authorize this app by visiting this url: ', authUrl);

    let rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })

    rl.question('Enter the code from that page here: ', code => {
        rl.close()
        oauth2Client.getToken(code, (err, token) => {
            if(err) {
                console.error('Error while trying to retrieve access token', err)
                return
            }
            oauth2Client.credentials = token
            storeToken(token)
            callback(oauth2Client)
        })
    })
}

function storeToken(token)
{
    try {
        fs.mkdirSync(TOKEN_DIR)
    } catch(err) {
        if(err.code != 'EEXIST') throw err
    }

    fs.writeFile(TOKEN_PATH, JSON.stringify(token))
    console.log('Token stored to ' + TOKEN_PATH)
}

function retrieveData(auth)
{
    let sheets = google.sheets('v4')
    sheets.spreadsheets.values.get({
        auth: auth,
        spreadsheetId: '1UkCheR39HB27Tc7aE8_OmyTNEP8HguLstVlvkuHNBd4',
        range: 'A:B'
    }, (err, response) => {
        if(err) {
            console.error('The API returned an error: ' + err)
            return
        }

        let rows = response.values
        if(rows.length === 0) console.log('No data found')
        else {
            rows.forEach(row => {
                console.log('%s, %s', row[0], row[1])
            })
        }
    })
}

module.exports = {
    user: {
        authenticated: false
    },

    login() {
        
    }
}
