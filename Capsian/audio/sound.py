## ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# Copyright (c) 2008-2020 pyglet contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Capsian Engine
# Copyright 2020 Alessandro Salerno (Tzyvoski)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------


from locals import *


class DirectionalSound:
    """
    A Directional Sound object is an abstract object that can reproduce sound coming from a direction.
    The direction is automatically calculated thanks to pyglet.media.Player().
    CURRENTLY INCOMPLETE!

    """

    def __init__(self, source, pos, auto_play):
        """
        Creates a direction sound object in the world

        :param source: The file from which the Directional Sound object should retrieve the audio (String)
        :param pos: A position in 3D space (Array [x, y, z])
        :param auto_play: Weather it should play as soon as it's created or not (Boolean)
        """

        self.player          = Framework.media.player.Player()
        self.player.position = pos
        self.source          = source

        if auto_play: self.play()

        # Add this object to the stack
        graphics.stack.append(self)

        # Start the loop
        Framework.clock.schedule_interval(self.update, 1/120)


    # Plays the audio
    def play(self):
        """
        Plays a given directional sound

        :return: Nothing
        """

        self.player.queue(Framework.media.load(self.source, streaming=False))
        self.player.play()


    def update(self, delta_time):
        """
        This method updates the sound.
        It's empty by default and it's called 120 times a second automatically.
        DO NOT CALL THIS YOURSELF!

        :param delta_time:
        :return: Nothing
        """

        pass


    # Dunderscore method
    def __call__(self):
        """
        When the object is called it plays a sound
        This method handles the call

        """

        self.play()