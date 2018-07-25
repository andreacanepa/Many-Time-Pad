# one-time-pad

In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a one-time pre-shared key the same size as, or longer than, the message being sent. 
It satisfies the perfect-secrecy's requirements.

# perfect secrecy

<p><b>P(M=m|C=c)=P(M=m)</b></p>

<p> i.e. seeing a ciphertext doesn't give you any extra information about the plaintext. The probability of seeing a message m after the ciphertext has been observed is the same as the probability of the message without the ciphertext. </p>

# many-time-pad

Let us see what goes wrong when a "one-time" pad is used more than once.

The file "ciphertexts.txt" contains some hex-encoded ciphertexts that are the result of encrypting some ASCII messages with the same pad.

Note:
1) Cleartext messages contain only letters and spaces
2) The key idea to crack this code is considering what happens when a space is XORed with a (uppercase/lowercase) letter

The idea for this exercise has been taken from the excellent course "Cryptography I" on Coursera (https://www.coursera.org/course/crypto)

You may find the following resources useful:
<ul>
  <il>https://docs.python.org/3/library/argparse.html</il>
<il>https://docs.python.org/3/library/binascii.html</il>
<il>https://docs.python.org/3/library/stdtypes.html#string-methods</il>
<il>https://docs.python.org/3/library/functions.html#func-range</il>
<il>https://docs.python.org/3/library/functions.html#enumerate</il>
<il>https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations</il>
</ul>


