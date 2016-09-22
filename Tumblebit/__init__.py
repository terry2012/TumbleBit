import ctypes
import ctypes.util

###########################################################################
## CTypes -- Function Definitions
###########################################################################

########################################################
## Standard C Library
########################################################

_libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('libc'))

_libc.fopen.restype = ctypes.c_void_p
_libc.fopen.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

_libc.fclose.restype = ctypes.c_int
_libc.fclose.argtypes = [ctypes.c_void_p]

########################################################
## LibreSSL
########################################################

# Change path to where libressl library is
# TODO: Find a way to automate this
path = "/usr/local/opt/libressl/lib/libssl.dylib"
_ssl = ctypes.cdll.LoadLibrary(path)


class LibreSSLException(OSError):
    pass


# Taken from python-bitcoinlib key.py
# Thx to Sam Devlin for the ctypes magic 64-bit fix
def _check_res_void_p(val, func, args):
    if val == 0:
        errno = _ssl.ERR_get_error()
        errmsg = ctypes.create_string_buffer(120)
        _ssl.ERR_error_string_n(errno, errmsg, 120)
        raise LibreSSLException(errno, str(errmsg.value))

    return ctypes.c_void_p(val)


def _print_ssl_error():
    errno = _ssl.ERR_get_error()
    errmsg = ctypes.create_string_buffer(120)
    _ssl.ERR_error_string_n(errno, errmsg, 120)
    raise OpenSSLException(errno, str(errmsg.value))

_ssl.SSL_load_error_strings()

#####################################
## Constants
#####################################

RSA_F4 = 65537
RSA_NO_PADDING = 3

#####################################
## BN
#####################################

##################
## BN
##################

_ssl.BN_new.errcheck = _check_res_void_p
_ssl.BN_new.restype = ctypes.c_void_p
_ssl.BN_new.argtypes = None

_ssl.BN_free.restype = None
_ssl.BN_free.argtypes = [ctypes.c_void_p]

_ssl.BN_num_bits.restype = ctypes.c_int
_ssl.BN_num_bits.argtypes = [ctypes.c_void_p]

_ssl.BN_set_word.restype = ctypes.c_int
_ssl.BN_set_word.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

_ssl.BN_gcd.restype = ctypes.c_int
_ssl.BN_gcd.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                        ctypes.c_void_p, ctypes.c_void_p]

##################
## Conversions
##################

_ssl.BN_bn2bin.restype = ctypes.c_int
_ssl.BN_bn2bin.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

_ssl.BN_bin2bn.errcheck = _check_res_void_p
_ssl.BN_bin2bn.restype = ctypes.c_void_p
_ssl.BN_bin2bn.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p]

##################
## BN_CTX
##################

_ssl.BN_CTX_new.errcheck = _check_res_void_p
_ssl.BN_CTX_new.restype = ctypes.c_void_p
_ssl.BN_CTX_new.argtypes = None

_ssl.BN_CTX_free.restype = None
_ssl.BN_CTX_free.argtypes = [ctypes.c_void_p]

_ssl.BN_CTX_start.restype = None
_ssl.BN_CTX_start.argtypes = [ctypes.c_void_p]
_ssl.BN_new.errcheck = _check_res_void_p
_ssl.BN_new.restype = ctypes.c_void_p
_ssl.BN_new.argtypes = None
_ssl.BN_CTX_end.restype = None
_ssl.BN_CTX_end.argtypes = [ctypes.c_void_p]

_ssl.BN_CTX_get.errcheck = _check_res_void_p
_ssl.BN_CTX_get.restype = ctypes.c_void_p
_ssl.BN_CTX_get.argtypes = [ctypes.c_void_p]

##################
## Operations
##################

_ssl.BN_mod_inverse.errcheck = _check_res_void_p
_ssl.BN_mod_inverse.restype = ctypes.c_void_p
_ssl.BN_mod_inverse.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                ctypes.c_void_p, ctypes.c_void_p]


_ssl.BN_mod_mul.restype = ctypes.c_int
_ssl.BN_mod_mul.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                            ctypes.c_void_p, ctypes.c_void_p,
                            ctypes.c_void_p]

_ssl.BN_mod_exp.restype = ctypes.c_int
_ssl.BN_mod_exp.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                            ctypes.c_void_p, ctypes.c_void_p,
                            ctypes.c_void_p]

##################
## BN_BLINDING
##################

_ssl.BN_BLINDING_new.errcheck = _check_res_void_p
_ssl.BN_BLINDING_new.restype = ctypes.c_void_p
_ssl.BN_BLINDING_new.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                 ctypes.c_void_p]

_ssl.BN_BLINDING_free.restype = None
_ssl.BN_BLINDING_free.argtypes = [ctypes.c_void_p]

