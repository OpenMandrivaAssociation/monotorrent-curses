using System;

namespace Mono.Terminal {
public partial class Curses {
	public const int A_NORMAL = unchecked((int)0x0);
	public const int A_STANDOUT = unchecked((int)0x10000);
	public const int A_UNDERLINE = unchecked((int)0x20000);
	public const int A_REVERSE = unchecked((int)0x40000);
	public const int A_BLINK = unchecked((int)0x80000);
	public const int A_DIM = unchecked((int)0x100000);
	public const int A_BOLD = unchecked((int)0x200000);
	public const int A_PROTECT = unchecked((int)0x1000000);
	public const int A_INVIS = unchecked((int)0x800000);
	public const int ACS_LLCORNER = unchecked((int)0x40006d);
	public const int ACS_LRCORNER = unchecked((int)0x40006a);
	public const int ACS_HLINE = unchecked((int)0x400071);
	public const int ACS_ULCORNER = unchecked((int)0x40006c);
	public const int ACS_URCORNER = unchecked((int)0x40006b);
	public const int ACS_VLINE = unchecked((int)0x400078);
	public const int COLOR_BLACK = unchecked((int)0x0);
	public const int COLOR_RED = unchecked((int)0x1);
	public const int COLOR_GREEN = unchecked((int)0x2);
	public const int COLOR_YELLOW = unchecked((int)0x3);
	public const int COLOR_BLUE = unchecked((int)0x4);
	public const int COLOR_MAGENTA = unchecked((int)0x5);
	public const int COLOR_CYAN = unchecked((int)0x6);
	public const int COLOR_WHITE = unchecked((int)0x7);
public enum Event : long {
		Button1Pressed = unchecked((int)0x2),
		Button1Released = unchecked((int)0x1),
		Button1Clicked = unchecked((int)0x4),
		Button1DoubleClicked = unchecked((int)0x8),
		Button1TripleClicked = unchecked((int)0x10),
		Button2Pressed = unchecked((int)0x80),
		Button2Released = unchecked((int)0x40),
		Button2Clicked = unchecked((int)0x100),
		Button2DoubleClicked = unchecked((int)0x200),
		Button2TrippleClicked = unchecked((int)0x400),
		Button3Pressed = unchecked((int)0x2000),
		Button3Released = unchecked((int)0x1000),
		Button3Clicked = unchecked((int)0x4000),
		Button3DoubleClicked = unchecked((int)0x8000),
		Button3TripleClicked = unchecked((int)0x10000),
		Button4Pressed = unchecked((int)0x80000),
		Button4Released = unchecked((int)0x40000),
		Button4Clicked = unchecked((int)0x100000),
		Button4DoubleClicked = unchecked((int)0x200000),
		Button4TripleClicked = unchecked((int)0x400000),
		ButtonShift = unchecked((int)0x2000000),
		ButtonCtrl = unchecked((int)0x1000000),
		ButtonAlt = unchecked((int)0x4000000),
		ReportMousePosition = unchecked((int)0x8000000),
		AllEvents = unchecked((int)0x7ffffff),
}
	public const int ERR = unchecked((int)0xffffffff);
	public const int KeyBackspace = unchecked((int)0x107);
	public const int KeyUp = unchecked((int)0x103);
	public const int KeyDown = unchecked((int)0x102);
	public const int KeyLeft = unchecked((int)0x104);
	public const int KeyRight = unchecked((int)0x105);
	public const int KeyNPage = unchecked((int)0x152);
	public const int KeyPPage = unchecked((int)0x153);
	public const int KeyHome = unchecked((int)0x106);
	public const int KeyMouse = unchecked((int)0x199);
	public const int KeyEnd = unchecked((int)0x168);


	static public int ColorPair(int n){
		return 0 + n * 256;
	}

}
}
