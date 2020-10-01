# Generated from ./Expr.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u015f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\6\2")
        buf.write("<\n\2\r\2\16\2=\3\2\3\2\3\3\3\3\5\3D\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4T\n\4\3")
        buf.write("\5\3\5\3\5\7\5Y\n\5\f\5\16\5\\\13\5\5\5^\n\5\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\7\7h\n\7\f\7\16\7k\13\7\3\b\3\b")
        buf.write("\7\bo\n\b\f\b\16\br\13\b\3\b\3\b\3\t\3\t\5\tx\n\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u008a\n\n\3\n\3\n\3\n\5\n\u008f\n\n\3\n\3\n")
        buf.write("\5\n\u0093\n\n\3\n\3\n\5\n\u0097\n\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u009f\n\n\3\n\3\n\5\n\u00a3\n\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u00ba\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\7\13\u00c1\n\13\f\13\16\13\u00c4\13\13\3\13\3\13\5")
        buf.write("\13\u00c8\n\13\3\13\3\13\3\f\3\f\3\f\7\f\u00cf\n\f\f\f")
        buf.write("\16\f\u00d2\13\f\5\f\u00d4\n\f\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00dd\n\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u00e6\n\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\7\20\u00ee\n\20\f\20\16\20\u00f1\13\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u00f9\n\21\f\21\16\21\u00fc\13\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u0105\n\22\f")
        buf.write("\22\16\22\u0108\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u0111\n\23\f\23\16\23\u0114\13\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u011d\n\24\f\24\16\24\u0120")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0129\n")
        buf.write("\25\f\25\16\25\u012c\13\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u0138\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0141\n\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u0148\n\27\f\27\16\27\u014b\13\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u0153\n\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\2\n\f\36 \"$")
        buf.write("&(,\36\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668\2\7\4\2\3\3\22\25\4\2\22\22\26\26\4\2\3")
        buf.write("\3\27\30\3\2\31\32\3\2\33\36\2\u016c\2;\3\2\2\2\4C\3\2")
        buf.write("\2\2\6S\3\2\2\2\b]\3\2\2\2\n_\3\2\2\2\fb\3\2\2\2\16l\3")
        buf.write("\2\2\2\20w\3\2\2\2\22\u00b9\3\2\2\2\24\u00bb\3\2\2\2\26")
        buf.write("\u00d3\3\2\2\2\30\u00d5\3\2\2\2\32\u00dc\3\2\2\2\34\u00e5")
        buf.write("\3\2\2\2\36\u00e7\3\2\2\2 \u00f2\3\2\2\2\"\u00fd\3\2\2")
        buf.write("\2$\u0109\3\2\2\2&\u0115\3\2\2\2(\u0121\3\2\2\2*\u0137")
        buf.write("\3\2\2\2,\u0140\3\2\2\2.\u0152\3\2\2\2\60\u0154\3\2\2")
        buf.write("\2\62\u0156\3\2\2\2\64\u0158\3\2\2\2\66\u015a\3\2\2\2")
        buf.write("8\u015c\3\2\2\2:<\5\4\3\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2")
        buf.write("\2=>\3\2\2\2>?\3\2\2\2?@\7\2\2\3@\3\3\2\2\2AD\5\6\4\2")
        buf.write("BD\5\24\13\2CA\3\2\2\2CB\3\2\2\2D\5\3\2\2\2EF\5\f\7\2")
        buf.write("FG\7*\2\2GH\7!\2\2HI\5\b\5\2IJ\7\"\2\2JK\5\16\b\2KT\3")
        buf.write("\2\2\2LM\5\f\7\2MN\7*\2\2NO\7!\2\2OP\5\b\5\2PQ\7\"\2\2")
        buf.write("QR\7&\2\2RT\3\2\2\2SE\3\2\2\2SL\3\2\2\2T\7\3\2\2\2UZ\5")
        buf.write("\n\6\2VW\7%\2\2WY\5\n\6\2XV\3\2\2\2Y\\\3\2\2\2ZX\3\2\2")
        buf.write("\2Z[\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2]U\3\2\2\2]^\3\2\2\2")
        buf.write("^\t\3\2\2\2_`\5\f\7\2`a\7*\2\2a\13\3\2\2\2bc\b\7\1\2c")
        buf.write("d\7\37\2\2di\3\2\2\2ef\f\3\2\2fh\7\3\2\2ge\3\2\2\2hk\3")
        buf.write("\2\2\2ig\3\2\2\2ij\3\2\2\2j\r\3\2\2\2ki\3\2\2\2lp\7#\2")
        buf.write("\2mo\5\20\t\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2")
        buf.write("qs\3\2\2\2rp\3\2\2\2st\7$\2\2t\17\3\2\2\2ux\5\22\n\2v")
        buf.write("x\5\24\13\2wu\3\2\2\2wv\3\2\2\2x\21\3\2\2\2yz\7 \2\2z")
        buf.write("{\5\30\r\2{|\7&\2\2|\u00ba\3\2\2\2}~\5\30\r\2~\177\7&")
        buf.write("\2\2\177\u00ba\3\2\2\2\u0080\u00ba\7&\2\2\u0081\u00ba")
        buf.write("\5\16\b\2\u0082\u0083\7\4\2\2\u0083\u0084\7!\2\2\u0084")
        buf.write("\u0085\5\30\r\2\u0085\u0086\7\"\2\2\u0086\u0089\5\22\n")
        buf.write("\2\u0087\u0088\7\5\2\2\u0088\u008a\5\22\n\2\u0089\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u00ba\3\2\2\2\u008b")
        buf.write("\u008c\7\6\2\2\u008c\u008e\7!\2\2\u008d\u008f\5\30\r\2")
        buf.write("\u008e\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\3")
        buf.write("\2\2\2\u0090\u0092\7&\2\2\u0091\u0093\5\30\r\2\u0092\u0091")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0096\7&\2\2\u0095\u0097\5\30\r\2\u0096\u0095\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\7")
        buf.write("\"\2\2\u0099\u00ba\5\22\n\2\u009a\u009b\7\6\2\2\u009b")
        buf.write("\u009c\7!\2\2\u009c\u009e\5\24\13\2\u009d\u009f\5\30\r")
        buf.write("\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a2\7&\2\2\u00a1\u00a3\5\30\r\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a5\7\"\2\2\u00a5\u00a6\5\22\n\2\u00a6\u00ba")
        buf.write("\3\2\2\2\u00a7\u00a8\7\7\2\2\u00a8\u00a9\7!\2\2\u00a9")
        buf.write("\u00aa\5\30\r\2\u00aa\u00ab\7\"\2\2\u00ab\u00ac\5\22\n")
        buf.write("\2\u00ac\u00ba\3\2\2\2\u00ad\u00ae\7\b\2\2\u00ae\u00af")
        buf.write("\5\22\n\2\u00af\u00b0\7\7\2\2\u00b0\u00b1\7!\2\2\u00b1")
        buf.write("\u00b2\5\30\r\2\u00b2\u00b3\7\"\2\2\u00b3\u00b4\7&\2\2")
        buf.write("\u00b4\u00ba\3\2\2\2\u00b5\u00b6\7\t\2\2\u00b6\u00ba\7")
        buf.write("&\2\2\u00b7\u00b8\7\n\2\2\u00b8\u00ba\7&\2\2\u00b9y\3")
        buf.write("\2\2\2\u00b9}\3\2\2\2\u00b9\u0080\3\2\2\2\u00b9\u0081")
        buf.write("\3\2\2\2\u00b9\u0082\3\2\2\2\u00b9\u008b\3\2\2\2\u00b9")
        buf.write("\u009a\3\2\2\2\u00b9\u00a7\3\2\2\2\u00b9\u00ad\3\2\2\2")
        buf.write("\u00b9\u00b5\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\23\3\2")
        buf.write("\2\2\u00bb\u00bc\5\f\7\2\u00bc\u00c2\7*\2\2\u00bd\u00be")
        buf.write("\7\13\2\2\u00be\u00bf\7)\2\2\u00bf\u00c1\7\f\2\2\u00c0")
        buf.write("\u00bd\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c5\u00c6\7\r\2\2\u00c6\u00c8\5\30\r\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00ca\7&\2\2\u00ca\25\3\2\2\2\u00cb\u00d0\5\30")
        buf.write("\r\2\u00cc\u00cd\7%\2\2\u00cd\u00cf\5\30\r\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d3\u00cb\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\27\3\2")
        buf.write("\2\2\u00d5\u00d6\5\32\16\2\u00d6\31\3\2\2\2\u00d7\u00dd")
        buf.write("\5\34\17\2\u00d8\u00d9\5*\26\2\u00d9\u00da\7\r\2\2\u00da")
        buf.write("\u00db\5\30\r\2\u00db\u00dd\3\2\2\2\u00dc\u00d7\3\2\2")
        buf.write("\2\u00dc\u00d8\3\2\2\2\u00dd\33\3\2\2\2\u00de\u00e6\5")
        buf.write("\36\20\2\u00df\u00e0\5\36\20\2\u00e0\u00e1\7\16\2\2\u00e1")
        buf.write("\u00e2\5\30\r\2\u00e2\u00e3\7\17\2\2\u00e3\u00e4\5\34")
        buf.write("\17\2\u00e4\u00e6\3\2\2\2\u00e5\u00de\3\2\2\2\u00e5\u00df")
        buf.write("\3\2\2\2\u00e6\35\3\2\2\2\u00e7\u00e8\b\20\1\2\u00e8\u00e9")
        buf.write("\5 \21\2\u00e9\u00ef\3\2\2\2\u00ea\u00eb\f\3\2\2\u00eb")
        buf.write("\u00ec\7\20\2\2\u00ec\u00ee\5 \21\2\u00ed\u00ea\3\2\2")
        buf.write("\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0\37\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3")
        buf.write("\b\21\1\2\u00f3\u00f4\5\"\22\2\u00f4\u00fa\3\2\2\2\u00f5")
        buf.write("\u00f6\f\3\2\2\u00f6\u00f7\7\21\2\2\u00f7\u00f9\5\"\22")
        buf.write("\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb!\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fe\b\22\1\2\u00fe\u00ff\5$\23\2\u00ff")
        buf.write("\u0106\3\2\2\2\u0100\u0101\f\3\2\2\u0101\u0102\5\66\34")
        buf.write("\2\u0102\u0103\5$\23\2\u0103\u0105\3\2\2\2\u0104\u0100")
        buf.write("\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107#\3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write("\u010a\b\23\1\2\u010a\u010b\5&\24\2\u010b\u0112\3\2\2")
        buf.write("\2\u010c\u010d\f\3\2\2\u010d\u010e\58\35\2\u010e\u010f")
        buf.write("\5&\24\2\u010f\u0111\3\2\2\2\u0110\u010c\3\2\2\2\u0111")
        buf.write("\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2")
        buf.write("\u0113%\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116\b\24\1")
        buf.write("\2\u0116\u0117\5(\25\2\u0117\u011e\3\2\2\2\u0118\u0119")
        buf.write("\f\3\2\2\u0119\u011a\5\62\32\2\u011a\u011b\5(\25\2\u011b")
        buf.write("\u011d\3\2\2\2\u011c\u0118\3\2\2\2\u011d\u0120\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\'\3\2\2")
        buf.write("\2\u0120\u011e\3\2\2\2\u0121\u0122\b\25\1\2\u0122\u0123")
        buf.write("\5*\26\2\u0123\u012a\3\2\2\2\u0124\u0125\f\3\2\2\u0125")
        buf.write("\u0126\5\64\33\2\u0126\u0127\5*\26\2\u0127\u0129\3\2\2")
        buf.write("\2\u0128\u0124\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b)\3\2\2\2\u012c\u012a")
        buf.write("\3\2\2\2\u012d\u0138\5,\27\2\u012e\u012f\5\60\31\2\u012f")
        buf.write("\u0130\5*\26\2\u0130\u0138\3\2\2\2\u0131\u0132\7!\2\2")
        buf.write("\u0132\u0133\5\f\7\2\u0133\u0134\7\"\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0136\5*\26\2\u0136\u0138\3\2\2\2\u0137\u012d")
        buf.write("\3\2\2\2\u0137\u012e\3\2\2\2\u0137\u0131\3\2\2\2\u0138")
        buf.write("+\3\2\2\2\u0139\u013a\b\27\1\2\u013a\u0141\5.\30\2\u013b")
        buf.write("\u013c\7*\2\2\u013c\u013d\7!\2\2\u013d\u013e\5\26\f\2")
        buf.write("\u013e\u013f\7\"\2\2\u013f\u0141\3\2\2\2\u0140\u0139\3")
        buf.write("\2\2\2\u0140\u013b\3\2\2\2\u0141\u0149\3\2\2\2\u0142\u0143")
        buf.write("\f\3\2\2\u0143\u0144\7\13\2\2\u0144\u0145\5\30\r\2\u0145")
        buf.write("\u0146\7\f\2\2\u0146\u0148\3\2\2\2\u0147\u0142\3\2\2\2")
        buf.write("\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a-\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u0153")
        buf.write("\7)\2\2\u014d\u014e\7!\2\2\u014e\u014f\5\30\r\2\u014f")
        buf.write("\u0150\7\"\2\2\u0150\u0153\3\2\2\2\u0151\u0153\7*\2\2")
        buf.write("\u0152\u014c\3\2\2\2\u0152\u014d\3\2\2\2\u0152\u0151\3")
        buf.write("\2\2\2\u0153/\3\2\2\2\u0154\u0155\t\2\2\2\u0155\61\3\2")
        buf.write("\2\2\u0156\u0157\t\3\2\2\u0157\63\3\2\2\2\u0158\u0159")
        buf.write("\t\4\2\2\u0159\65\3\2\2\2\u015a\u015b\t\5\2\2\u015b\67")
        buf.write("\3\2\2\2\u015c\u015d\t\6\2\2\u015d9\3\2\2\2!=CSZ]ipw\u0089")
        buf.write("\u008e\u0092\u0096\u009e\u00a2\u00b9\u00c2\u00c7\u00d0")
        buf.write("\u00d3\u00dc\u00e5\u00ef\u00fa\u0106\u0112\u011e\u012a")
        buf.write("\u0137\u0140\u0149\u0152")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'break'", "'continue'", "'['", "']'", "'='", 
                     "'?'", "':'", "'||'", "'&&'", "'-'", "'~'", "'!'", 
                     "'&'", "'+'", "'/'", "'%'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'int'", "'return'", "'('", 
                     "')'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Int", "Return", "Lparen", "Rparen", 
                      "Lbrace", "Rbrace", "Comma", "Semicolon", "Punctuator", 
                      "Whitespace", "Integer", "Identifier" ]

    RULE_program = 0
    RULE_globalDeclare = 1
    RULE_func = 2
    RULE_paramlist = 3
    RULE_paramDeclare = 4
    RULE_tp = 5
    RULE_block = 6
    RULE_blockitem = 7
    RULE_statement = 8
    RULE_declaration = 9
    RULE_exprlist = 10
    RULE_expr = 11
    RULE_assignment = 12
    RULE_conditional = 13
    RULE_logicalOr = 14
    RULE_logicalAnd = 15
    RULE_equality = 16
    RULE_relational = 17
    RULE_additive = 18
    RULE_multiplicative = 19
    RULE_unary = 20
    RULE_postfix = 21
    RULE_primary = 22
    RULE_unOperator = 23
    RULE_addOperator = 24
    RULE_mulOperator = 25
    RULE_eqOperator = 26
    RULE_relOperator = 27

    ruleNames =  [ "program", "globalDeclare", "func", "paramlist", "paramDeclare", 
                   "tp", "block", "blockitem", "statement", "declaration", 
                   "exprlist", "expr", "assignment", "conditional", "logicalOr", 
                   "logicalAnd", "equality", "relational", "additive", "multiplicative", 
                   "unary", "postfix", "primary", "unOperator", "addOperator", 
                   "mulOperator", "eqOperator", "relOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    Int=29
    Return=30
    Lparen=31
    Rparen=32
    Lbrace=33
    Rbrace=34
    Comma=35
    Semicolon=36
    Punctuator=37
    Whitespace=38
    Integer=39
    Identifier=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def globalDeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.GlobalDeclareContext)
            else:
                return self.getTypedRuleContext(ExprParser.GlobalDeclareContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.globalDeclare()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.Int):
                    break

            self.state = 61
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_globalDeclare

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SymbolGlobalDeclareContext(GlobalDeclareContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.GlobalDeclareContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(ExprParser.DeclarationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbolGlobalDeclare" ):
                return visitor.visitSymbolGlobalDeclare(self)
            else:
                return visitor.visitChildren(self)


    class FuncGlobalDeclareContext(GlobalDeclareContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.GlobalDeclareContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncGlobalDeclare" ):
                return visitor.visitFuncGlobalDeclare(self)
            else:
                return visitor.visitChildren(self)



    def globalDeclare(self):

        localctx = ExprParser.GlobalDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globalDeclare)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ExprParser.FuncGlobalDeclareContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.func()
                pass

            elif la_ == 2:
                localctx = ExprParser.SymbolGlobalDeclareContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_func

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncDefineContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tp(self):
            return self.getTypedRuleContext(ExprParser.TpContext,0)

        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)
        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def paramlist(self):
            return self.getTypedRuleContext(ExprParser.ParamlistContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)
        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDefine" ):
                return visitor.visitFuncDefine(self)
            else:
                return visitor.visitChildren(self)


    class FuncDeclareContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tp(self):
            return self.getTypedRuleContext(ExprParser.TpContext,0)

        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)
        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def paramlist(self):
            return self.getTypedRuleContext(ExprParser.ParamlistContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)
        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclare" ):
                return visitor.visitFuncDeclare(self)
            else:
                return visitor.visitChildren(self)



    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ExprParser.FuncDefineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.tp(0)
                self.state = 68
                self.match(ExprParser.Identifier)
                self.state = 69
                self.match(ExprParser.Lparen)
                self.state = 70
                self.paramlist()
                self.state = 71
                self.match(ExprParser.Rparen)
                self.state = 72
                self.block()
                pass

            elif la_ == 2:
                localctx = ExprParser.FuncDeclareContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.tp(0)
                self.state = 75
                self.match(ExprParser.Identifier)
                self.state = 76
                self.match(ExprParser.Lparen)
                self.state = 77
                self.paramlist()
                self.state = 78
                self.match(ExprParser.Rparen)
                self.state = 79
                self.match(ExprParser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ParamDeclareContext)
            else:
                return self.getTypedRuleContext(ExprParser.ParamDeclareContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.Comma)
            else:
                return self.getToken(ExprParser.Comma, i)

        def getRuleIndex(self):
            return ExprParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ExprParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExprParser.Int:
                self.state = 83
                self.paramDeclare()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ExprParser.Comma:
                    self.state = 84
                    self.match(ExprParser.Comma)
                    self.state = 85
                    self.paramDeclare()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tp(self):
            return self.getTypedRuleContext(ExprParser.TpContext,0)


        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_paramDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclare" ):
                return visitor.visitParamDeclare(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclare(self):

        localctx = ExprParser.ParamDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.tp(0)
            self.state = 94
            self.match(ExprParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_tp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ScalarContext(TpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Int(self):
            return self.getToken(ExprParser.Int, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)


    class PointerContext(TpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tp(self):
            return self.getTypedRuleContext(ExprParser.TpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)



    def tp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.TpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_tp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.ScalarContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 97
            self.match(ExprParser.Int)
            self._ctx.stop = self._input.LT(-1)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.PointerContext(self, ExprParser.TpContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_tp)
                    self.state = 99
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 100
                    self.match(ExprParser.T__0) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lbrace(self):
            return self.getToken(ExprParser.Lbrace, 0)

        def Rbrace(self):
            return self.getToken(ExprParser.Rbrace, 0)

        def blockitem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlockitemContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlockitemContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ExprParser.Lbrace)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__1) | (1 << ExprParser.T__3) | (1 << ExprParser.T__4) | (1 << ExprParser.T__5) | (1 << ExprParser.T__6) | (1 << ExprParser.T__7) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18) | (1 << ExprParser.Int) | (1 << ExprParser.Return) | (1 << ExprParser.Lparen) | (1 << ExprParser.Lbrace) | (1 << ExprParser.Semicolon) | (1 << ExprParser.Integer) | (1 << ExprParser.Identifier))) != 0):
                self.state = 107
                self.blockitem()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(ExprParser.Rbrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockitemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_blockitem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclareStatementContext(BlockitemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.BlockitemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(ExprParser.DeclarationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareStatement" ):
                return visitor.visitDeclareStatement(self)
            else:
                return visitor.visitChildren(self)


    class SingleStatementContext(BlockitemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.BlockitemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleStatement" ):
                return visitor.visitSingleStatement(self)
            else:
                return visitor.visitChildren(self)



    def blockitem(self):

        localctx = ExprParser.BlockitemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blockitem)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.T__0, ExprParser.T__1, ExprParser.T__3, ExprParser.T__4, ExprParser.T__5, ExprParser.T__6, ExprParser.T__7, ExprParser.T__15, ExprParser.T__16, ExprParser.T__17, ExprParser.T__18, ExprParser.Return, ExprParser.Lparen, ExprParser.Lbrace, ExprParser.Semicolon, ExprParser.Integer, ExprParser.Identifier]:
                localctx = ExprParser.SingleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.statement()
                pass
            elif token in [ExprParser.Int]:
                localctx = ExprParser.DeclareStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForDeclareStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.pre = None # DeclarationContext
            self.cond = None # ExprContext
            self.post = None # ExprContext
            self.copyFrom(ctx)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)
        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)
        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)

        def declaration(self):
            return self.getTypedRuleContext(ExprParser.DeclarationContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForDeclareStatement" ):
                return visitor.visitForDeclareStatement(self)
            else:
                return visitor.visitChildren(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.thens = None # StatementContext
            self.elses = None # StatementContext
            self.copyFrom(ctx)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class NullStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullStatement" ):
                return visitor.visitNullStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForNaiveStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.pre = None # ExprContext
            self.cond = None # ExprContext
            self.post = None # ExprContext
            self.copyFrom(ctx)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.Semicolon)
            else:
                return self.getToken(ExprParser.Semicolon, i)
        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)
        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForNaiveStatement" ):
                return visitor.visitForNaiveStatement(self)
            else:
                return visitor.visitChildren(self)


    class ExprStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)


    class BlockStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)
        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStatement" ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)
        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class RetStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Return(self):
            return self.getToken(ExprParser.Return, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetStatement" ):
                return visitor.visitRetStatement(self)
            else:
                return visitor.visitChildren(self)


    class ContinueStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = ExprParser.RetStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(ExprParser.Return)
                self.state = 120
                self.expr()
                self.state = 121
                self.match(ExprParser.Semicolon)
                pass

            elif la_ == 2:
                localctx = ExprParser.ExprStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.expr()
                self.state = 124
                self.match(ExprParser.Semicolon)
                pass

            elif la_ == 3:
                localctx = ExprParser.NullStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(ExprParser.Semicolon)
                pass

            elif la_ == 4:
                localctx = ExprParser.BlockStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.block()
                pass

            elif la_ == 5:
                localctx = ExprParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.match(ExprParser.T__1)
                self.state = 129
                self.match(ExprParser.Lparen)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(ExprParser.Rparen)
                self.state = 132
                localctx.thens = self.statement()
                self.state = 135
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 133
                    self.match(ExprParser.T__2)
                    self.state = 134
                    localctx.elses = self.statement()


                pass

            elif la_ == 6:
                localctx = ExprParser.ForNaiveStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 137
                self.match(ExprParser.T__3)
                self.state = 138
                self.match(ExprParser.Lparen)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18) | (1 << ExprParser.Lparen) | (1 << ExprParser.Integer) | (1 << ExprParser.Identifier))) != 0):
                    self.state = 139
                    localctx.pre = self.expr()


                self.state = 142
                self.match(ExprParser.Semicolon)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18) | (1 << ExprParser.Lparen) | (1 << ExprParser.Integer) | (1 << ExprParser.Identifier))) != 0):
                    self.state = 143
                    localctx.cond = self.expr()


                self.state = 146
                self.match(ExprParser.Semicolon)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18) | (1 << ExprParser.Lparen) | (1 << ExprParser.Integer) | (1 << ExprParser.Identifier))) != 0):
                    self.state = 147
                    localctx.post = self.expr()


                self.state = 150
                self.match(ExprParser.Rparen)
                self.state = 151
                self.statement()
                pass

            elif la_ == 7:
                localctx = ExprParser.ForDeclareStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 152
                self.match(ExprParser.T__3)
                self.state = 153
                self.match(ExprParser.Lparen)
                self.state = 154
                localctx.pre = self.declaration()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18) | (1 << ExprParser.Lparen) | (1 << ExprParser.Integer) | (1 << ExprParser.Identifier))) != 0):
                    self.state = 155
                    localctx.cond = self.expr()


                self.state = 158
                self.match(ExprParser.Semicolon)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18) | (1 << ExprParser.Lparen) | (1 << ExprParser.Integer) | (1 << ExprParser.Identifier))) != 0):
                    self.state = 159
                    localctx.post = self.expr()


                self.state = 162
                self.match(ExprParser.Rparen)
                self.state = 163
                self.statement()
                pass

            elif la_ == 8:
                localctx = ExprParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 165
                self.match(ExprParser.T__4)
                self.state = 166
                self.match(ExprParser.Lparen)
                self.state = 167
                self.expr()
                self.state = 168
                self.match(ExprParser.Rparen)
                self.state = 169
                self.statement()
                pass

            elif la_ == 9:
                localctx = ExprParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 171
                self.match(ExprParser.T__5)
                self.state = 172
                self.statement()
                self.state = 173
                self.match(ExprParser.T__4)
                self.state = 174
                self.match(ExprParser.Lparen)
                self.state = 175
                self.expr()
                self.state = 176
                self.match(ExprParser.Rparen)
                self.state = 177
                self.match(ExprParser.Semicolon)
                pass

            elif la_ == 10:
                localctx = ExprParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 179
                self.match(ExprParser.T__6)
                self.state = 180
                self.match(ExprParser.Semicolon)
                pass

            elif la_ == 11:
                localctx = ExprParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 181
                self.match(ExprParser.T__7)
                self.state = 182
                self.match(ExprParser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tp(self):
            return self.getTypedRuleContext(ExprParser.TpContext,0)


        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)

        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.Integer)
            else:
                return self.getToken(ExprParser.Integer, i)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ExprParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.tp(0)
            self.state = 186
            self.match(ExprParser.Identifier)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.T__8:
                self.state = 187
                self.match(ExprParser.T__8)
                self.state = 188
                self.match(ExprParser.Integer)
                self.state = 189
                self.match(ExprParser.T__9)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExprParser.T__10:
                self.state = 195
                self.match(ExprParser.T__10)
                self.state = 196
                self.expr()


            self.state = 199
            self.match(ExprParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.Comma)
            else:
                return self.getToken(ExprParser.Comma, i)

        def getRuleIndex(self):
            return ExprParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ExprParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18) | (1 << ExprParser.Lparen) | (1 << ExprParser.Integer) | (1 << ExprParser.Identifier))) != 0):
                self.state = 201
                self.expr()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ExprParser.Comma:
                    self.state = 202
                    self.match(ExprParser.Comma)
                    self.state = 203
                    self.expr()
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conditional(self):
            return self.getTypedRuleContext(ExprParser.ConditionalContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleAssign" ):
                return visitor.visitSingleAssign(self)
            else:
                return visitor.visitChildren(self)


    class ComplexAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexAssign" ):
                return visitor.visitComplexAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SingleAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.conditional()
                pass

            elif la_ == 2:
                localctx = ExprParser.ComplexAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.unary()
                self.state = 215
                self.match(ExprParser.T__10)
                self.state = 216
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_conditional

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleCondContext(ConditionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalOr(self):
            return self.getTypedRuleContext(ExprParser.LogicalOrContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleCond" ):
                return visitor.visitSingleCond(self)
            else:
                return visitor.visitChildren(self)


    class ComplexCondContext(ConditionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalOr(self):
            return self.getTypedRuleContext(ExprParser.LogicalOrContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def conditional(self):
            return self.getTypedRuleContext(ExprParser.ConditionalContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexCond" ):
                return visitor.visitComplexCond(self)
            else:
                return visitor.visitChildren(self)



    def conditional(self):

        localctx = ExprParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SingleCondContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.logicalOr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.ComplexCondContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.logicalOr(0)
                self.state = 222
                self.match(ExprParser.T__11)
                self.state = 223
                self.expr()
                self.state = 224
                self.match(ExprParser.T__12)
                self.state = 225
                self.conditional()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_logicalOr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComplexOrContext(LogicalOrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LogicalOrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalOr(self):
            return self.getTypedRuleContext(ExprParser.LogicalOrContext,0)

        def logicalAnd(self):
            return self.getTypedRuleContext(ExprParser.LogicalAndContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexOr" ):
                return visitor.visitComplexOr(self)
            else:
                return visitor.visitChildren(self)


    class SingleOrContext(LogicalOrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LogicalOrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalAnd(self):
            return self.getTypedRuleContext(ExprParser.LogicalAndContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleOr" ):
                return visitor.visitSingleOr(self)
            else:
                return visitor.visitChildren(self)



    def logicalOr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.LogicalOrContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_logicalOr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.SingleOrContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 230
            self.logicalAnd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ComplexOrContext(self, ExprParser.LogicalOrContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOr)
                    self.state = 232
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 233
                    self.match(ExprParser.T__13)
                    self.state = 234
                    self.logicalAnd(0) 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalAndContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_logicalAnd

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleAndContext(LogicalAndContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LogicalAndContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def equality(self):
            return self.getTypedRuleContext(ExprParser.EqualityContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleAnd" ):
                return visitor.visitSingleAnd(self)
            else:
                return visitor.visitChildren(self)


    class ComplexAndContext(LogicalAndContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LogicalAndContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalAnd(self):
            return self.getTypedRuleContext(ExprParser.LogicalAndContext,0)

        def equality(self):
            return self.getTypedRuleContext(ExprParser.EqualityContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexAnd" ):
                return visitor.visitComplexAnd(self)
            else:
                return visitor.visitChildren(self)



    def logicalAnd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.LogicalAndContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_logicalAnd, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.SingleAndContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 241
            self.equality(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ComplexAndContext(self, ExprParser.LogicalAndContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalAnd)
                    self.state = 243
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 244
                    self.match(ExprParser.T__14)
                    self.state = 245
                    self.equality(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_equality

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleEqContext(EqualityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.EqualityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def relational(self):
            return self.getTypedRuleContext(ExprParser.RelationalContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleEq" ):
                return visitor.visitSingleEq(self)
            else:
                return visitor.visitChildren(self)


    class ComplexEqContext(EqualityContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.EqualityContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def equality(self):
            return self.getTypedRuleContext(ExprParser.EqualityContext,0)

        def eqOperator(self):
            return self.getTypedRuleContext(ExprParser.EqOperatorContext,0)

        def relational(self):
            return self.getTypedRuleContext(ExprParser.RelationalContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexEq" ):
                return visitor.visitComplexEq(self)
            else:
                return visitor.visitChildren(self)



    def equality(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.EqualityContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_equality, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.SingleEqContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 252
            self.relational(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ComplexEqContext(self, ExprParser.EqualityContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equality)
                    self.state = 254
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 255
                    self.eqOperator()
                    self.state = 256
                    self.relational(0) 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_relational

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComplexReContext(RelationalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.RelationalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def relational(self):
            return self.getTypedRuleContext(ExprParser.RelationalContext,0)

        def relOperator(self):
            return self.getTypedRuleContext(ExprParser.RelOperatorContext,0)

        def additive(self):
            return self.getTypedRuleContext(ExprParser.AdditiveContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexRe" ):
                return visitor.visitComplexRe(self)
            else:
                return visitor.visitChildren(self)


    class SingleReContext(RelationalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.RelationalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additive(self):
            return self.getTypedRuleContext(ExprParser.AdditiveContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleRe" ):
                return visitor.visitSingleRe(self)
            else:
                return visitor.visitChildren(self)



    def relational(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.RelationalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_relational, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.SingleReContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 264
            self.additive(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ComplexReContext(self, ExprParser.RelationalContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                    self.state = 266
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 267
                    self.relOperator()
                    self.state = 268
                    self.additive(0) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_additive

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComplexAddContext(AdditiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AdditiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additive(self):
            return self.getTypedRuleContext(ExprParser.AdditiveContext,0)

        def addOperator(self):
            return self.getTypedRuleContext(ExprParser.AddOperatorContext,0)

        def multiplicative(self):
            return self.getTypedRuleContext(ExprParser.MultiplicativeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexAdd" ):
                return visitor.visitComplexAdd(self)
            else:
                return visitor.visitChildren(self)


    class SingleAddContext(AdditiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AdditiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicative(self):
            return self.getTypedRuleContext(ExprParser.MultiplicativeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleAdd" ):
                return visitor.visitSingleAdd(self)
            else:
                return visitor.visitChildren(self)



    def additive(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.AdditiveContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_additive, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.SingleAddContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 276
            self.multiplicative(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ComplexAddContext(self, ExprParser.AdditiveContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 278
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 279
                    self.addOperator()
                    self.state = 280
                    self.multiplicative(0) 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_multiplicative

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleMulContext(MultiplicativeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.MultiplicativeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleMul" ):
                return visitor.visitSingleMul(self)
            else:
                return visitor.visitChildren(self)


    class ComplexMulContext(MultiplicativeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.MultiplicativeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicative(self):
            return self.getTypedRuleContext(ExprParser.MultiplicativeContext,0)

        def mulOperator(self):
            return self.getTypedRuleContext(ExprParser.MulOperatorContext,0)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexMul" ):
                return visitor.visitComplexMul(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.MultiplicativeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_multiplicative, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.SingleMulContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 288
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ComplexMulContext(self, ExprParser.MultiplicativeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative)
                    self.state = 290
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 291
                    self.mulOperator()
                    self.state = 292
                    self.unary() 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_unary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CastContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def tp(self):
            return self.getTypedRuleContext(ExprParser.TpContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCast" ):
                return visitor.visitCast(self)
            else:
                return visitor.visitChildren(self)


    class SingleUnaryContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix(self):
            return self.getTypedRuleContext(ExprParser.PostfixContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleUnary" ):
                return visitor.visitSingleUnary(self)
            else:
                return visitor.visitChildren(self)


    class ComplexUnaryContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unOperator(self):
            return self.getTypedRuleContext(ExprParser.UnOperatorContext,0)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexUnary" ):
                return visitor.visitComplexUnary(self)
            else:
                return visitor.visitChildren(self)



    def unary(self):

        localctx = ExprParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unary)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SingleUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.postfix(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.ComplexUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.unOperator()
                self.state = 301
                self.unary()
                pass

            elif la_ == 3:
                localctx = ExprParser.CastContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(ExprParser.Lparen)
                self.state = 304
                self.tp(0)
                self.state = 305
                self.match(ExprParser.Rparen)
                self.state = 307
                self.unary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_postfix

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComplexPostfixContext(PostfixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.PostfixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)
        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def exprlist(self):
            return self.getTypedRuleContext(ExprParser.ExprlistContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexPostfix" ):
                return visitor.visitComplexPostfix(self)
            else:
                return visitor.visitChildren(self)


    class SinglePostfixContext(PostfixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.PostfixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(ExprParser.PrimaryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinglePostfix" ):
                return visitor.visitSinglePostfix(self)
            else:
                return visitor.visitChildren(self)


    class ArrayIndexContext(PostfixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.PostfixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix(self):
            return self.getTypedRuleContext(ExprParser.PostfixContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayIndex" ):
                return visitor.visitArrayIndex(self)
            else:
                return visitor.visitChildren(self)



    def postfix(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.PostfixContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_postfix, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SinglePostfixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 312
                self.primary()
                pass

            elif la_ == 2:
                localctx = ExprParser.ComplexPostfixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 313
                self.match(ExprParser.Identifier)
                self.state = 314
                self.match(ExprParser.Lparen)
                self.state = 315
                self.exprlist()
                self.state = 316
                self.match(ExprParser.Rparen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ArrayIndexContext(self, ExprParser.PostfixContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix)
                    self.state = 320
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 321
                    self.match(ExprParser.T__8)
                    self.state = 322
                    self.expr()
                    self.state = 323
                    self.match(ExprParser.T__9) 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomIdentifierContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomIdentifier" ):
                return visitor.visitAtomIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class AtomIntegerContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Integer(self):
            return self.getToken(ExprParser.Integer, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomInteger" ):
                return visitor.visitAtomInteger(self)
            else:
                return visitor.visitChildren(self)


    class ComplexPrimaryContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexPrimary" ):
                return visitor.visitComplexPrimary(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = ExprParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primary)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.Integer]:
                localctx = ExprParser.AtomIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(ExprParser.Integer)
                pass
            elif token in [ExprParser.Lparen]:
                localctx = ExprParser.ComplexPrimaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(ExprParser.Lparen)
                self.state = 332
                self.expr()
                self.state = 333
                self.match(ExprParser.Rparen)
                pass
            elif token in [ExprParser.Identifier]:
                localctx = ExprParser.AtomIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.match(ExprParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_unOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnOperator" ):
                return visitor.visitUnOperator(self)
            else:
                return visitor.visitChildren(self)




    def unOperator(self):

        localctx = ExprParser.UnOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__15) | (1 << ExprParser.T__16) | (1 << ExprParser.T__17) | (1 << ExprParser.T__18))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_addOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOperator" ):
                return visitor.visitAddOperator(self)
            else:
                return visitor.visitChildren(self)




    def addOperator(self):

        localctx = ExprParser.AddOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_addOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            _la = self._input.LA(1)
            if not(_la==ExprParser.T__15 or _la==ExprParser.T__19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_mulOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOperator" ):
                return visitor.visitMulOperator(self)
            else:
                return visitor.visitChildren(self)




    def mulOperator(self):

        localctx = ExprParser.MulOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mulOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__0) | (1 << ExprParser.T__20) | (1 << ExprParser.T__21))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_eqOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqOperator" ):
                return visitor.visitEqOperator(self)
            else:
                return visitor.visitChildren(self)




    def eqOperator(self):

        localctx = ExprParser.EqOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_eqOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            _la = self._input.LA(1)
            if not(_la==ExprParser.T__22 or _la==ExprParser.T__23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_relOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelOperator" ):
                return visitor.visitRelOperator(self)
            else:
                return visitor.visitChildren(self)




    def relOperator(self):

        localctx = ExprParser.RelOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_relOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__24) | (1 << ExprParser.T__25) | (1 << ExprParser.T__26) | (1 << ExprParser.T__27))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.tp_sempred
        self._predicates[14] = self.logicalOr_sempred
        self._predicates[15] = self.logicalAnd_sempred
        self._predicates[16] = self.equality_sempred
        self._predicates[17] = self.relational_sempred
        self._predicates[18] = self.additive_sempred
        self._predicates[19] = self.multiplicative_sempred
        self._predicates[21] = self.postfix_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def tp_sempred(self, localctx:TpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def logicalOr_sempred(self, localctx:LogicalOrContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def logicalAnd_sempred(self, localctx:LogicalAndContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def equality_sempred(self, localctx:EqualityContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def relational_sempred(self, localctx:RelationalContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def additive_sempred(self, localctx:AdditiveContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def multiplicative_sempred(self, localctx:MultiplicativeContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def postfix_sempred(self, localctx:PostfixContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         




