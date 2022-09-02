/**
 * Generates a sequence of characters to be used
 * as a secret key for password hashing and verification
 * writes the output to a file named randomBytes.txt
 */

const crypto = require('crypto')
const fs = require('fs');
const numOfCharacters = 2**12
const str = crypto.randomBytes(numOfCharacters).toString('hex')

fs.writeFileSync('randomBytes.txt', str);
