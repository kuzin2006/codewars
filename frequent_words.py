# https://www.codewars.com/kata/most-frequently-used-words-in-a-text/train/python
import re


def top_3_words(text):
    words = [word.lower() for word in re.findall(r"'?[A-Za-z]+'?[A-Za-z]*", text)]
    words_count = {}
    for word in words:
        try:
            words_count[word] += 1
        except KeyError:
            words_count[word] = 1
    top_3 = sorted(words_count.items(), key=lambda i: i[1], reverse=True)[:3]
    return [i[0] for i in top_3]


print(top_3_words("CYrW//- :IGFxR.!; ssCHGLhuGN;, XemtAf-?dYHKsN,-!.;ssCHGLhuGN.,?::ssCHGLhuGN?./.dYHKsN??_:.dYHKsN?!wVIwB -ssCHGLhuGN_gxe'WYYi'??,..ssCHGLhuGN;?-,gxe'WYYi'. /.,wVIwB,,dYHKsN._ _;XemtAf!;--IGFxR?,. XemtAf_;ssCHGLhuGN_,XemtAf/?-;wVIwB/;!/ssCHGLhuGN!_IGFxR?_CYrW,-gxe'WYYi'._!!dYHKsN,_?.ssCHGLhuGN,!,; ssCHGLhuGN __-,gxe'WYYi', ??!XemtAf,ssCHGLhuGN,: ?IGFxR?.XemtAf;?,ssCHGLhuGN?IGFxR!,/gxe'WYYi'?,:/XemtAf_-!.!dYHKsN:gxe'WYYi';XemtAf/XemtAf/ .,wVIwB/ssCHGLhuGN?;_CYrW!XemtAf - /,wVIwB!,gxe'WYYi'-: :gxe'WYYi'-;;ssCHGLhuGN ?ssCHGLhuGN,gxe'WYYi'./;?XemtAf! gxe'WYYi'?/ CYrW;dYHKsN XemtAf:gxe'WYYi'.-._:dYHKsN,.gxe'WYYi'/IGFxR,/, :gxe'WYYi'_ .:dYHKsN-;dYHKsN!/gxe'WYYi'  XemtAf_!?/ CYrW-.- ssCHGLhuGN?-:;ssCHGLhuGN/.:!-IGFxR.!:.gxe'WYYi'!!,gzLcf!-_/;XemtAf_XemtAf.:__ wVIwB;gxe'WYYi'_?;:XemtAf ;ssCHGLhuGN,/dYHKsN/,dYHKsN_ ./XemtAf.!;-;IGFxR!gxe'WYYi'_/,?,dYHKsN_-,::gxe'WYYi'/?_gxe'WYYi'.:XemtAf;!?CYrW!.dYHKsN!  /wVIwB:dYHKsN;!,!gxe'WYYi',?;?:ssCHGLhuGN;./gxe'WYYi'.!wVIwB:-_/?IGFxR; _ CYrW //_!ssCHGLhuGN;,//XemtAf?-;-XemtAf/_;XemtAf?_dYHKsN;ssCHGLhuGN:/dYHKsN//!-:gxe'WYYi'.;,_/dYHKsN_?ssCHGLhuGN CYrW-.?-;XemtAf!??.ssCHGLhuGN,__!XemtAf!__!XemtAf??,ssCHGLhuGN _gxe'WYYi'  -/?gxe'WYYi'?/ _wVIwB  XemtAf_!-gxe'WYYi'/-/!,gxe'WYYi';XemtAf/,._gxe'WYYi' -:.!XemtAf ssCHGLhuGN;??ssCHGLhuGN /!-XemtAf:-gxe'WYYi';ssCHGLhuGN?;"))
