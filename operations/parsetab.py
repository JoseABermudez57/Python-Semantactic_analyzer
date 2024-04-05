
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDITION ASSIGNMENT BOOLEAN_TYPE DECIMAL_TYPE DOT EQUAL FALSE_VALUE FOR GREATER_OR_EQUAL GREATER_THAN IF INTEGER_TYPE LESS_OR_EQUAL LESS_THAN NOT_EQUAL NUMBER OPEN_BODY PARENTHESIS_CLOSE PARENTHESIS_OPEN PIPE QUOTATION_MARKS RETURN STRING_TYPE SUBTRACTION TRUE_VALUE VARIABLE\n\tPROGRAM : BLOCK_CODE\n\t\n    BLOCK_CODE : GV\n            | GC\n            | GF\n            | GCF\n            | PRINT\n            | EMPTY\n    \n    C : GV\n        | GC\n        | GCF\n        | PRINT\n        | EMPTY\n    \n    GV : TD V I VA BLOCK_CODE\n        | TD V BLOCK_CODE\n        | EMPTY\n    \n    PRINT : AO VAP AC BLOCK_CODE\n        | EMPTY\n    \n    AO : SUBTRACTION MA\n    \n    VAP : V\n        | VA\n        | CD\n        | FR\n    \n    FR : TD V ME PR MA\n        | TD V ME MA\n    \n    AC : ME SUBTRACTION\n    \n    TD : INTEGER_TYPE\n        | BOOLEAN_TYPE\n        | DECIMAL_TYPE\n        | STRING_TYPE\n    \n    V : VARIABLE\n    \n    I : ASSIGNMENT\n    \n    VA : NUMBER\n       | NUMBER DOT NUMBER\n       | TRUE_VALUE\n       | FALSE_VALUE\n       | QUOTATION_MARKS V QUOTATION_MARKS\n    \n    GC : CN PA CD PC MY C MN BLOCK_CODE\n        | CN PA CD PC MY MN BLOCK_CODE\n        | EMPTY\n    \n    CN : IF\n    \n    CD : V S V\n        | V S VA\n        | VA S V\n        | VA S VA\n    \n    S : EQUAL\n        | GREATER_THAN\n        | LESS_THAN\n        | GREATER_OR_EQUAL\n        | LESS_OR_EQUAL\n        | NOT_EQUAL\n    \n    GF : TD V ME PR MA MY C RT MN BLOCK_CODE\n        | V ME PR MA MY C MN BLOCK_CODE\n        | TD V ME PR MA MY RT MN BLOCK_CODE\n        | V ME PR MA MY MN BLOCK_CODE\n        | TD V ME MA MY C RT MN BLOCK_CODE\n        | V ME MA MY C MN BLOCK_CODE\n        | TD V ME MA MY RT MN BLOCK_CODE\n        | V ME MA MY MN BLOCK_CODE\n        | EMPTY\n    \n    PR : V\n    \n    ME : LESS_THAN\n    \n    MA : GREATER_THAN\n    \n    RT : RETURN V\n    \n    GCF : F PA CDF PC MY C MN BLOCK_CODE\n        | F PA CDF PC MY MN BLOCK_CODE\n        | EMPTY\n    \n    F :  FOR\n    \n    CDF : NUMBER SE NUMBER SE O\n    \n    SE : PIPE\n    \n    O : SUBTRACTION\n        | ADDITION\n    \n    PA : PARENTHESIS_OPEN\n    \n    PC : PARENTHESIS_CLOSE\n    \n    MY : OPEN_BODY\n    \n    MN : LESS_OR_EQUAL\n    \n\tEMPTY :\n\t'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,19,22,33,34,35,41,52,65,76,77,82,83,85,90,96,108,109,110,113,115,121,123,124,125,126,127,128,129,134,135,136,137,138,139,140,141,142,143,],[-76,0,-1,-2,-3,-4,-5,-6,-7,-30,-76,-32,-34,-35,-14,-76,-76,-16,-25,-33,-36,-13,-76,-75,-76,-76,-58,-76,-76,-76,-76,-54,-56,-76,-38,-76,-65,-76,-76,-57,-52,-37,-64,-76,-53,-55,-51,]),'INTEGER_TYPE':([0,13,19,22,33,34,35,38,39,52,65,69,70,77,82,83,87,88,90,96,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[14,14,-30,14,-32,-34,-35,-18,-62,14,14,14,-74,-25,-33,-36,14,14,14,-75,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'BOOLEAN_TYPE':([0,13,19,22,33,34,35,38,39,52,65,69,70,77,82,83,87,88,90,96,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[15,15,-30,15,-32,-34,-35,-18,-62,15,15,15,-74,-25,-33,-36,15,15,15,-75,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'DECIMAL_TYPE':([0,13,19,22,33,34,35,38,39,52,65,69,70,77,82,83,87,88,90,96,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[16,16,-30,16,-32,-34,-35,-18,-62,16,16,16,-74,-25,-33,-36,16,16,16,-75,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'STRING_TYPE':([0,13,19,22,33,34,35,38,39,52,65,69,70,77,82,83,87,88,90,96,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[17,17,-30,17,-32,-34,-35,-18,-62,17,17,17,-74,-25,-33,-36,17,17,17,-75,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'IF':([0,19,22,33,34,35,52,65,69,70,77,82,83,87,88,90,96,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[18,-30,18,-32,-34,-35,18,18,18,-74,-25,-33,-36,18,18,18,-75,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'VARIABLE':([0,9,13,14,15,16,17,19,22,23,24,25,26,33,34,35,36,37,38,39,42,52,54,55,56,57,58,59,60,61,65,77,82,83,84,90,96,97,106,108,109,111,113,115,121,123,126,128,134,135,140,],[19,19,19,-26,-27,-28,-29,-30,19,19,-61,19,-72,-32,-34,-35,19,19,-18,-62,19,19,19,-45,-46,-47,-48,-49,-50,19,19,-25,-33,-36,19,19,-75,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'FOR':([0,19,22,33,34,35,52,65,69,70,77,82,83,87,88,90,96,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[20,-30,20,-32,-34,-35,20,20,20,-74,-25,-33,-36,20,20,20,-75,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'SUBTRACTION':([0,19,22,24,33,34,35,52,53,65,69,70,75,77,82,83,87,88,90,96,98,99,103,108,109,111,113,115,116,121,123,126,128,134,135,140,],[21,-30,21,-61,-32,-34,-35,21,77,21,21,-74,-69,-25,-33,-36,21,21,21,-75,21,21,21,21,21,21,21,21,131,21,21,21,21,21,21,21,]),'LESS_OR_EQUAL':([3,4,5,6,7,8,19,22,29,30,33,34,35,41,48,49,52,65,69,70,76,77,82,83,85,88,89,90,91,92,93,94,95,96,98,99,105,107,108,109,110,111,112,113,114,115,119,120,121,122,123,124,125,126,127,128,129,133,134,135,136,137,138,139,140,141,142,143,],[-2,-3,-4,-5,-6,-7,-30,-76,59,59,-32,-34,-35,-14,59,59,-76,-76,96,-74,-16,-25,-33,-36,-13,96,96,-76,-8,-9,-10,-11,-12,-75,96,96,96,96,-76,-76,-58,-76,96,-76,96,-76,96,96,-76,-63,-76,-54,-56,-76,-38,-76,-65,96,-76,-76,-57,-52,-37,-64,-76,-53,-55,-51,]),'RETURN':([3,4,5,6,7,8,19,22,33,34,35,41,52,65,70,76,77,82,83,85,87,90,91,92,93,94,95,96,103,104,108,109,110,111,113,115,118,121,123,124,125,126,127,128,129,134,135,136,137,138,139,140,141,142,143,],[-2,-3,-4,-5,-6,-7,-30,-76,-32,-34,-35,-14,-76,-76,-74,-16,-25,-33,-36,-13,106,-76,-8,-9,-10,-11,-12,-75,106,106,-76,-76,-58,-76,-76,-76,106,-76,-76,-54,-56,-76,-38,-76,-65,-76,-76,-57,-52,-37,-64,-76,-53,-55,-51,]),'LESS_THAN':([10,19,22,28,29,30,31,32,33,34,35,39,48,49,64,78,79,80,81,82,83,102,117,],[24,-30,24,24,57,57,-21,-22,-32,-34,-35,-62,57,57,24,-41,-42,-44,-43,-33,-36,-24,-23,]),'PARENTHESIS_OPEN':([11,12,18,20,],[26,26,-40,-67,]),'NUMBER':([13,25,26,27,38,39,40,43,54,55,56,57,58,59,60,61,62,74,75,],[33,33,-72,51,-18,-62,33,-31,33,-45,-46,-47,-48,-49,-50,33,82,100,-69,]),'TRUE_VALUE':([13,25,26,38,39,40,43,54,55,56,57,58,59,60,61,],[34,34,-72,-18,-62,34,-31,34,-45,-46,-47,-48,-49,-50,34,]),'FALSE_VALUE':([13,25,26,38,39,40,43,54,55,56,57,58,59,60,61,],[35,35,-72,-18,-62,35,-31,35,-45,-46,-47,-48,-49,-50,35,]),'QUOTATION_MARKS':([13,19,25,26,38,39,40,43,54,55,56,57,58,59,60,61,63,],[36,-30,36,-72,-18,-62,36,-31,36,-45,-46,-47,-48,-49,-50,36,83,]),'ASSIGNMENT':([19,22,111,],[-30,43,43,]),'EQUAL':([19,29,30,33,34,35,48,49,82,83,],[-30,55,55,-32,-34,-35,55,55,-33,-36,]),'GREATER_THAN':([19,21,23,24,29,30,33,34,35,42,44,45,48,49,66,82,83,84,101,],[-30,39,39,-61,56,56,-32,-34,-35,39,-60,39,56,56,39,-33,-36,39,39,]),'GREATER_OR_EQUAL':([19,29,30,33,34,35,48,49,82,83,],[-30,58,58,-32,-34,-35,58,58,-33,-36,]),'NOT_EQUAL':([19,29,30,33,34,35,48,49,82,83,],[-30,60,60,-32,-34,-35,60,60,-33,-36,]),'PARENTHESIS_CLOSE':([19,33,34,35,47,50,78,79,80,81,82,83,130,131,132,],[-30,-32,-34,-35,72,72,-41,-42,-44,-43,-33,-36,-68,-70,-71,]),'DOT':([33,],[62,]),'OPEN_BODY':([39,46,67,68,71,72,73,86,],[-62,70,70,70,70,-73,70,70,]),'PIPE':([51,100,],[75,75,]),'ADDITION':([75,116,],[-69,132,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'BLOCK_CODE':([0,22,52,65,90,108,109,111,113,115,121,123,126,128,134,135,140,],[2,41,76,85,110,124,125,41,127,129,136,137,138,139,141,142,143,]),'GV':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[3,3,3,3,91,91,91,3,91,91,91,3,3,3,3,3,3,3,3,3,3,3,3,]),'GC':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[4,4,4,4,92,92,92,4,92,92,92,4,4,4,4,4,4,4,4,4,4,4,4,]),'GF':([0,22,52,65,90,108,109,111,113,115,121,123,126,128,134,135,140,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'GCF':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[6,6,6,6,93,93,93,6,93,93,93,6,6,6,6,6,6,6,6,6,6,6,6,]),'PRINT':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[7,7,7,7,94,94,94,7,94,94,94,7,7,7,7,7,7,7,7,7,7,7,7,]),'EMPTY':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[8,8,8,8,95,95,95,8,95,95,95,8,8,8,8,8,8,8,8,8,8,8,8,]),'TD':([0,13,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[9,37,9,9,9,97,97,97,9,97,97,97,9,9,9,9,9,9,9,9,9,9,9,9,]),'V':([0,9,13,22,23,25,36,37,42,52,54,61,65,84,90,97,106,108,109,111,113,115,121,123,126,128,134,135,140,],[10,22,29,10,44,48,63,64,44,10,78,81,10,44,10,111,122,10,10,10,10,10,10,10,10,10,10,10,10,]),'CN':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'F':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'AO':([0,22,52,65,69,87,88,90,98,99,103,108,109,111,113,115,121,123,126,128,134,135,140,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'ME':([10,22,28,64,],[23,42,53,84,]),'PA':([11,12,],[25,27,]),'VAP':([13,],[28,]),'VA':([13,25,40,54,61,],[30,49,65,79,80,]),'CD':([13,25,],[31,47,]),'FR':([13,],[32,]),'MA':([21,23,42,45,66,84,101,],[38,46,67,68,86,102,117,]),'I':([22,111,],[40,40,]),'PR':([23,42,84,],[45,66,101,]),'CDF':([27,],[50,]),'AC':([28,],[52,]),'S':([29,30,48,49,],[54,61,54,61,]),'MY':([46,67,68,71,73,86,],[69,87,88,98,99,103,]),'PC':([47,50,],[71,73,]),'SE':([51,100,],[74,116,]),'C':([69,87,88,98,99,103,],[89,104,107,112,114,118,]),'MN':([69,88,89,98,99,105,107,112,114,119,120,133,],[90,108,109,113,115,121,123,126,128,134,135,140,]),'RT':([87,103,104,118,],[105,119,120,133,]),'O':([116,],[130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> BLOCK_CODE','PROGRAM',1,'p_PROGRAM','syntactic_analyzer.py',101),
  ('BLOCK_CODE -> GV','BLOCK_CODE',1,'p_BLOCK_CODE','syntactic_analyzer.py',108),
  ('BLOCK_CODE -> GC','BLOCK_CODE',1,'p_BLOCK_CODE','syntactic_analyzer.py',109),
  ('BLOCK_CODE -> GF','BLOCK_CODE',1,'p_BLOCK_CODE','syntactic_analyzer.py',110),
  ('BLOCK_CODE -> GCF','BLOCK_CODE',1,'p_BLOCK_CODE','syntactic_analyzer.py',111),
  ('BLOCK_CODE -> PRINT','BLOCK_CODE',1,'p_BLOCK_CODE','syntactic_analyzer.py',112),
  ('BLOCK_CODE -> EMPTY','BLOCK_CODE',1,'p_BLOCK_CODE','syntactic_analyzer.py',113),
  ('C -> GV','C',1,'p_C','syntactic_analyzer.py',124),
  ('C -> GC','C',1,'p_C','syntactic_analyzer.py',125),
  ('C -> GCF','C',1,'p_C','syntactic_analyzer.py',126),
  ('C -> PRINT','C',1,'p_C','syntactic_analyzer.py',127),
  ('C -> EMPTY','C',1,'p_C','syntactic_analyzer.py',128),
  ('GV -> TD V I VA BLOCK_CODE','GV',5,'p_GV','syntactic_analyzer.py',171),
  ('GV -> TD V BLOCK_CODE','GV',3,'p_GV','syntactic_analyzer.py',172),
  ('GV -> EMPTY','GV',1,'p_GV','syntactic_analyzer.py',173),
  ('PRINT -> AO VAP AC BLOCK_CODE','PRINT',4,'p_PRINT','syntactic_analyzer.py',191),
  ('PRINT -> EMPTY','PRINT',1,'p_PRINT','syntactic_analyzer.py',192),
  ('AO -> SUBTRACTION MA','AO',2,'p_AO','syntactic_analyzer.py',202),
  ('VAP -> V','VAP',1,'p_VAP','syntactic_analyzer.py',209),
  ('VAP -> VA','VAP',1,'p_VAP','syntactic_analyzer.py',210),
  ('VAP -> CD','VAP',1,'p_VAP','syntactic_analyzer.py',211),
  ('VAP -> FR','VAP',1,'p_VAP','syntactic_analyzer.py',212),
  ('FR -> TD V ME PR MA','FR',5,'p_FR','syntactic_analyzer.py',219),
  ('FR -> TD V ME MA','FR',4,'p_FR','syntactic_analyzer.py',220),
  ('AC -> ME SUBTRACTION','AC',2,'p_AC','syntactic_analyzer.py',230),
  ('TD -> INTEGER_TYPE','TD',1,'p_TD','syntactic_analyzer.py',238),
  ('TD -> BOOLEAN_TYPE','TD',1,'p_TD','syntactic_analyzer.py',239),
  ('TD -> DECIMAL_TYPE','TD',1,'p_TD','syntactic_analyzer.py',240),
  ('TD -> STRING_TYPE','TD',1,'p_TD','syntactic_analyzer.py',241),
  ('V -> VARIABLE','V',1,'p_V','syntactic_analyzer.py',249),
  ('I -> ASSIGNMENT','I',1,'p_I','syntactic_analyzer.py',257),
  ('VA -> NUMBER','VA',1,'p_VA','syntactic_analyzer.py',265),
  ('VA -> NUMBER DOT NUMBER','VA',3,'p_VA','syntactic_analyzer.py',266),
  ('VA -> TRUE_VALUE','VA',1,'p_VA','syntactic_analyzer.py',267),
  ('VA -> FALSE_VALUE','VA',1,'p_VA','syntactic_analyzer.py',268),
  ('VA -> QUOTATION_MARKS V QUOTATION_MARKS','VA',3,'p_VA','syntactic_analyzer.py',269),
  ('GC -> CN PA CD PC MY C MN BLOCK_CODE','GC',8,'p_GC','syntactic_analyzer.py',280),
  ('GC -> CN PA CD PC MY MN BLOCK_CODE','GC',7,'p_GC','syntactic_analyzer.py',281),
  ('GC -> EMPTY','GC',1,'p_GC','syntactic_analyzer.py',282),
  ('CN -> IF','CN',1,'p_CN','syntactic_analyzer.py',297),
  ('CD -> V S V','CD',3,'p_CD','syntactic_analyzer.py',309),
  ('CD -> V S VA','CD',3,'p_CD','syntactic_analyzer.py',310),
  ('CD -> VA S V','CD',3,'p_CD','syntactic_analyzer.py',311),
  ('CD -> VA S VA','CD',3,'p_CD','syntactic_analyzer.py',312),
  ('S -> EQUAL','S',1,'p_S','syntactic_analyzer.py',321),
  ('S -> GREATER_THAN','S',1,'p_S','syntactic_analyzer.py',322),
  ('S -> LESS_THAN','S',1,'p_S','syntactic_analyzer.py',323),
  ('S -> GREATER_OR_EQUAL','S',1,'p_S','syntactic_analyzer.py',324),
  ('S -> LESS_OR_EQUAL','S',1,'p_S','syntactic_analyzer.py',325),
  ('S -> NOT_EQUAL','S',1,'p_S','syntactic_analyzer.py',326),
  ('GF -> TD V ME PR MA MY C RT MN BLOCK_CODE','GF',10,'p_GF','syntactic_analyzer.py',334),
  ('GF -> V ME PR MA MY C MN BLOCK_CODE','GF',8,'p_GF','syntactic_analyzer.py',335),
  ('GF -> TD V ME PR MA MY RT MN BLOCK_CODE','GF',9,'p_GF','syntactic_analyzer.py',336),
  ('GF -> V ME PR MA MY MN BLOCK_CODE','GF',7,'p_GF','syntactic_analyzer.py',337),
  ('GF -> TD V ME MA MY C RT MN BLOCK_CODE','GF',9,'p_GF','syntactic_analyzer.py',338),
  ('GF -> V ME MA MY C MN BLOCK_CODE','GF',7,'p_GF','syntactic_analyzer.py',339),
  ('GF -> TD V ME MA MY RT MN BLOCK_CODE','GF',8,'p_GF','syntactic_analyzer.py',340),
  ('GF -> V ME MA MY MN BLOCK_CODE','GF',6,'p_GF','syntactic_analyzer.py',341),
  ('GF -> EMPTY','GF',1,'p_GF','syntactic_analyzer.py',342),
  ('PR -> V','PR',1,'p_PR','syntactic_analyzer.py',361),
  ('ME -> LESS_THAN','ME',1,'p_ME','syntactic_analyzer.py',369),
  ('MA -> GREATER_THAN','MA',1,'p_MA','syntactic_analyzer.py',377),
  ('RT -> RETURN V','RT',2,'p_RT','syntactic_analyzer.py',385),
  ('GCF -> F PA CDF PC MY C MN BLOCK_CODE','GCF',8,'p_GCF','syntactic_analyzer.py',393),
  ('GCF -> F PA CDF PC MY MN BLOCK_CODE','GCF',7,'p_GCF','syntactic_analyzer.py',394),
  ('GCF -> EMPTY','GCF',1,'p_GCF','syntactic_analyzer.py',395),
  ('F -> FOR','F',1,'p_F','syntactic_analyzer.py',410),
  ('CDF -> NUMBER SE NUMBER SE O','CDF',5,'p_CDF','syntactic_analyzer.py',418),
  ('SE -> PIPE','SE',1,'p_PIPE','syntactic_analyzer.py',426),
  ('O -> SUBTRACTION','O',1,'p_O','syntactic_analyzer.py',434),
  ('O -> ADDITION','O',1,'p_O','syntactic_analyzer.py',435),
  ('PA -> PARENTHESIS_OPEN','PA',1,'p_PA','syntactic_analyzer.py',446),
  ('PC -> PARENTHESIS_CLOSE','PC',1,'p_PC','syntactic_analyzer.py',454),
  ('MY -> OPEN_BODY','MY',1,'p_MY','syntactic_analyzer.py',462),
  ('MN -> LESS_OR_EQUAL','MN',1,'p_MN','syntactic_analyzer.py',470),
  ('EMPTY -> <empty>','EMPTY',0,'p_empty','syntactic_analyzer.py',477),
]
