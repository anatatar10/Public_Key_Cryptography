#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>

// Function to check if a number is prime
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;

    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }

    return true;
}

// Function to compute modular exponentiation (a^b mod m)
int modExp(int base, int exponent, int mod) {
    int result = 1;
    base = base % mod;

    while (exponent > 0) {
        if (exponent % 2 == 1)
            result = (result * base) % mod;

        exponent = exponent >> 1;
        base = (base * base) % mod;
    }

    return result;
}

// Function to generate a random prime number
int generateRandomPrime() {
    int prime;
    do {
        prime = rand() % 100 + 101; // Generate a random number in the range [101, 200]
    } while (!isPrime(prime));

    return prime;
}

// Check if a is a generator for the prime field Z_p
bool isGenerator(int a, int n) {
    if (a <= 1 || a >= n) {
        return false; // Invalid input
    }

    // Factorize n - 1
    int m = n - 1;
    while (m % 2 == 0) {
        m /= 2;
    }

    // Check a^m mod n != 1
    if (modExp(a, m, n) == 1) {
        return false;
    }

    // Check a^(2^i * m) mod n != 1 for i = 0 to k-1
    while (m > 1) {
        int power = modExp(a, m, n);
        if (power == 1) {
            return false;
        }
        m /= 2;
    }

    return true;
}


// Generate a random generator for the prime field Z_p
int generateRandomGenerator(int p) {
    if (p < 2) {
        return -1; // Invalid input
    }

    for (int a = 1; a < p; ++a) {
        if (isGenerator(a, p)) {
            return a;
        }
    }
    return -1; // No generator found (should not occur for prime p)
}


// Function to generate a random private key (a)
int generatePrivateKey(int p) {
    return rand() % (p - 2) + 1; // Generate a random number in the range [1, p - 2]
}

// Function to generate public key (p, g, g^a)
void generatePublicKey(int& p, int& g, int& ga, int& a) {
    p = generateRandomPrime();
    g = generateRandomGenerator(p);
    a = generatePrivateKey(p);
    ga = modExp(g, a, p);
}
// Function to convert a string to a vector of integers (representing the message)
std::vector<int> stringToVector(const std::string& message) {
    std::vector<int> result;
    for (char ch : message) {
        if (isalpha(ch)) {
            result.push_back(toupper(ch) - 'A' + 1);
        }
        else if (ch == ' ') {
            result.push_back(0); // Use 0 to represent space
        }
    }
    return result;
}

// Function to convert a vector of integers to a string (representing the decrypted message)
std::string vectorToString(const std::vector<int>& values) {
    std::string result;
    for (int val : values) {
        if (val == 0) {
            result.push_back(' '); // Convert 0 back to space
        }
        else {
            result.push_back(static_cast<char>('A' + val - 1));
        }
    }
    return result;
}

// Function to encrypt a plaintext message using ElGamal
void encrypt(const std::string& plaintext, int p, int g, int ga, std::vector<int>& alpha, std::vector<int>& beta) {
    std::vector<int> message = stringToVector(plaintext);

    alpha.clear();
    beta.clear();

    for (int m : message) {
        int k = rand() % (p - 2) + 1;
        alpha.push_back(modExp(g, k, p));
        beta.push_back((m * modExp(ga, k, p)) % p);
    }
}

// Function to decrypt a ciphertext message using ElGamal
std::string decrypt(const std::vector<int>& alpha, const std::vector<int>& beta, int a, int p) {
    std::vector<int> decryptedMessage;

    int inverseA = modExp(a, p - 2, p);

    for (size_t i = 0; i < alpha.size(); ++i) {
        int m = (beta[i] * modExp(alpha[i], p - 1 - a, p)) % p;
        decryptedMessage.push_back(m);
    }

    return vectorToString(decryptedMessage);
}



int main() {
    srand(time(0));

    // Step 1: Generate public and private keys
    int p, g, ga, a;
    generatePublicKey(p, g, ga, a);
    std::cout << "Public Key (p, g, g^a): (" << p << ", " << g << ", " << ga << ")\n";
    std::cout << "Private Key (a): " << a << "\n";

    // Step 2: Encryption
    std::string plaintext;
    std::cout << "Enter a message (uppercase letters and spaces only): ";
    std::getline(std::cin, plaintext);

    std::vector<int> alpha, beta;
    encrypt(plaintext, p, g, ga, alpha, beta);

    std::cout << "Ciphertext (alpha, beta): ";
    for (size_t i = 0; i < alpha.size(); ++i) {
        std::cout << "(" << alpha[i] << ", " << beta[i] << ") ";
    }
    std::cout << "\n";

    // Step 3: Decryption
    std::string decryptedMessage = decrypt(alpha, beta, a, p);
    std::cout << "Decrypted Message: " << decryptedMessage << "\n";

    return 0;
}
