
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDITION ASSIGNMENT BOOLEAN_TYPE DECIMAL_TYPE DOT EQUAL FALSE_VALUE FOR GREATER_OR_EQUAL GREATER_THAN IF INTEGER_TYPE LESS_OR_EQUAL LESS_THAN NOT_EQUAL NUMBER OPEN_BODY PARENTHESIS_CLOSE PARENTHESIS_OPEN PIPE QUOTATION_MARKS RETURN STRING_TYPE SUBTRACTION TRUE_VALUE VARIABLE\n    C : GV\n        | GC\n        | GCF\n        | GF\n    \n    GV : TD V I VA\n        | TD V\n    \n    TD : INTEGER_TYPE\n        | BOOLEAN_TYPE\n        | DECIMAL_TYPE\n        | STRING_TYPE\n    \n    V : VARIABLE\n    \n    I : ASSIGNMENT\n    \n    VA : NUMBER\n        | NUMBER DOT NUMBER\n        | TRUE_VALUE\n        | FALSE_VALUE\n        | QUOTATION_MARKS V QUOTATION_MARKS\n    \n    GC : CN PA CD PC MY C MN\n        | CN PA CD PC MY MN\n    \n    CN : IF\n    \n    CD : V S V\n        | V S VA\n        | VA S V\n        | VA S VA\n    \n    S : EQUAL\n        | GREATER_THAN\n        | LESS_THAN\n        | GREATER_OR_EQUAL\n        | LESS_OR_EQUAL\n        | NOT_EQUAL\n    \n    GF : TD V ME PR MA MY C RT MN\n        | V ME PR MA MY C MN\n        | TD V ME PR MA MY RT MN\n        | V ME PR MA MY MN\n        | TD V ME MA MY C RT MN\n        | V ME MA MY C MN\n        | TD V ME MA MY RT MN\n        | V ME MA MY MN\n    \n    PR : V\n    \n    ME : LESS_THAN\n    \n    MA : GREATER_THAN\n    \n    RT : RETURN V\n    \n    GCF : F PA CDF PC MY C MN\n        | F PA CDF PC MY MN\n    \n    F :  FOR\n    \n    CDF : NUMBER SE NUMBER SE O\n    \n    SE : PIPE\n    \n    O : SUBTRACTION\n        | ADDITION\n    \n    PA : PARENTHESIS_OPEN\n    \n    PC : PARENTHESIS_CLOSE\n    \n    MY : OPEN_BODY\n    \n    MN : LESS_OR_EQUAL\n    '
    
