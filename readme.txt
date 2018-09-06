---------------------------------------------------------------------
		IP Messenger for Win version 2.06
			H.Shirouzu Sep 08, 2004

		Copyright (C) 1996-2004 SHIROUZU Hiroaki
			All Rights Reserved.
---------------------------------------------------------------------

Contents:

  1. Overview
  2. License
  3. Requirements
  4. Usage
  5. Others
  6. WAN Settings (Broadcast Settings)
  7. Appendices
  8. Support
  9. History
 10. Acknowledgment

======================================================================
  Important notice: comctl32.dll 4.70 or before is a limited version.
  Please check 3. Requirements for more information.
======================================================================

----------------------------------------------------------------------
1. Overview

 - IP Messenger is a pop up style LAN message communication software
   for multi platforms. It is based on TCP and UDP/IP.

 - This software does not require server machine.

 - Folder/file transfer (ver2.00 or later)

 - RSA/Blofish Encryption of commnication data (ver2.00 or later)

 - Simple, lightweight, and free software :-)

 - IPMsg software is available for Win16, MacOS, MacOSX, X11, GTK,
   GNOME, Java and all sources supplied with protocol.
   Please check the URL addresses below.
       http://www.ipmsg.org/index.html.en

----------------------------------------------------------------------
2. License (BSD License)

  Copyright (c) 1996-2004 SHIROUZU Hiroaki All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:

    Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer. 

    Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.

    Neither the name of the SHIROUZU Hiroaki nor the names of its
    contributors may be used to endorse or promote products derived
    from this software without specific prior written permission. 

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE.

----------------------------------------------------------------------
3. Requirements

   MS Windows 95/98/Me/NT4.0/2000/XP/2003
   95/98/NT4.0 ... require comctl32.dll version 5.x or later.
   (If it is installed IE 5.x or later, comctl32.dll will be upgraded)

   Note: For Windows 3.1(and NT3.5x), use IP Messenger for Win16

----------------------------------------------------------------------
4. Usage

 <Install/Uninstall>
   You can install IPMsg into the specified folder and setup or
   re-setup into startup with setup.exe.
   If needed, you can uninstall from control panel. 

 <Task tray icon>
   Left double click on the icon opens a Send Message window.
   Right single click on the icon opens IPMsg menu such as setting,
   absence mode, etc.

 <Send Message Window>
   If [Seal] is checked, it will be sealed message.
   If [Lock] is checked, it will be locked message. The receiver must
   use *receiver's own* password to open a locked message.

   To transfer File/Folder, Drag & Drop File/Folder to Send Window.
   (or selec right button menu on Send Window)

     File/Folder transfer can't be completed until a receiver starts
     to download the file. If a sender re-starts IPMSG, the attachment
     file information becomes clear, and a receiver will not be able
     to download the file.)

   The order of Send Message window header item list can be changed
   by Drag & Drop. Right click and select "Save List Header" for
   saving order.

   Prefix mark of the user list
     ':' indicates absence mode.
     '|' indicates v1.x user. (not supporting File/Folder transfer
         and encryption of commnication data)
     '|'(short line) indicates only for File/Folder transfer.

   Right click on the window and select from the menu: Sort/Filter, 
   Group Select, Search User Ctl+F, File Transfer, (Folder)Transfer, 
   Save List Header, Font Setting, Size Setting, Fix Position, Disp Setting.

   Sort/Filter display order priority
     Sort priority is from small to large number. 
     If there are identical priority data, then go to the detail
     setting -> approx. level user sort setting

 <Receive Message Window>
   Right click on the window and select from the menu: Font Setting,
   Size Setting, Fix Position.

   '+' or '-' charactor in Receive Window title means
   Encryption of commnication data in LAN.
   ('+' means RSA/1024bit and blowfish/128bit encryption)
   ('-' means RSA/512bit and RC2/40bit encrytion)

   If you receive a message with an attachment, then an attachment
   button will be displayed. Folder transfer data can't be overwritten. 

 <Others>
   To make connection to WAN through router, Broadcast setting will
   be required. (See in Broadcast setting for detail).

   Other features are easy to understand.
   Try first, you will see it. (See 8.Appendices and 10.History)

