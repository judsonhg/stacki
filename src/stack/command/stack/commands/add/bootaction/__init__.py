# @SI_Copyright@
#                               stacki.com
#                                  v4.0
# 
#      Copyright (c) 2006 - 2017 StackIQ Inc. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#  
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#  
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
#  
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	 "This product includes software developed by StackIQ" 
#  
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY STACKIQ AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL STACKIQ OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# @SI_Copyright@

import stack.commands

class Command(stack.commands.add.command):
	"""
	Add a bootaction specification to the system.
	
	<param type='string' name='action'>
	Label name for the bootaction. You can see the bootaction label names by
	executing: 'stack list bootaction [host(s)]'.
	</param>
	
	<param type='string' name='kernel'>
	The name of the kernel that is associated with this boot action.
	</param>

	<param type='string' name='ramdisk'>
	The name of the ramdisk that is associated with this boot action.
	</param>
	
	<param type='string' name='args'>
	The second line for a pxelinux definition (e.g., ks ramdisk_size=150000
	lang= devfs=nomount pxe kssendmac selinux=0)
	</param>
	
	<example cmd='add bootaction action=os kernel="localboot 0"'>
	Add the 'os' bootaction.
	</example>
	
	<example cmd='add bootaction action=memtest command="memtest"'>
	Add the 'memtest' bootaction.
	</example>
	"""

	def run(self, params, args):

		self.command('set.bootaction', self._argv + [ 'force=no' ])
		return self.rc

		#	
		# regenerate all the pxe boot configuration files
		# including the default.
		#
#		self.command('set.host.boot', self.getHostnames())

