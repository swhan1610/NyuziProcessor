//
// Copyright 2011-2015 Jeff Bush
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//


#pragma once

#define EPERM 1
#define ENOENT 2
#define EIO 5
#define ENOEXEC 8
#define EBADF 9
#define ENOMEM 12
#define EFAULT 14
#define EINVAL 22
#define EMFILE 24 // Too many open files

extern int *__errno_ptr(void);

#define errno (*__errno_ptr())