_ssl.BN_BLINDING_invert_ex.restype = ctypes.c_int
_ssl.BN_BLINDING_invert_ex.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                       ctypes.c_void_p, ctypes.c_void_p]

_ssl.BN_BLINDING_convert_ex.restype = ctypes.c_int
_ssl.BN_BLINDING_convert_ex.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                        ctypes.c_void_p, ctypes.c_void_p]

#####################################
## RSA
#####################################

_ssl.RSA_new.errcheck = _check_res_void_p
_ssl.RSA_new.restype = ctypes.c_void_p
_ssl.RSA_new.argtypes = None

_ssl.RSA_free.restype = None
_ssl.RSA_free.argtypes = [ctypes.c_void_p]

_ssl.i2d_RSAPublicKey.restype = ctypes.c_int
_ssl.i2d_RSAPublicKey.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

_ssl.RSA_generate_key_ex.restype = ctypes.c_int
_ssl.RSA_generate_key_ex.argtypes = [ctypes.c_void_p, ctypes.c_int,
                                     ctypes.c_void_p, ctypes.c_void_p]

_ssl.RSA_blinding_on.restype = ctypes.c_int
_ssl.RSA_blinding_on.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

_ssl.RSA_size.restype = ctypes.c_int
_ssl.RSA_size.argtypes = [ctypes.c_void_p]

_ssl.RSA_private_encrypt.restype = ctypes.c_int
_ssl.RSA_private_encrypt.argtypes = [ctypes.c_int, ctypes.c_char_p,
                                     ctypes.c_void_p, ctypes.c_void_p,
                                     ctypes.c_int]

_ssl.RSA_public_decrypt.restype = ctypes.c_int
_ssl.RSA_public_decrypt.argtypes = [ctypes.c_int, ctypes.c_void_p,
                                    ctypes.c_void_p, ctypes.c_void_p,
                                    ctypes.c_int]

#####################################
## BIO
#####################################

_ssl.BIO_new_file.errcheck = _check_res_void_p
_ssl.BIO_new_file.restype = ctypes.c_void_p
_ssl.BIO_new_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

_ssl.BIO_free_all.restype = None
_ssl.BIO_free_all.argtypes = [ctypes.c_void_p]

#####################################
## PEM
#####################################

_ssl.PEM_write_bio_RSAPublicKey.restype = ctypes.c_int
_ssl.PEM_write_bio_RSAPublicKey.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

_ssl.PEM_write_bio_RSAPrivateKey.restype = ctypes.c_int
_ssl.PEM_write_bio_RSAPrivateKey.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                             ctypes.c_void_p,
                                             ctypes.c_char_p, ctypes.c_int,
                                             ctypes.c_void_p, ctypes.c_void_p]

_ssl.PEM_read_RSAPublicKey.errcheck = _check_res_void_p
_ssl.PEM_read_RSAPublicKey.restype = ctypes.c_void_p
_ssl.PEM_read_RSAPublicKey.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                       ctypes.c_void_p, ctypes.c_void_p]

_ssl.PEM_read_RSAPrivateKey.errcheck = _check_res_void_p
_ssl.PEM_read_RSAPrivateKey.restype = ctypes.c_void_p
_ssl.PEM_read_RSAPrivateKey.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                                        ctypes.c_void_p, ctypes.c_void_p]


###########################################################################
## Helpers
###########################################################################

def _free_bn(self, x):
    if x is not None:
        _ssl.BN_free(x)


def BN_num_bytes(bn):
    return (_ssl.BN_num_bits(bn) + 7) // 8


def BNToBin(bn, data, data_len):
    if bn is None or data is None:
        return None

    offset = data_len - BN_num_bytes(bn)
    ret = _ssl.BN_bn2bin(bn, ctypes.byref(data, offset))
    for i in range(offset):
        data[i] = 0

    return data[:data_len]


def get_random(bits, mod=None):
    ctx = _ssl.BN_CTX_new()
    _ssl.BN_CTX_start(ctx)
    r = _ssl.BN_CTX_get(ctx)
    ret = _ssl.BN_CTX_get(ctx)

    if mod:
        if _ssl.BN_rand_range(r, n) == 0:
            print("get_random: failed to generate random number")

        while _ssl.BN_gcd(ret, r, n, ctx) != 1:
            print("R is not a relative prime")
            if _ssl.BN_rand_range(r, n) == 0:
                print("get_random: failed to generate random number")

    else:
        if _ssl.BN_rand(r, bits, 0, 1) == 0:
            print("get_random: failed to generate random number")

    r_len = BN_num_bytes(r)
    rand = ctypes.create_string_buffer(r_len)
    _ssl.BN_bn2bin(r, rand)

    _ssl.BN_free(r)
    _ssl.BN_CTX_end(ctx)
    _ssl.BN_CTX_free(ctx)

    return rand[:r_len]
