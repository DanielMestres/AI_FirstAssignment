import time
from array import *

M3x4 = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]
M4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

M3x3 = [[10,4,6],[6,3,25],[12,121,2]]
M3x5 = [[34,25,12,9,3],[1,2,3,4,5],[87,22,3,0,2]]



M7x9 = [[127, 139, -109, 64, -98, -35, 81, 136, -10],
    [146, 87, -117, -32, -12, -83, -109, -2, 118],
    [136, -67, 61, 113, 142, 32, -108, 108, -50],
    [-57, -101, 97, -66, -101, -99, 131, 118, -17],
    [-54, 132, 87, 96, 19, 27, 107, -70, -89],
    [34, -145, 130, -119, 96, -11, -31, -144, -149],
    [123, 44, -142, 136, 24, -137, -39, -84, 110]]

     
M9x9 = [[5, -76, -98, 147, -8, -19, 72, -55, -52],
    [-57, 3, 130, 48, -70, 32, 17, -150, 144],
    [58, -40, -69, 85, -42, -25, -84, 70, 45],
    [-113, -107, -45, -127, -57, -149, 27, 48, 70],
    [-60, 83, 117, 116, -64, 98, 97, 20, 55],
    [-138, 79, -33, -34, -92, 20, -26, -6, -120],
    [140, 136, -93, 128, 37, -46, -54, 146, -91],
    [-25, -150, 148, 58, -110, -17, 69, 131, -97],
    [-147, -102, 108, -24, -105, 15, -103, -121, -72]]



M10x12 = [[-53,  117,  -85,   80,   84,  141,  -15,   59,   78,   45,  111, -134],
    [-78, -135,   29,  -22, -111, -129,  -48,   11,  104,  -71,  -75,   74],
    [  2,   90,   43, -135,   14,  -39,  -79,   21,  129,  -11, -141, -129],
    [-33,  105,  117,   79,  -23, -100,  -26,   33,  -58,  137,   64,   56],
    [ 90,  134,  -89,  111,  101, -124, -119,   14, -110,  -18, -139,  139],
    [-95,   41,  128,  118,   62,   11,  100,  -63,  136,  -20,   50, -112],
    [ 50, -115,  -76,   56,  110,   44,   38,  -63,  146,  -18,   70,   29],
    [ -4, -102,  -10, -146, -102,   60,  -34,   76, -114,   94,   19,   27],
    [-76,  -27,  105,   56,  -61,  -30,  118,  -22,  139,   20, -142, -148],
    [ -7,  -83,   96,  118,   23,  142,  -70,   30,   11,  130,  -36, -148]]
     
M12x18 = [[67,  12,  51,  -9,  32, -98, -150,  67, -128,  38,  33, 124, -45,  28,  54,  34,  10,  74],
    [-39, -50, -29, -92, -35, -98, -107, 123, -38, -35, -70,  49, -14,  96,  61,  38,  62,  40],
    [-20, -73, -53, -64,  44, -31,  139, -139, -10,  77, -95,  32,  44, 138, -34, 130,  16,  40],
    [102, -73, -63, -148, 138,  53, -39, -146,  61,  59, -61,  13,  12,  51,  49,  17, 129, -25],
    [-19, 105, -34, -27, -110, -71, -92,  128, -129,  31,  59, -84, -50, -27, -128, -94, -39, -14],
    [-80, 144, -147, -39,  88, 140, -51,  140,  17,  17, -40,  102, -26, -97, -51, -44, -99, -26],
    [-118, -26, -22,  10, -94,  55,  27,   20, -80,  35,  30, -117, 102,  12, -21, -70,  -8,  72],
    [-24,  91, 138, -57,  29,  87, -12, -150, -123, -39, -59, 118, -20,  79, -39,  55, 118, -147],
    [119, -119,  80, 142,  36,  25, -49, -51, -97, -67, -145, 131, -107, -96, -21, 107, -141, -73],
    [-18,  73,  32, -92, -148, -12, -59, -22,  99, 142, -122,  30,  86, -42, -132,  59,  90, -94],
    [81,  -36,  49, -84, -15, -147, -67, -149, -89, -110,  98,  71,  11,  74,  76, -71,  41, -124],
    [-21, -26, -143, -140, 146,  55,  20,   79, -91, -36, -121, -42, -81, -131,  57, -23,  -9, 1]]



