/*
    call api.fetch()
        .then(responseObject)
        .catch({
            uri: authUrl,
            answer: answer()
                .then(responseObject)
                .catch(errorMsg)
        })
        .catch(errorMsg)
*/

import router from '../index'

import fs from 'fs'
import google from 'googleapis'
import googleAuth from 'google-auth-library'

const SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
const TOKEN_DIR = (process.env.HOME || process.env.HOMEPATH ||
    process.env.USERPROFILE) + '/.credentials/';
const TOKEN_PATH = TOKEN_DIR + 'sheets.googleapis.com-nodejs-quickstart.json';

function authorize(credentials)
{
    return new Promise((resolve, reject) => {
        let clientSecret = credentials.installed.client_secret
        let clientId = credentials.installed.client_id
        let redirectUrl = credentials.installed.redirect_uris[0]

        let auth = new googleAuth()
        let oauth2Client = new auth.OAuth2(clientId, clientSecret, redirectUrl)

        fs.readFile(TOKEN_PATH, (err, token) => {
            if(err) reject(oauth2Client)
            else {
                oauth2Client.credentials = JSON.parse(token)
                resolve(oauth2Client)
            }
        })
    })
}

function getNewToken(oauth2Client, callback)
{
    return new Promise((resolve, reject) => {
        let authUrl = oauth2Client.generateAuthUrl({
            access_type: 'offline',
            scope: SCOPES
        })
        resolve({
            uri: authUrl,
            answer: answer
        })
    })

    function answer(code)
    {
        return new Promise((resolve, reject) => {
            oauth2Client.getToken(code, (err, token) => {
                if(err) reject('Error while trying to retrieve access token')
                else
                {
                    oauth2Client.credentials = token
                    storeToken(token)
                    resolve(retrieveData(oauth2Client))
                }
            })
        })
    }
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
    return new Promise((resolve, reject) => {
        let sheets = google.sheets('v4')
        sheets.spreadsheets.values.get({
            auth: auth,
            spreadsheetId: '1UkCheR39HB27Tc7aE8_OmyTNEP8HguLstVlvkuHNBd4',
            range: 'A:B'
        }, (err, response) => {
            if(err) reject('The API returned an error: ' + err)

            let rows = response.values
            if(rows.length === 0) reject('No data found')
            else resolve(rows)
        })
    })
}

module.exports = {

    fetch() {
        return new Promise((resolve, reject) => {
            fs.readFile('client_secret.json', (err, content) => {
                if(err) {
                    reject(`Error loading client secret file: ${JSON.stringify(err)}`)
                }
                else
                    authorize(JSON.parse(content))
                    .then(auth => resolve(retrieveData(auth)))
                    .catch(auth => reject(getNewToken(auth)))
            })
        })
    }
}