----------------------------------------------------------------------
5. Others

 - Setting is saved in the following registry key.
   \\HKEY_CURRENT_USER\Software\HSTools\IPMsgEng
   (If port number has been set, IPMsg + port number)
   When changing your registry number, please re-start ipmsg.

 - Password for Lock and Seal is saved in registry with encording.

   *******************************************************************
   * If you forget the password, remove it in the following registry *
   * key.  \\HKEY_CURRENT_USER\Software\HSTools\IPMsgEng\PasswordStr *
   *******************************************************************

 - This software can be used for Mail delivery check.
   Check URL at [Support],You will find UNIX mail server software.

 - Normally use 2425 port for TCP/UDP. (See 8. Appendices)
   Use 2425 port only for UDP with no File(Folder) Transfer.  
   (These ports should be activated when using firewall software.)

 - Protocol specification comes with source.(Japanese)

 - Broadcast messaging happens only at [Start/End], [Absencemode],
   [Refresh].

 - Compiled by Visual C++4.1(J)

----------------------------------------------------------------------
6. WAN settings (Broadcast Settings)

 - All bits of Host part have to be 1 in the receiver's IP address. 
   For example, connect to Class C(network 24bit, host 8bit) address
   "aaa.bbb.ccc.ddd", broadcast address will be "aaa.bbb.ccc.255".
   If network uses subnet, it may not work.

 - For more detail check TCP/IP books or ask network administrators.

 - If you have difficulty to connect, especially over two or more
   router connection. Set IP addresses independent.

 - For dialup connection, check [Dialup connection] box on.
   When press [Refresh], member list doesn't go off.

----------------------------------------------------------------------
7. Appendices

 - At startup IPMSG software, you can specify UDP/TCP port number.
   IPMSG can run at multiple sessions.
   For example, using [ipmsg.exe 2426] command, you can contact only
   people who are using 2426 port.

 - You can run as much as you want using different port number.

 - Using more UDP/TCP port number, then 1024 is recommended.
   (Between 10000 - 60000 may be more safer)
   For example, Known NFS software uses 2049/UDP.
   Ask network administrator

 - Specifing NIC (for multi NIC environment)
   ipmsg.exe [port] /NIC nic_ipaddr
   ex) C:\> ipmsg.exe /NIC 192.168.10.100

 - Command Line support
   ipmsg.exe [port] /MSG [/LOG][/SEAL] <hostname or IPaddr> <message>
   ex) C:\> ipmsg.exe /MSG /SEAL localhost Hello.

 - Tips.

   1. CTL+D ... boss is coming.(toggle of hide/show windows)

   2. CTL+RefreshButton ... remain existing members, and refresh

   3. ALT+CTL+'S'/'R' ... Send/Recv Hotkey (need detail settings)

   4. CTL+F ... open search user box in send window
 
----------------------------------------------------------------------
8. Support

 - ipmsg-ML is opened. If you want to subscribe for this ML, 
   mail to ipmsg-subscribe@ring.gr.jp

 - Any bug report, suggestion and recommendations are welcome.

 - If you have any question, send to Mailing list.
 
 - For these report, please send the following information.
   Software Version, Operating System, problem situation, repeatability.

----------------------------------------------------------------------
9. History

  ver 1.00 ... Official public version (1996/08/19)

  ver 1.31 ... English version support (1997/09/01)

  ver 2.00 ... Official public version (2002/11/19)
               File/Folder Transfer function support
	       Encrypted communication path support 

  ver 2.03 ... Bug fix (File transfer buffer overflow)
               Hostname(FQDN) support for Broadcast setting 

  ver 2.04 ... Specifying NIC extension

  ver 2.05 ... Bug fix (If a send/recv window is remained,
               logout/shutdown action is failed. only ver2.04 bug)

  ver 2.06 ... Small Refine

----------------------------------------------------------------------
10. Acknowledgment

 - ipmsg-ML members

 - Mr.Kanazawa (English message corrections)

 - Everyone who sent bug reports and suggestions.


