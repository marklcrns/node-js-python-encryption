#!/usr/bin/env node

const crypto = require('crypto');
const URLSafeBase64 = require('urlsafe-base64');

const input = "80:c9:55:64:73:f0";
const CRYPTO_KEY = "8ookgvdIiH2YOgBnAju6Nmxtp14fn8d3";
const CRYPTO_IV = "rBEssDfxofOveRxR";

// async function encrypt(val) {
function encrypt(val) {
  let cipher = crypto.createCipheriv('aes-256-cbc', CRYPTO_KEY, CRYPTO_IV);
  // UTF-8 to Base64 encoding
  let encrypted = cipher.update(val, 'utf8', 'base64');
  encrypted += cipher.final('base64');
  return URLSafeBase64.encode(encrypted);
};

// async function decrypt(encrypted) {
function decrypt(encrypted) {
  encrypted = URLSafeBase64.decode(encrypted);
  let decipher = crypto.createDecipheriv('aes-256-cbc', CRYPTO_KEY, CRYPTO_IV);
  // Base64 to UTF-8 decoding
  let decrypted = decipher.update(encrypted, 'base64', 'utf8');
  return (decrypted + decipher.final('utf8'));
};

var encrypted_key = encrypt(input);
var original_input = decrypt(encrypted_key);

console.log(encrypted_key);
console.log(original_input);
