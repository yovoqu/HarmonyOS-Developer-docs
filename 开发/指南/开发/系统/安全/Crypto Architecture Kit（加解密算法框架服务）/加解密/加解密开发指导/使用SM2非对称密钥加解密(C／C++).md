# 使用SM2非对称密钥加解密(C/C++)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt-ndk

对应的算法规格请查看[非对称密钥加解密算法规格：SM2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec#sm2)。

**加密**


**解密**


```text
#include "CryptoArchitectureKit/crypto_architecture_kit.h"
#include
#include
#include

static std::vector doTestSm2Enc(OH_CryptoKeyPair *keyPair, std::vector &plainText)
{
    std::vector cipherText;
    OH_CryptoAsymCipher *cipher = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("SM2_256|SM3", &cipher);
    if (ret != CRYPTO_SUCCESS) {
        return std::vector{};
    }

    ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_ENCRYPT_MODE, keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymCipher_Destroy(cipher);
        return std::vector{};
    }

    Crypto_DataBlob in = {};
    in.data = plainText.data();
    in.len = plainText.size();
    Crypto_DataBlob out = {};
    ret = OH_CryptoAsymCipher_Final(cipher, &in, &out);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymCipher_Destroy(cipher);
        return std::vector{};
    }
    cipherText.insert(cipherText.end(), out.data, out.data + out.len);
    OH_Crypto_FreeDataBlob(&out);

    OH_CryptoAsymCipher_Destroy(cipher);
    return cipherText;
}

static std::vector doTestSm2Dec(OH_CryptoKeyPair *keyPair, std::vector &encryptText)
{
    std::vector decryptText;
    OH_CryptoAsymCipher *cipher = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("SM2_256|SM3", &cipher);
    if (ret != CRYPTO_SUCCESS) {
        return std::vector{};
    }

    ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_DECRYPT_MODE, keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymCipher_Destroy(cipher);
        return std::vector{};
    }

    Crypto_DataBlob in = {};
    in.data = encryptText.data();
    in.len = encryptText.size();
    Crypto_DataBlob out = {};
    ret = OH_CryptoAsymCipher_Final(cipher, &in, &out);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymCipher_Destroy(cipher);
        return std::vector{};
    }
    decryptText.insert(decryptText.end(), out.data, out.data + out.len);
    OH_Crypto_FreeDataBlob(&out);

    OH_CryptoAsymCipher_Destroy(cipher);
    return decryptText;
}

OH_Crypto_ErrCode doTestSm2EncMessage()
{
    OH_CryptoAsymKeyGenerator *keyGen = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("SM2_256", &keyGen);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    OH_CryptoKeyPair *keyPair = nullptr;
    ret = OH_CryptoAsymKeyGenerator_Generate(keyGen, &keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(keyGen);
        return ret;
    }

    std::string message = "This is a test";
    std::vector plainText(message.begin(), message.end());
    std::vector cipherText = doTestSm2Enc(keyPair, plainText);
    std::vector decryptText = doTestSm2Dec(keyPair, cipherText);

    if ((plainText.size() != decryptText.size()) ||
        (!std::equal(plainText.begin(), plainText.end(), decryptText.begin()))) {
        OH_CryptoKeyPair_Destroy(keyPair);
        OH_CryptoAsymKeyGenerator_Destroy(keyGen);
        return CRYPTO_OPERTION_ERROR;
    }

    OH_CryptoKeyPair_Destroy(keyPair);
    OH_CryptoAsymKeyGenerator_Destroy(keyGen);
    return CRYPTO_SUCCESS;
}
```
