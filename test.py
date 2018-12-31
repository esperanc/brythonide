from sys import _getframe 
def f ():
	_getframe(1).f_locals['local1'] = 1
	_getframe(1).f_globals['global1'] = 1
	_getframe(2).f_locals['local2'] = 2
	_getframe(2).f_globals['global2'] = 2

