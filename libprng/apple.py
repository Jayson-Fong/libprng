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
#   https://github.com/apple-oss-distributions/Libc/blob/Libc-1353.11.2/stdlib/FreeBSD/rand.c


"""
Pseudo-random number generator for macOS.

This version of the algorithm was verified against macOS 15.6.1.
While the FreeBSD implementation has since been updated, the
version used on macOS has not yet been updated to match at time
of writing.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(slots=True)
class Seed:
    value: int


GLOBAL_STATE: Seed = Seed(123459876)


def do_rand(state: int = 123459876) -> Tuple[int, int]:
    if state == 0:
        state = 123459876

    hi = state // 127773
    lo = state % 127773
    x = 16807 * lo - 2836 * hi

    if x < 0:
        x += 0x7fffffff

    state = x
    return state % 2147483648, state


def rand() -> int:
    result, next_seed = do_rand(GLOBAL_STATE.value)
    GLOBAL_STATE.value = next_seed

    return result


def srand(state: int = 0):
    GLOBAL_STATE.value = state


__all__: Tuple[str, ...] = ("rand", "srand")
