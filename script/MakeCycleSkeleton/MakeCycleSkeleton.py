import os
import sys

cyclename = sys.argv[1]

# .h 파일 생성
out_h = open(cyclename + '.h', 'w')
print(
    '''#ifndef {0}_h
#define {0}_h

#include "AnalyzerCore.h"

class {0} : public AnalyzerCore {{

public:

  void initializeAnalyzer();
  void executeEventFromParameter(AnalyzerParameter param);
  void executeEvent();

  {0}();
  ~{0}();

}};

#endif
'''.format(cyclename),
    file=out_h,
)
out_h.close()

# .C 파일 생성
out_c = open(cyclename + '.C', 'w')
print(
    '''#include "{0}.h"

void {0}::initializeAnalyzer(){{

}}

void {0}::executeEvent(){{

  AnalyzerParameter param;

  executeEventFromParameter(param);

}}

void {0}::executeEventFromParameter(AnalyzerParameter param){{

  if(!PassMETFilter()) return;

  Event ev = GetEvent();

}}

{0}::{0}(){{

}}

{0}::~{0}(){{

}}

'''.format(cyclename),
    file=out_c,
)
out_c.close()

# 출력 안내
print('mv ' + cyclename + '.h $SKFlat_WD/Analyzers/include/')
print('mv ' + cyclename + '.C $SKFlat_WD/Analyzers/src/')
