#!/usr/bin/env python
# 
# Copyright 2011-2015 Jeff Bush
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
# See the License for the specific language governing permissions and
# limitations under the License.
# 

import sys
import subprocess

sys.path.insert(0, '../..')
import test_harness

def mmu_test(name):
	test_harness.compile_test(['mmu.c', 'tlb_miss_handler.s'])
	result = test_harness.run_verilator()
	if result.find('TLB test passed') == -1:
		raise TestException('test program did not indicate pass')

test_harness.register_tests(mmu_test, ['mmu'])
test_harness.execute_tests()
