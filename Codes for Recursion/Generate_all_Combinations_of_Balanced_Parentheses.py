#Generate all Combinations of Balanced Parentheses in python ?
"""We are given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses."""

def printParenthesis(str, n):
	if n > 0:
		_printParenthesis(str, 0, n, 0, 0)
	return


def _printParenthesis(str, pos, n, open, close):

	if close == n:
		for i in str:
			print(i, end="")
		print()
		return
	else:
		if open > close:
			str[pos] = '}'
			_printParenthesis(str, pos + 1, n, open, close + 1)
		if open < n:
			str[pos] = '{'
			_printParenthesis(str, pos + 1, n, open + 1, close)


n = 3
string = [""] * 2 * n
printParenthesis(string, n)