M20x5 = [[  22, -123, -127,  -60, -141],
    [ -31,   98,  -74,  -87,   69],
    [  55,  -74,  102,   21,  -95],
    [  15,  -89, -131,  144,   13],
    [ -17,  -52,   97,   57,  145],
    [ 149,  -97,  -67, -113, -107],
    [  16,   90, -144, -112,   10],
    [  21,   29,  -13,   56,   58],
    [  66,  -72, -143, -136,  -17],
    [  29,  -52, -112,  -39, -146],
    [ 131,  -36,   17,   67,   19],
    [  44,   36,  -49,   61, -111],
    [ -85,  -96,  -29,   47, -117],
    [  -5, -134,  105,   39,  -49],
    [ 149,  -68,  -20,   62,  -59],
    [  67,   85, -118, -145, -141],
    [ -36, -131,   15,  -77,   79],
    [ 102,  -28, -149,   -5, -111],
    [  32, -102,  101, -117,   39],
    [  24,   31,   43,  -11,  105]]

          
M5x12 = [[-140, 107, -56, -30, -61, 93, -27, -36, -32, 87, -102, -23],
    [106, 6, 93, 71, 31, 72, -120, -125, -93, -9, -122, -8],
    [-22, 129, -28, -92, -77, -22, 84, -121, 120, 57, 50, -51],
    [77, 14, -146, -103, -32, 64, -116, -25, 78, 117, -97, 128],
    [-49, -3, -44, -149, 143, -148, -32, -117, 85, -10, -80, -36]]


M10x128= [
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21],
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21]
]

M128x3=[
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19]
]

M3x196=[
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,1,1,1,1],
	
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,1,1,1,1],
	
	[12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,
	12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21, 12, 8, 32, 6, 9, 3, 1, 21,1,1,1,1]
	]

M196x3 =[
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
    [12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
    [12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
    [12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
    [12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
    [12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
    [12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
    [12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7], 	[1,2,3], 	[21,45,19], 	[5,6,7],	[11,3,2],
	[12,2,3], 	[8,3,13], 	[32,23,14], 	[6,45,2], 	[9,34,0], 	[3,45,7]
]

# [4x1][4x4]
r_a1 = len(M3x4)
c_a1 = len(M3x4[0])
r_a2 = len(M4x4)
c_a2 = len(M4x4[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M3x4[i][k] * M4x4[k][j]

    end_time = time.time()

    #print(result)
    print("Execution time[3x4][4x4]: ", end_time - start_time, " seconds")



# [3x3][3x5]
r_a1 = len(M3x3)
c_a1 = len(M3x3[0])
r_a2 = len(M3x5)
c_a2 = len(M3x5[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M3x3[i][k] * M3x5[k][j]

    end_time = time.time()


    #print(result)
    print("Execution time[3x3][3x5]: ", end_time - start_time, " seconds")



# [7x9][9x9]
r_a1 = len(M7x9)
c_a1 = len(M7x9[0])
r_a2 = len(M9x9)
c_a2 = len(M9x9[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M7x9[i][k] * M9x9[k][j]

    end_time = time.time()


    #print(result)
    print("Execution time[7x9][9x9]: ", end_time - start_time, " seconds")



# [10x12][12x18]
r_a1 = len(M10x12)
c_a1 = len(M10x12[0])
r_a2 = len(M12x18)
c_a2 = len(M12x18[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M10x12[i][k] * M12x18[k][j]

    end_time = time.time()


    #print(result)
    print("Execution time[10x12][12x18]: ", end_time - start_time, " seconds")


# [20x5][5x12]
r_a1 = len(M20x5)
c_a1 = len(M20x5[0])
r_a2 = len(M5x12)
c_a2 = len(M5x12[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M20x5[i][k] * M5x12[k][j]

    end_time = time.time()


    #print(result)
    print("Execution time[20x5][5x12]: ", end_time - start_time, " seconds")


#   [10x128][128x3]
r_a1 = len(M10x128)
c_a1 = len(M10x128[0])
r_a2 = len(M128x3)
c_a2 = len(M128x3[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M10x128[i][k] * M128x3[k][j]

    end_time = time.time()


    #print(result)
    print("Execution time[10x128][128x3]: ", end_time - start_time, " seconds")


# [3x196][196x3]
r_a1 = len(M3x196)
c_a1 = len(M3x196[0])
r_a2 = len(M196x3)
c_a2 = len(M196x3[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M3x196[i][k] * M196x3[k][j]

    end_time = time.time()


    #print(result)
    print("Execution time[3x196][196x3]: ", end_time - start_time, " seconds")




#   [128x3][3x196]
r_a1 = len(M128x3)
c_a1 = len(M128x3[0])
r_a2 = len(M3x196)
c_a2 = len(M3x196[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += M128x3[i][k] * M3x196[k][j]

    end_time = time.time()


    #print(result)
    print("Execution time[128x3][3x196]: ", end_time - start_time, " seconds")