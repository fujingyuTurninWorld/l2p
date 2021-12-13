# coding=utf-8
# Copyright 2020 The Learning-to-Prompt Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific Learning-to-Prompt governing permissions and
# limitations under the License.
# ==============================================================================
"""Constant dicts for class statistics."""


def get_number_filtered_examples(dataset, subclasses):
  """Get class stats for the filtered classes."""
  num = [0, 0]
  if dataset.startswith('cifar'):
    phases = ['train', 'test']
  elif dataset.startswith('imagenet'):
    phases = ['train', 'validation']
  else:
    raise NotImplementedError(f'{dataset} does not exist.')
  for i, phase in enumerate(phases):
    for class_label in subclasses:
      num[i] += CLASS_STATS[dataset][phase][class_label]
  return num


CLASS_STATS = {}
CLASS_STATS['cifar10'] = {
    'train': {x: 5000 for x in range(10)},
    'test': {x: 1000 for x in range(10)}
}

CLASS_STATS['cifar100'] = {
    'train': {x: 500 for x in range(100)},
    'test': {x: 100 for x in range(100)}
}

CLASS_STATS['imagenet2012'] = {
    'train': {
        0: 1300,
        1: 1300,
        2: 1300,
        3: 1300,
        4: 1300,
        5: 1300,
        6: 1300,
        7: 1300,
        8: 1300,
        9: 1300,
        10: 1300,
        11: 1300,
        12: 1300,
        13: 1300,
        14: 1300,
        15: 1300,
        16: 1300,
        17: 1300,
        18: 1300,
        19: 1300,
        20: 1300,
        21: 1300,
        22: 1300,
        23: 1300,
        24: 1300,
        25: 1300,
        26: 1300,
        27: 1300,
        28: 1300,
        29: 1300,
        30: 1300,
        31: 1300,
        32: 1300,
        33: 1300,
        34: 1300,
        35: 1300,
        36: 1300,
        37: 1300,
        38: 1300,
        39: 1300,
        40: 1300,
        41: 1300,
        42: 1300,
        43: 1117,
        44: 1300,
        45: 1300,
        46: 1300,
        47: 1300,
        48: 1300,
        49: 1300,
        50: 1300,
        51: 1266,
        52: 1300,
        53: 1300,
        54: 1300,
        55: 1300,
        56: 1300,
        57: 1300,
        58: 1300,
        59: 1300,
        60: 1300,
        61: 1300,
        62: 1071,
        63: 1300,
        64: 1300,
        65: 1300,
        66: 1300,
        67: 1300,
        68: 1300,
        69: 1300,
        70: 1300,
        71: 1300,
        72: 1300,
        73: 1300,
        74: 1300,
        75: 1300,
        76: 1300,
        77: 1300,
        78: 1300,
        79: 1300,
        80: 1300,
        81: 1300,
        82: 1300,
        83: 1300,
        84: 1300,
        85: 1300,
        86: 1300,
        87: 1300,
        88: 1300,
        89: 1300,
        90: 1300,
        91: 1300,
        92: 1300,
        93: 1300,
        94: 1300,
        95: 1300,
        96: 1300,
        97: 1300,
        98: 1141,
        99: 1300,
        100: 1300,
        101: 1300,
        102: 1300,
        103: 1272,
        104: 1300,
        105: 1300,
        106: 1300,
        107: 1300,
        108: 1300,
        109: 1300,
        110: 1300,
        111: 1300,
        112: 1300,
        113: 1300,
        114: 1300,
        115: 1300,
        116: 1300,
        117: 1300,
        118: 1300,
        119: 1300,
        120: 1300,
        121: 1300,
        122: 1300,
        123: 1300,
        124: 1300,
        125: 1300,
        126: 1300,
        127: 1300,
        128: 1300,
        129: 1300,
        130: 1300,
        131: 1300,
        132: 1300,
        133: 1300,
        134: 1300,
        135: 1300,
        136: 1300,
        137: 1300,
        138: 1300,
        139: 1300,
        140: 1300,
        141: 1300,
        142: 1300,
        143: 1300,
        144: 1300,
        145: 1300,
        146: 1300,
        147: 1150,
        148: 1300,
        149: 1300,
        150: 1300,
        151: 1300,
        152: 772,
        153: 1300,
        154: 1300,
        155: 1300,
        156: 1300,
        157: 1300,
        158: 860,
        159: 1300,
        160: 1300,
        161: 1300,
        162: 1300,
        163: 1300,
        164: 1136,
        165: 732,
        166: 1025,
        167: 754,
        168: 1290,
        169: 1300,
        170: 1300,
        171: 1300,
        172: 1300,
        173: 1300,
        174: 1300,
        175: 738,
        176: 1300,
        177: 1300,
        178: 1300,
        179: 1300,
        180: 1300,
        181: 1258,
        182: 1300,
        183: 1273,
        184: 1300,
        185: 1300,
        186: 1300,
        187: 1300,
        188: 977,
        189: 1300,
        190: 936,
        191: 1300,
        192: 1300,
        193: 1300,
        194: 1156,
        195: 1300,
        196: 1300,
        197: 1300,
        198: 1300,
        199: 1300,
        200: 1300,
        201: 1300,
        202: 1300,
        203: 1300,
        204: 1300,
        205: 1300,
        206: 1218,
        207: 1300,
        208: 1300,
        209: 1300,
        210: 1300,
        211: 1300,
        212: 1300,
        213: 1300,
        214: 1300,
        215: 1300,
        216: 1300,
        217: 1300,
        218: 1300,
        219: 1300,
        220: 1300,
        221: 969,
        222: 1300,
        223: 1300,
        224: 1300,
        225: 1300,
        226: 1300,
        227: 1300,
        228: 1300,
        229: 1300,
        230: 1300,
        231: 1300,
        232: 1300,
        233: 1300,
        234: 1300,
        235: 1300,
        236: 1300,
        237: 1300,
        238: 1300,
        239: 1300,
        240: 1300,
        241: 1300,
        242: 1300,
        243: 1300,
        244: 1300,
        245: 1300,
        246: 1300,
        247: 1300,
        248: 1300,
        249: 1300,
        250: 1300,
        251: 1300,
        252: 954,
        253: 1300,
        254: 1300,
        255: 1300,
        256: 1300,
        257: 1300,
        258: 1300,
        259: 1300,
        260: 1300,
        261: 1300,
        262: 1070,
        263: 1300,
        264: 1300,
        265: 1300,
        266: 1300,
        267: 1300,
        268: 755,
        269: 1300,
        270: 1300,
        271: 1300,
        272: 1300,
        273: 1300,
        274: 1300,
        275: 1300,
        276: 1300,
        277: 1300,
        278: 1300,
        279: 1300,
        280: 1300,
        281: 1300,
        282: 1300,
        283: 1300,
        284: 1300,
        285: 1300,
        286: 1300,
        287: 1300,
        288: 1300,
        289: 1300,
        290: 1300,
        291: 1300,
        292: 1300,
        293: 1300,
        294: 1300,
        295: 1300,
        296: 1300,
        297: 1300,
        298: 1300,
        299: 1300,
        300: 1300,
        301: 1300,
        302: 1300,
        303: 1300,
        304: 1300,
        305: 1300,
        306: 1300,
        307: 1300,
        308: 1300,
        309: 1300,
        310: 1300,
        311: 1300,
        312: 1300,
        313: 1300,
        314: 1300,
        315: 1300,
        316: 1300,
        317: 1300,
        318: 1300,
        319: 1300,
        320: 1300,
        321: 1300,
        322: 1300,
        323: 1300,
        324: 1300,
        325: 1300,
        326: 1300,
        327: 1300,
        328: 1300,
        329: 1300,
        330: 1300,
        331: 1300,
        332: 1300,
        333: 1300,
        334: 1300,
        335: 1206,
        336: 1300,
        337: 1300,
        338: 1300,
        339: 1300,
        340: 1300,
        341: 1300,
        342: 1300,
        343: 1300,
        344: 1300,
        345: 1300,
        346: 1300,
        347: 1300,
        348: 1300,
        349: 1300,
        350: 1300,
        351: 1300,
        352: 1300,
        353: 1300,
        354: 1300,
        355: 1300,
        356: 1300,
        357: 1300,
        358: 1300,
        359: 1300,
        360: 1300,
        361: 1300,
        362: 1300,
        363: 1300,
        364: 1300,
        365: 1300,
        366: 1300,
        367: 1300,
        368: 1300,
        369: 1300,
        370: 1300,
        371: 1300,
        372: 1300,
        373: 1300,
        374: 1300,
        375: 1300,
        376: 1300,
        377: 1300,
        378: 1300,
        379: 1300,
        380: 1300,
        381: 1300,
        382: 1300,
        383: 1300,
        384: 1300,
        385: 1300,
        386: 1300,
        387: 1300,
        388: 1300,
        389: 1300,
        390: 1165,
        391: 1300,
        392: 969,
        393: 1300,
        394: 1300,
        395: 1300,
        396: 1300,
        397: 1300,
        398: 1300,
        399: 1300,
        400: 1300,
        401: 1300,
        402: 1300,
        403: 1300,
        404: 1300,
        405: 1300,
        406: 1300,
        407: 1300,
        408: 1300,
        409: 1292,
        410: 1300,
        411: 1300,
        412: 1300,
        413: 1300,
        414: 1300,
        415: 1300,
        416: 1300,
        417: 1300,
        418: 1236,
        419: 1300,
        420: 1300,
        421: 1300,
        422: 1300,
        423: 1300,
        424: 1300,
        425: 1300,
        426: 1199,
        427: 1300,
        428: 1300,
        429: 1300,
        430: 1300,
        431: 1300,
        432: 1300,
        433: 1300,
        434: 1300,
        435: 1300,
        436: 1300,
        437: 1300,
        438: 1300,
        439: 1209,
        440: 1300,
        441: 1300,
        442: 1300,
        443: 1300,
        444: 1300,
        445: 1300,
        446: 1300,
        447: 1300,
        448: 1300,
        449: 1300,
        450: 1300,
        451: 1300,
        452: 1300,
        453: 1300,
        454: 1300,
        455: 1300,
        456: 1300,
        457: 1300,
        458: 1300,
        459: 1300,
        460: 1300,
        461: 1300,
        462: 1300,
        463: 1300,
        464: 1300,
        465: 1176,
        466: 1300,
        467: 1300,
        468: 1300,
        469: 1300,
        470: 1300,
        471: 1300,
        472: 1300,
        473: 1300,
        474: 1300,
        475: 1300,
        476: 1300,
        477: 1300,
        478: 1300,
        479: 1300,
        480: 1300,
        481: 1186,
        482: 1300,
        483: 1300,
        484: 1300,
        485: 1300,
        486: 1300,
        487: 1300,
        488: 1300,
        489: 1300,
        490: 1300,
        491: 1194,
        492: 1300,
        493: 1300,
        494: 1300,
        495: 1300,
        496: 1300,
        497: 1300,
        498: 1300,
        499: 1067,
        500: 1300,
        501: 1029,
        502: 1300,
        503: 1154,
        504: 1300,
        505: 1300,
        506: 1300,
        507: 1216,
        508: 1300,
        509: 1300,
        510: 1300,
        511: 1300,
        512: 1300,
        513: 1300,
        514: 1300,
        515: 1300,
        516: 1300,
        517: 1300,
        518: 1300,
        519: 1300,
        520: 1300,
        521: 1187,
        522: 1300,
        523: 1300,
        524: 1300,
        525: 1300,
        526: 1300,
        527: 1300,
        528: 1300,
        529: 1300,
        530: 1300,
        531: 889,
        532: 1300,
        533: 1300,
        534: 1300,
        535: 1300,
        536: 1211,
        537: 1300,
        538: 1300,
        539: 1300,
        540: 1300,
        541: 1300,
        542: 1300,
        543: 1300,
        544: 1300,
        545: 1300,
        546: 1300,
        547: 1300,
        548: 1300,
        549: 1300,
        550: 1136,
        551: 1153,
        552: 1300,
        553: 1300,
        554: 1300,
        555: 1300,
        556: 1300,
        557: 1300,
        558: 1300,
        559: 1300,
        560: 1300,
        561: 1300,
        562: 1300,
        563: 1300,
        564: 1300,
        565: 1300,
        566: 1300,
        567: 1222,
        568: 1300,
        569: 1300,
        570: 1300,
        571: 1300,
        572: 1300,
        573: 1300,
        574: 1300,
        575: 1300,
        576: 1300,
        577: 1282,
        578: 1300,
        579: 1300,
        580: 1300,
        581: 1300,
        582: 1300,
        583: 1283,
        584: 1300,
        585: 980,
        586: 1300,
        587: 1300,
        588: 1300,
        589: 1300,
        590: 1034,
        591: 1300,
        592: 1300,
        593: 1300,
        594: 1300,
        595: 1300,
        596: 891,
        597: 1300,
        598: 1300,
        599: 1300,
        600: 1300,
        601: 1300,
        602: 1300,
        603: 1300,
        604: 1300,
        605: 1300,
        606: 1300,
        607: 1300,
        608: 1300,
        609: 1300,
        610: 1285,
        611: 1300,
        612: 1300,
        613: 1300,
        614: 1300,
        615: 1300,
        616: 1300,
        617: 1300,
        618: 1300,
        619: 1300,
        620: 1300,
        621: 1300,
        622: 1300,
        623: 986,
        624: 1300,
        625: 1300,
        626: 1300,
        627: 1300,
        628: 1300,
        629: 1300,
        630: 1137,
        631: 1272,
        632: 1300,
        633: 1300,
        634: 1300,
        635: 1155,
        636: 1300,
        637: 1300,
        638: 1300,
        639: 1300,
        640: 1300,
        641: 1300,
        642: 1300,
        643: 1300,
        644: 1300,
        645: 1300,
        646: 1300,
        647: 1300,
        648: 1300,
        649: 1300,
        650: 1300,
        651: 1300,
        652: 1300,
        653: 1097,
        654: 1300,
        655: 1300,
        656: 1300,
        657: 1300,
        658: 1300,
        659: 1300,
        660: 1300,
        661: 1300,
        662: 1149,
        663: 1155,
        664: 1300,
        665: 1300,
        666: 1300,
        667: 1300,
        668: 1300,
        669: 1300,
        670: 1300,
        671: 1300,
        672: 1300,
        673: 1300,
        674: 1300,
        675: 1159,
        676: 1133,
        677: 1300,
        678: 1180,
        679: 1300,
        680: 1300,
        681: 1300,
        682: 1300,
        683: 1300,
        684: 1300,
        685: 1300,
        686: 1120,
        687: 1300,
        688: 1300,
        689: 1005,
        690: 1300,
        691: 1300,
        692: 1300,
        693: 1300,
        694: 1300,
        695: 1300,
        696: 1300,
        697: 1300,
        698: 1300,
        699: 1300,
        700: 1300,
        701: 1300,
        702: 1300,
        703: 1300,
        704: 1300,
        705: 1300,
        706: 1152,
        707: 1300,
        708: 1156,
        709: 1300,
        710: 1300,
        711: 1300,
        712: 962,
        713: 1300,
        714: 1157,
        715: 1300,
        716: 1300,
        717: 1300,
        718: 1300,
        719: 1300,
        720: 1300,
        721: 1300,
        722: 1282,
        723: 1117,
        724: 1118,
        725: 1300,
        726: 1300,
        727: 1270,
        728: 1069,
        729: 1053,
        730: 1300,
        731: 1254,
        732: 1300,
        733: 1300,
        734: 1300,
        735: 1300,
        736: 1300,
        737: 1300,
        738: 1300,
        739: 1300,
        740: 908,
        741: 1300,
        742: 1300,
        743: 1300,
        744: 1300,
        745: 1300,
        746: 1300,
        747: 1247,
        748: 1300,
        749: 1300,
        750: 1300,
        751: 1300,
        752: 1300,
        753: 1253,
        754: 1300,
        755: 1300,
        756: 1300,
        757: 1300,
        758: 1300,
        759: 1300,
        760: 1300,
        761: 1300,
        762: 1300,
        763: 1300,
        764: 1300,
        765: 1300,
        766: 1300,
        767: 1300,
        768: 1300,
        769: 1300,
        770: 1300,
        771: 1029,
        772: 1259,
        773: 1300,
        774: 1300,
        775: 1300,
        776: 1300,
        777: 1300,
        778: 1300,
        779: 1300,
        780: 1300,
        781: 1300,
        782: 1267,
        783: 1300,
        784: 1300,
        785: 1300,
        786: 1300,
        787: 1300,
        788: 1300,
        789: 1249,
        790: 1300,
        791: 1300,
        792: 1300,
        793: 1300,
        794: 1300,
        795: 1300,
        796: 1300,
        797: 1300,
        798: 1162,
        799: 1300,
        800: 1300,
        801: 1300,
        802: 1300,
        803: 1300,
        804: 1300,
        805: 1300,
        806: 1300,
        807: 1300,
        808: 1300,
        809: 1300,
        810: 1045,
        811: 1004,
        812: 1238,
        813: 1300,
        814: 1300,
        815: 1300,
        816: 1300,
        817: 1300,
        818: 1300,
        819: 1300,
        820: 1300,
        821: 1153,
        822: 1300,
        823: 1300,
        824: 1300,
        825: 1300,
        826: 1084,
        827: 1300,
        828: 1300,
        829: 1300,
        830: 1300,
        831: 1300,
        832: 1300,
        833: 1300,
        834: 1300,
        835: 1300,
        836: 1300,
        837: 1300,
        838: 1217,
        839: 1300,
        840: 1300,
        841: 931,
        842: 1300,
        843: 1300,
        844: 1300,
        845: 1300,
        846: 1300,
        847: 1300,
        848: 1300,
        849: 1300,
        850: 1300,
        851: 1300,
        852: 1300,
        853: 1300,
        854: 1264,
        855: 1300,
        856: 1300,
        857: 976,
        858: 1300,
        859: 1300,
        860: 1250,
        861: 1300,
        862: 1300,
        863: 1300,
        864: 1300,
        865: 1300,
        866: 1300,
        867: 1300,
        868: 1300,
        869: 1053,
        870: 1300,
        871: 1300,
        872: 1160,
        873: 1300,
        874: 1300,
        875: 1300,
        876: 1300,
        877: 1300,
        878: 1300,
        879: 1300,
        880: 1300,
        881: 1300,
        882: 1300,
        883: 1300,
        884: 1300,
        885: 1062,
        886: 1300,
        887: 1300,
        888: 1300,
        889: 1300,
        890: 1300,
        891: 1137,
        892: 1299,
        893: 1300,
        894: 1300,
        895: 1300,
        896: 1300,
        897: 1300,
        898: 1300,
        899: 1300,
        900: 1300,
        901: 1055,
        902: 1300,
        903: 1300,
        904: 1300,
        905: 1300,
        906: 1213,
        907: 1300,
        908: 1300,
        909: 1300,
        910: 1300,
        911: 1300,
        912: 1300,
        913: 1300,
        914: 1206,
        915: 1300,
        916: 1300,
        917: 1300,
        918: 1300,
        919: 1300,
        920: 1300,
        921: 1154,
        922: 1300,
        923: 1300,
        924: 1300,
        925: 1207,
        926: 1149,
        927: 1300,
        928: 1300,
        929: 1300,
        930: 1300,
        931: 1300,
        932: 1300,
        933: 1300,
        934: 1300,
        935: 1300,
        936: 1300,
        937: 1300,
        938: 1300,
        939: 1300,
        940: 1239,
        941: 1300,
        942: 1300,
        943: 1300,
        944: 1300,
        945: 1300,
        946: 1125,
        947: 1300,
        948: 1300,
        949: 1300,
        950: 1300,
        951: 1300,
        952: 1300,
        953: 1300,
        954: 1300,
        955: 1300,
        956: 1300,
        957: 1300,
        958: 1300,
        959: 1300,
        960: 1300,
        961: 1300,
        962: 1300,
        963: 1300,
        964: 1300,
        965: 1300,
        966: 1300,
        967: 1300,
        968: 1300,
        969: 1193,
        970: 1300,
        971: 1300,
        972: 1300,
        973: 1300,
        974: 1300,
        975: 1300,
        976: 1300,
        977: 1300,
        978: 1300,
        979: 1300,
        980: 1300,
        981: 1300,
        982: 1300,
        983: 1300,
        984: 1300,
        985: 1300,
        986: 1300,
        987: 1300,
        988: 1300,
        989: 1300,
        990: 1300,
        991: 1300,
        992: 1300,
        993: 1300,
        994: 1300,
        995: 1300,
        996: 1300,
        997: 1300,
        998: 1300,
        999: 1300
    },
    'validation': {x: 50 for x in range(1000)}
}