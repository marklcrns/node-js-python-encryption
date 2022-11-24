const crypto = require("node:crypto");
const algorithm = "aes-256-cbc";

const CRYPTO_KEY= "8ookgvdIiH2YOgBnAju6Nmxtp14fn8d3"
const CRYPTO_IV= "rBEssDfxofOveRxR"

async function encryptText(text) {
  const key = CRYPTO_KEY;
  const iv = CRYPTO_IV;

  let cipher = crypto.createCipheriv(algorithm, Buffer.from(key), iv);
  let encryptedText = cipher.update(text, 'utf-8');
  encryptedText = Buffer.concat([encryptedText, cipher.final()]);

  return encryptedText.toString("hex");
}

async function decryptText(inputText) {
  const key = CRYPTO_KEY;
  const iv = CRYPTO_IV;

  let encryptedText = Buffer.from(inputText, "hex");
  let decipher = crypto.createDecipheriv(algorithm, Buffer.from(key), iv);
  let decrypted = decipher.update(encryptedText, 'utf-8');
  decrypted = Buffer.concat([decrypted, decipher.final()]);

  return decrypted.toString();
}

let mac = "80:c9:55:64:73:f0";
let encrypted = encryptText(mac);
let decrypted = decryptText("fe1029a0eac96d22bd53196bfbd8df5210a62afa754e56388109bd25499e78c0");

console.log(encrypted);
console.log(decrypted);

if (mac == decrypted) { console.log("Success") }
