
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDITION ASSIGNMENT BOOLEAN_TYPE DECIMAL_TYPE DOT EQUAL FALSE_VALUE FOR GREATER_OR_EQUAL GREATER_THAN IF INTEGER_TYPE LESS_OR_EQUAL LESS_THAN NOT_EQUAL NUMBER OPEN_BODY PARENTHESIS_CLOSE PARENTHESIS_OPEN PIPE QUOTATION_MARKS RETURN STRING_TYPE SUBTRACTION TRUE_VALUE VARIABLE\n\tPROGRAM : BLOCK_CODE\n\t\n    BLOCK_CODE : GV\n            | GC\n            | GF\n            | GCF\n            | EMPTY\n    \n    C : GV\n        | GC\n        | GCF\n        | EMPTY\n    \n    GV : TD V I VA BLOCK_CODE\n        | TD V BLOCK_CODE\n        | EMPTY\n    \n    TD : INTEGER_TYPE\n        | BOOLEAN_TYPE\n        | DECIMAL_TYPE\n        | STRING_TYPE\n    \n    V : VARIABLE\n    \n    I : ASSIGNMENT\n    \n    VA : NUMBER\n       | NUMBER DOT NUMBER\n       | TRUE_VALUE\n       | FALSE_VALUE\n       | QUOTATION_MARKS V QUOTATION_MARKS\n    \n    GC : CN PA CD PC MY C MN BLOCK_CODE\n        | CN PA CD PC MY MN BLOCK_CODE\n        | EMPTY\n    \n    CN : IF\n    \n    CD : V S V\n        | V S VA\n        | VA S V\n        | VA S VA\n    \n    S : EQUAL\n        | GREATER_THAN\n        | LESS_THAN\n        | GREATER_OR_EQUAL\n        | LESS_OR_EQUAL\n        | NOT_EQUAL\n    \n    GF : TD V ME PR MA MY C RT MN BLOCK_CODE\n        | V ME PR MA MY C MN BLOCK_CODE\n        | TD V ME PR MA MY RT MN BLOCK_CODE\n        | V ME PR MA MY MN BLOCK_CODE\n        | TD V ME MA MY C RT MN BLOCK_CODE\n        | V ME MA MY C MN BLOCK_CODE\n        | TD V ME MA MY RT MN BLOCK_CODE\n        | V ME MA MY MN BLOCK_CODE\n        | EMPTY\n    \n    PR : V\n    \n    ME : LESS_THAN\n    \n    MA : GREATER_THAN\n    \n    RT : RETURN V\n    \n    GCF : F PA CDF PC MY C MN BLOCK_CODE\n        | F PA CDF PC MY MN BLOCK_CODE\n        | EMPTY\n    \n    F :  FOR\n    \n    CDF : NUMBER SE NUMBER SE O\n    \n    SE : PIPE\n    \n    O : SUBTRACTION\n        | ADDITION\n    \n    PA : PARENTHESIS_OPEN\n    \n    PC : PARENTHESIS_CLOSE\n    \n    MY : OPEN_BODY\n    \n    MN : LESS_OR_EQUAL\n    \n\tEMPTY :\n\t'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,17,19,26,36,37,38,42,63,68,73,80,81,89,90,91,94,96,101,103,104,105,106,107,108,109,114,115,116,117,118,119,120,121,122,123,],[-64,0,-1,-2,-3,-4,-5,-6,-18,-64,-12,-20,-22,-23,-64,-11,-64,-63,-21,-24,-64,-64,-46,-64,-64,-64,-64,-42,-44,-64,-26,-64,-53,-64,-64,-45,-40,-25,-52,-64,-41,-43,-39,]),'INTEGER_TYPE':([0,17,19,36,37,38,42,46,47,65,66,68,73,75,80,81,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[12,-18,12,-20,-22,-23,12,12,-62,12,12,12,-63,12,-21,-24,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'BOOLEAN_TYPE':([0,17,19,36,37,38,42,46,47,65,66,68,73,75,80,81,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[13,-18,13,-20,-22,-23,13,13,-62,13,13,13,-63,13,-21,-24,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'DECIMAL_TYPE':([0,17,19,36,37,38,42,46,47,65,66,68,73,75,80,81,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[14,-18,14,-20,-22,-23,14,14,-62,14,14,14,-63,14,-21,-24,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'STRING_TYPE':([0,17,19,36,37,38,42,46,47,65,66,68,73,75,80,81,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[15,-18,15,-20,-22,-23,15,15,-62,15,15,15,-63,15,-21,-24,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'IF':([0,17,19,36,37,38,42,46,47,65,66,68,73,75,80,81,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[16,-18,16,-20,-22,-23,16,16,-62,16,16,16,-63,16,-21,-24,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'VARIABLE':([0,8,12,13,14,15,17,19,20,21,22,23,27,36,37,38,39,42,50,51,52,53,54,55,56,57,68,73,74,80,81,87,89,90,92,94,96,101,103,106,108,114,115,120,],[17,17,-14,-15,-16,-17,-18,17,17,-49,17,-60,17,-20,-22,-23,17,17,17,-33,-34,-35,-36,-37,-38,17,17,-63,17,-21,-24,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'FOR':([0,17,19,36,37,38,42,46,47,65,66,68,73,75,80,81,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[18,-18,18,-20,-22,-23,18,18,-62,18,18,18,-63,18,-21,-24,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'LESS_OR_EQUAL':([3,4,5,6,7,17,19,26,34,35,36,37,38,42,46,47,63,66,67,68,69,70,71,72,73,75,80,81,82,86,88,89,90,91,92,93,94,95,96,99,100,101,102,103,104,105,106,107,108,109,113,114,115,116,117,118,119,120,121,122,123,],[-2,-3,-4,-5,-6,-18,-64,-12,55,55,-20,-22,-23,-64,73,-62,-11,73,73,-64,-7,-8,-9,-10,-63,73,-21,-24,73,73,73,-64,-64,-46,-64,73,-64,73,-64,73,73,-64,-51,-64,-42,-44,-64,-26,-64,-53,73,-64,-64,-45,-40,-25,-52,-64,-41,-43,-39,]),'RETURN':([3,4,5,6,7,17,19,26,36,37,38,42,47,63,65,68,69,70,71,72,73,80,81,84,85,89,90,91,92,94,96,98,101,103,104,105,106,107,108,109,114,115,116,117,118,119,120,121,122,123,],[-2,-3,-4,-5,-6,-18,-64,-12,-20,-22,-23,-64,-62,-11,87,-64,-7,-8,-9,-10,-63,-21,-24,87,87,-64,-64,-46,-64,-64,-64,87,-64,-64,-42,-44,-64,-26,-64,-53,-64,-64,-45,-40,-25,-52,-64,-41,-43,-39,]),'LESS_THAN':([9,17,19,34,35,36,37,38,80,81,],[21,-18,21,53,53,-20,-22,-23,-21,-24,]),'PARENTHESIS_OPEN':([10,11,16,18,],[23,23,-28,-55,]),'ASSIGNMENT':([17,19,92,],[-18,28,28,]),'GREATER_THAN':([17,20,21,27,29,30,34,35,36,37,38,43,80,81,],[-18,32,-49,32,-48,32,52,52,-20,-22,-23,32,-21,-24,]),'EQUAL':([17,34,35,36,37,38,80,81,],[-18,51,51,-20,-22,-23,-21,-24,]),'GREATER_OR_EQUAL':([17,34,35,36,37,38,80,81,],[-18,54,54,-20,-22,-23,-21,-24,]),'NOT_EQUAL':([17,34,35,36,37,38,80,81,],[-18,56,56,-20,-22,-23,-21,-24,]),'QUOTATION_MARKS':([17,22,23,25,28,50,51,52,53,54,55,56,57,59,],[-18,39,-60,39,-19,39,-33,-34,-35,-36,-37,-38,39,81,]),'PARENTHESIS_CLOSE':([17,33,36,37,38,40,76,77,78,79,80,81,110,111,112,],[-18,49,-20,-22,-23,49,-29,-30,-32,-31,-21,-24,-56,-58,-59,]),'NUMBER':([22,23,24,25,28,50,51,52,53,54,55,56,57,58,61,62,],[36,-60,41,36,-19,36,-33,-34,-35,-36,-37,-38,36,80,83,-57,]),'TRUE_VALUE':([22,23,25,28,50,51,52,53,54,55,56,57,],[37,-60,37,-19,37,-33,-34,-35,-36,-37,-38,37,]),'FALSE_VALUE':([22,23,25,28,50,51,52,53,54,55,56,57,],[38,-60,38,-19,38,-33,-34,-35,-36,-37,-38,38,]),'OPEN_BODY':([31,32,44,45,48,49,60,64,],[47,-50,47,47,47,-61,47,47,]),'DOT':([36,],[58,]),'PIPE':([41,83,],[62,62,]),'SUBTRACTION':([62,97,],[-57,111,]),'ADDITION':([62,97,],[-57,112,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'BLOCK_CODE':([0,19,42,68,89,90,92,94,96,101,103,106,108,114,115,120,],[2,26,63,91,104,105,26,107,109,116,117,118,119,121,122,123,]),'GV':([0,19,42,46,65,66,68,75,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[3,3,3,69,69,69,3,69,69,69,3,3,3,3,3,3,3,3,3,3,3,3,]),'GC':([0,19,42,46,65,66,68,75,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[4,4,4,70,70,70,4,70,70,70,4,4,4,4,4,4,4,4,4,4,4,4,]),'GF':([0,19,42,68,89,90,92,94,96,101,103,106,108,114,115,120,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'GCF':([0,19,42,46,65,66,68,75,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[6,6,6,71,71,71,6,71,71,71,6,6,6,6,6,6,6,6,6,6,6,6,]),'EMPTY':([0,19,42,46,65,66,68,75,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[7,7,7,72,72,72,7,72,72,72,7,7,7,7,7,7,7,7,7,7,7,7,]),'TD':([0,19,42,46,65,66,68,75,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[8,8,8,74,74,74,8,74,74,74,8,8,8,8,8,8,8,8,8,8,8,8,]),'V':([0,8,19,20,22,27,39,42,50,57,68,74,87,89,90,92,94,96,101,103,106,108,114,115,120,],[9,19,9,29,34,29,59,9,76,79,9,92,102,9,9,9,9,9,9,9,9,9,9,9,9,]),'CN':([0,19,42,46,65,66,68,75,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'F':([0,19,42,46,65,66,68,75,82,84,89,90,92,94,96,101,103,106,108,114,115,120,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'ME':([9,19,],[20,27,]),'PA':([10,11,],[22,24,]),'I':([19,92,],[25,25,]),'PR':([20,27,],[30,43,]),'MA':([20,27,30,43,],[31,44,45,64,]),'CD':([22,],[33,]),'VA':([22,25,50,57,],[35,42,77,78,]),'CDF':([24,],[40,]),'MY':([31,44,45,48,60,64,],[46,65,66,75,82,84,]),'PC':([33,40,],[48,60,]),'S':([34,35,],[50,57,]),'SE':([41,83,],[61,97,]),'C':([46,65,66,75,82,84,],[67,85,88,93,95,98,]),'MN':([46,66,67,75,82,86,88,93,95,99,100,113,],[68,89,90,94,96,101,103,106,108,114,115,120,]),'RT':([65,84,85,98,],[86,99,100,113,]),'O':([97,],[110,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> BLOCK_CODE','PROGRAM',1,'p_PROGRAM','<input>',104),
  ('BLOCK_CODE -> GV','BLOCK_CODE',1,'p_BLOCK_CODE','<input>',111),
  ('BLOCK_CODE -> GC','BLOCK_CODE',1,'p_BLOCK_CODE','<input>',112),
  ('BLOCK_CODE -> GF','BLOCK_CODE',1,'p_BLOCK_CODE','<input>',113),
  ('BLOCK_CODE -> GCF','BLOCK_CODE',1,'p_BLOCK_CODE','<input>',114),
  ('BLOCK_CODE -> EMPTY','BLOCK_CODE',1,'p_BLOCK_CODE','<input>',115),
  ('C -> GV','C',1,'p_C','<input>',126),
  ('C -> GC','C',1,'p_C','<input>',127),
  ('C -> GCF','C',1,'p_C','<input>',128),
  ('C -> EMPTY','C',1,'p_C','<input>',129),
  ('GV -> TD V I VA BLOCK_CODE','GV',5,'p_GV','<input>',166),
  ('GV -> TD V BLOCK_CODE','GV',3,'p_GV','<input>',167),
  ('GV -> EMPTY','GV',1,'p_GV','<input>',168),
  ('TD -> INTEGER_TYPE','TD',1,'p_TD','<input>',183),
  ('TD -> BOOLEAN_TYPE','TD',1,'p_TD','<input>',184),
  ('TD -> DECIMAL_TYPE','TD',1,'p_TD','<input>',185),
  ('TD -> STRING_TYPE','TD',1,'p_TD','<input>',186),
  ('V -> VARIABLE','V',1,'p_V','<input>',194),
  ('I -> ASSIGNMENT','I',1,'p_I','<input>',202),
  ('VA -> NUMBER','VA',1,'p_VA','<input>',210),
  ('VA -> NUMBER DOT NUMBER','VA',3,'p_VA','<input>',211),
  ('VA -> TRUE_VALUE','VA',1,'p_VA','<input>',212),
  ('VA -> FALSE_VALUE','VA',1,'p_VA','<input>',213),
  ('VA -> QUOTATION_MARKS V QUOTATION_MARKS','VA',3,'p_VA','<input>',214),
  ('GC -> CN PA CD PC MY C MN BLOCK_CODE','GC',8,'p_GC','<input>',225),
  ('GC -> CN PA CD PC MY MN BLOCK_CODE','GC',7,'p_GC','<input>',226),
  ('GC -> EMPTY','GC',1,'p_GC','<input>',227),
  ('CN -> IF','CN',1,'p_CN','<input>',240),
  ('CD -> V S V','CD',3,'p_CD','<input>',350),
  ('CD -> V S VA','CD',3,'p_CD','<input>',351),
  ('CD -> VA S V','CD',3,'p_CD','<input>',352),
  ('CD -> VA S VA','CD',3,'p_CD','<input>',353),
  ('S -> EQUAL','S',1,'p_S','<input>',362),
  ('S -> GREATER_THAN','S',1,'p_S','<input>',363),
  ('S -> LESS_THAN','S',1,'p_S','<input>',364),
  ('S -> GREATER_OR_EQUAL','S',1,'p_S','<input>',365),
  ('S -> LESS_OR_EQUAL','S',1,'p_S','<input>',366),
  ('S -> NOT_EQUAL','S',1,'p_S','<input>',367),
  ('GF -> TD V ME PR MA MY C RT MN BLOCK_CODE','GF',10,'p_GF','<input>',383),
  ('GF -> V ME PR MA MY C MN BLOCK_CODE','GF',8,'p_GF','<input>',384),
  ('GF -> TD V ME PR MA MY RT MN BLOCK_CODE','GF',9,'p_GF','<input>',385),
  ('GF -> V ME PR MA MY MN BLOCK_CODE','GF',7,'p_GF','<input>',386),
  ('GF -> TD V ME MA MY C RT MN BLOCK_CODE','GF',9,'p_GF','<input>',387),
  ('GF -> V ME MA MY C MN BLOCK_CODE','GF',7,'p_GF','<input>',388),
  ('GF -> TD V ME MA MY RT MN BLOCK_CODE','GF',8,'p_GF','<input>',389),
  ('GF -> V ME MA MY MN BLOCK_CODE','GF',6,'p_GF','<input>',390),
  ('GF -> EMPTY','GF',1,'p_GF','<input>',391),
  ('PR -> V','PR',1,'p_PR','<input>',425),
  ('ME -> LESS_THAN','ME',1,'p_ME','<input>',433),
  ('MA -> GREATER_THAN','MA',1,'p_MA','<input>',441),
  ('RT -> RETURN V','RT',2,'p_RT','<input>',449),
  ('GCF -> F PA CDF PC MY C MN BLOCK_CODE','GCF',8,'p_GCF','<input>',457),
  ('GCF -> F PA CDF PC MY MN BLOCK_CODE','GCF',7,'p_GCF','<input>',458),
  ('GCF -> EMPTY','GCF',1,'p_GCF','<input>',459),
  ('F -> FOR','F',1,'p_F','<input>',472),
  ('CDF -> NUMBER SE NUMBER SE O','CDF',5,'p_CDF','<input>',480),
  ('SE -> PIPE','SE',1,'p_PIPE','<input>',488),
  ('O -> SUBTRACTION','O',1,'p_O','<input>',496),
  ('O -> ADDITION','O',1,'p_O','<input>',497),
  ('PA -> PARENTHESIS_OPEN','PA',1,'p_PA','<input>',508),
  ('PC -> PARENTHESIS_CLOSE','PC',1,'p_PC','<input>',516),
  ('MY -> OPEN_BODY','MY',1,'p_MY','<input>',524),
  ('MN -> LESS_OR_EQUAL','MN',1,'p_MN','<input>',532),
  ('EMPTY -> <empty>','EMPTY',0,'p_EMPTY','<input>',539),
]