_lr_action_items = {'INTEGER_TYPE':([0,43,44,61,62,66,73,75,],[10,10,-52,10,10,10,10,10,]),'BOOLEAN_TYPE':([0,43,44,61,62,66,73,75,],[11,11,-52,11,11,11,11,11,]),'DECIMAL_TYPE':([0,43,44,61,62,66,73,75,],[12,12,-52,12,12,12,12,12,]),'STRING_TYPE':([0,43,44,61,62,66,73,75,],[13,13,-52,13,13,13,13,13,]),'IF':([0,43,44,61,62,66,73,75,],[14,14,-52,14,14,14,14,14,]),'FOR':([0,43,44,61,62,66,73,75,],[15,15,-52,15,15,15,15,15,]),'VARIABLE':([0,6,10,11,12,13,18,19,20,21,24,36,43,44,47,48,49,50,51,52,53,54,61,62,66,73,75,78,],[16,16,-7,-8,-9,-10,16,-40,16,-50,16,16,16,-52,16,-25,-26,-27,-28,-29,-30,16,16,16,16,16,16,16,]),'$end':([1,2,3,4,5,16,17,33,34,35,39,64,65,71,72,80,81,83,85,90,92,93,94,99,100,101,],[0,-1,-2,-3,-4,-11,-6,-13,-15,-16,-5,-38,-53,-14,-17,-34,-36,-19,-44,-37,-32,-18,-43,-33,-35,-31,]),'LESS_OR_EQUAL':([2,3,4,5,16,17,31,32,33,34,35,39,43,44,62,63,64,65,66,71,72,73,77,79,80,81,82,83,84,85,88,89,90,91,92,93,94,98,99,100,101,],[-1,-2,-3,-4,-11,-6,52,52,-13,-15,-16,-5,65,-52,65,65,-38,-53,65,-14,-17,65,65,65,-34,-36,65,-19,65,-44,65,65,-37,-42,-32,-18,-43,65,-33,-35,-31,]),'RETURN':([2,3,4,5,16,17,33,34,35,39,44,61,64,65,71,72,75,76,80,81,83,85,87,90,92,93,94,99,100,101,],[-1,-2,-3,-4,-11,-6,-13,-15,-16,-5,-52,78,-38,-53,-14,-17,78,78,-34,-36,-19,-44,78,-37,-32,-18,-43,-33,-35,-31,]),'LESS_THAN':([7,16,17,31,32,33,34,35,71,72,],[19,-11,19,50,50,-13,-15,-16,-14,-17,]),'PARENTHESIS_OPEN':([8,9,14,15,],[21,21,-20,-45,]),'ASSIGNMENT':([16,17,],[-11,25,]),'GREATER_THAN':([16,18,19,24,26,27,31,32,33,34,35,40,71,72,],[-11,29,-40,29,-39,29,49,49,-13,-15,-16,29,-14,-17,]),'EQUAL':([16,31,32,33,34,35,71,72,],[-11,48,48,-13,-15,-16,-14,-17,]),'GREATER_OR_EQUAL':([16,31,32,33,34,35,71,72,],[-11,51,51,-13,-15,-16,-14,-17,]),'NOT_EQUAL':([16,31,32,33,34,35,71,72,],[-11,53,53,-13,-15,-16,-14,-17,]),'QUOTATION_MARKS':([16,20,21,23,25,47,48,49,50,51,52,53,54,56,],[-11,36,-50,36,-12,36,-25,-26,-27,-28,-29,-30,36,72,]),'PARENTHESIS_CLOSE':([16,30,33,34,35,37,67,68,69,70,71,72,95,96,97,],[-11,46,-13,-15,-16,46,-21,-22,-24,-23,-14,-17,-46,-48,-49,]),'NUMBER':([20,21,22,23,25,47,48,49,50,51,52,53,54,55,58,59,],[33,-50,38,33,-12,33,-25,-26,-27,-28,-29,-30,33,71,74,-47,]),'TRUE_VALUE':([20,21,23,25,47,48,49,50,51,52,53,54,],[34,-50,34,-12,34,-25,-26,-27,-28,-29,-30,34,]),'FALSE_VALUE':([20,21,23,25,47,48,49,50,51,52,53,54,],[35,-50,35,-12,35,-25,-26,-27,-28,-29,-30,35,]),'OPEN_BODY':([28,29,41,42,45,46,57,60,],[44,-41,44,44,44,-51,44,44,]),'DOT':([33,],[55,]),'PIPE':([38,74,],[59,59,]),'SUBTRACTION':([59,86,],[-47,96,]),'ADDITION':([59,86,],[-47,97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'C':([0,43,61,62,66,73,75,],[1,63,76,79,82,84,87,]),'GV':([0,43,61,62,66,73,75,],[2,2,2,2,2,2,2,]),'GC':([0,43,61,62,66,73,75,],[3,3,3,3,3,3,3,]),'GCF':([0,43,61,62,66,73,75,],[4,4,4,4,4,4,4,]),'GF':([0,43,61,62,66,73,75,],[5,5,5,5,5,5,5,]),'TD':([0,43,61,62,66,73,75,],[6,6,6,6,6,6,6,]),'V':([0,6,18,20,24,36,43,47,54,61,62,66,73,75,78,],[7,17,26,31,26,56,7,67,70,7,7,7,7,7,91,]),'CN':([0,43,61,62,66,73,75,],[8,8,8,8,8,8,8,]),'F':([0,43,61,62,66,73,75,],[9,9,9,9,9,9,9,]),'ME':([7,17,],[18,24,]),'PA':([8,9,],[20,22,]),'I':([17,],[23,]),'PR':([18,24,],[27,40,]),'MA':([18,24,27,40,],[28,41,42,60,]),'CD':([20,],[30,]),'VA':([20,23,47,54,],[32,39,68,69,]),'CDF':([22,],[37,]),'MY':([28,41,42,45,57,60,],[43,61,62,66,73,75,]),'PC':([30,37,],[45,57,]),'S':([31,32,],[47,54,]),'SE':([38,74,],[58,86,]),'MN':([43,62,63,66,73,77,79,82,84,88,89,98,],[64,80,81,83,85,90,92,93,94,99,100,101,]),'RT':([61,75,76,87,],[77,88,89,98,]),'O':([86,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> C","S'",1,None,None,None),
  ('C -> GV','C',1,'p_C','syntactic_analyzer.py',99),
  ('C -> GC','C',1,'p_C','syntactic_analyzer.py',100),
  ('C -> GCF','C',1,'p_C','syntactic_analyzer.py',101),
  ('C -> GF','C',1,'p_C','syntactic_analyzer.py',102),
  ('GV -> TD V I VA','GV',4,'p_GV','syntactic_analyzer.py',110),
  ('GV -> TD V','GV',2,'p_GV','syntactic_analyzer.py',111),
  ('TD -> INTEGER_TYPE','TD',1,'p_TD','syntactic_analyzer.py',124),
  ('TD -> BOOLEAN_TYPE','TD',1,'p_TD','syntactic_analyzer.py',125),
  ('TD -> DECIMAL_TYPE','TD',1,'p_TD','syntactic_analyzer.py',126),
  ('TD -> STRING_TYPE','TD',1,'p_TD','syntactic_analyzer.py',127),
  ('V -> VARIABLE','V',1,'p_V','syntactic_analyzer.py',135),
  ('I -> ASSIGNMENT','I',1,'p_I','syntactic_analyzer.py',143),
  ('VA -> NUMBER','VA',1,'p_VA','syntactic_analyzer.py',151),
  ('VA -> NUMBER DOT NUMBER','VA',3,'p_VA','syntactic_analyzer.py',152),
  ('VA -> TRUE_VALUE','VA',1,'p_VA','syntactic_analyzer.py',153),
  ('VA -> FALSE_VALUE','VA',1,'p_VA','syntactic_analyzer.py',154),
  ('VA -> QUOTATION_MARKS V QUOTATION_MARKS','VA',3,'p_VA','syntactic_analyzer.py',155),
  ('GC -> CN PA CD PC MY C MN','GC',7,'p_GC','syntactic_analyzer.py',166),
  ('GC -> CN PA CD PC MY MN','GC',6,'p_GC','syntactic_analyzer.py',167),
  ('CN -> IF','CN',1,'p_CN','syntactic_analyzer.py',178),
  ('CD -> V S V','CD',3,'p_CD','syntactic_analyzer.py',186),
  ('CD -> V S VA','CD',3,'p_CD','syntactic_analyzer.py',187),
  ('CD -> VA S V','CD',3,'p_CD','syntactic_analyzer.py',188),
  ('CD -> VA S VA','CD',3,'p_CD','syntactic_analyzer.py',189),
  ('S -> EQUAL','S',1,'p_S','syntactic_analyzer.py',197),
  ('S -> GREATER_THAN','S',1,'p_S','syntactic_analyzer.py',198),
  ('S -> LESS_THAN','S',1,'p_S','syntactic_analyzer.py',199),
  ('S -> GREATER_OR_EQUAL','S',1,'p_S','syntactic_analyzer.py',200),
  ('S -> LESS_OR_EQUAL','S',1,'p_S','syntactic_analyzer.py',201),
  ('S -> NOT_EQUAL','S',1,'p_S','syntactic_analyzer.py',202),
  ('GF -> TD V ME PR MA MY C RT MN','GF',9,'p_GF','syntactic_analyzer.py',210),
  ('GF -> V ME PR MA MY C MN','GF',7,'p_GF','syntactic_analyzer.py',211),
  ('GF -> TD V ME PR MA MY RT MN','GF',8,'p_GF','syntactic_analyzer.py',212),
  ('GF -> V ME PR MA MY MN','GF',6,'p_GF','syntactic_analyzer.py',213),
  ('GF -> TD V ME MA MY C RT MN','GF',8,'p_GF','syntactic_analyzer.py',214),
  ('GF -> V ME MA MY C MN','GF',6,'p_GF','syntactic_analyzer.py',215),
  ('GF -> TD V ME MA MY RT MN','GF',7,'p_GF','syntactic_analyzer.py',216),
  ('GF -> V ME MA MY MN','GF',5,'p_GF','syntactic_analyzer.py',217),
  ('PR -> V','PR',1,'p_PR','syntactic_analyzer.py',234),
  ('ME -> LESS_THAN','ME',1,'p_ME','syntactic_analyzer.py',242),
  ('MA -> GREATER_THAN','MA',1,'p_MA','syntactic_analyzer.py',250),
  ('RT -> RETURN V','RT',2,'p_RT','syntactic_analyzer.py',258),
  ('GCF -> F PA CDF PC MY C MN','GCF',7,'p_GCF','syntactic_analyzer.py',266),
  ('GCF -> F PA CDF PC MY MN','GCF',6,'p_GCF','syntactic_analyzer.py',267),
  ('F -> FOR','F',1,'p_F','syntactic_analyzer.py',278),
  ('CDF -> NUMBER SE NUMBER SE O','CDF',5,'p_CDF','syntactic_analyzer.py',286),
  ('SE -> PIPE','SE',1,'p_PIPE','syntactic_analyzer.py',294),
  ('O -> SUBTRACTION','O',1,'p_O','syntactic_analyzer.py',302),
  ('O -> ADDITION','O',1,'p_O','syntactic_analyzer.py',303),
  ('PA -> PARENTHESIS_OPEN','PA',1,'p_PA','syntactic_analyzer.py',314),
  ('PC -> PARENTHESIS_CLOSE','PC',1,'p_PC','syntactic_analyzer.py',322),
  ('MY -> OPEN_BODY','MY',1,'p_MY','syntactic_analyzer.py',330),
  ('MN -> LESS_OR_EQUAL','MN',1,'p_MN','syntactic_analyzer.py',338),
]