# Copyright (c) 1990, 1993
#   The Regents of the University of California.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 4. Neither the name of the University nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
#
# This is a derivative from the FreeBSD C Library:
# - stdlib/rand.c
# It was rewritten for Python by Jayson Fong, 2025.
#
# Original sources that this file was based on is available at:
#   https://github.com/apple-oss-distributions/Libc/blob/bf35f81f8e712c9640fb1b0aed280b1b9c752aaf/stdlib/FreeBSD/rand.c
#
# Sources that this file was validated against are available at:
#   https://github.com/freebsd/freebsd-src/blob/47227ef0ef663b7abb81ab5a60a450da9a93d24b/lib/libc/stdlib/rand.c


from typing import Tuple

from .....definitions import Seed

GLOBAL_STATE: Seed = Seed(1)


def do_rand(state: int = 1) -> Tuple[int, int]:
    hi = state // 127773
    lo = state % 127773
    x = 16807 * lo - 2836 * hi

    if x < 0:
        x += 0x7FFFFFFF

    state = x
    return state % 2147483648, state


def rand() -> int:
    result, next_seed = do_rand(GLOBAL_STATE.value)
    GLOBAL_STATE.value = next_seed

    return result


def srand(state: int = 0):
    GLOBAL_STATE.value = state


__all__: Tuple[str, ...] = ("do_rand", "rand", "srand")
