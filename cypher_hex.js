const crypto = require('crypto');

const input = "80:c9:55:64:73:f0";
const CRYPTO_KEY = "8ookgvdIiH2YOgBnAju6Nmxtp14fn8d3";
const CRYPTO_IV = "rBEssDfxofOveRxR";

// async function encrypt(val) {
function encrypt(val) {
  let cipher = crypto.createCipheriv('aes-256-cbc', CRYPTO_KEY, CRYPTO_IV);
  // UTF-8 to Hex encoding
  let encrypted = cipher.update(val, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
};

// async function decrypt(encrypted) {
function decrypt(encrypted) {
  let decipher = crypto.createDecipheriv('aes-256-cbc', CRYPTO_KEY, CRYPTO_IV);
  // Hex to UTF-8 decoding
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  return (decrypted + decipher.final('utf8'));
};

var encrypted_key = encrypt(input);
var original_input = decrypt(encrypted_key);

console.log(encrypted_key);
console.log(original_input);
